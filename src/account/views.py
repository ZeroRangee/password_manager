from account.form.otp_auth import OtpForm 
from django.views.generic import FormView, View
from django.views.generic import FormView, View
from core.base.mixins import MixinFormValidTemplate
from django.http import HttpResponse
from account.service.otp import OTPService
from django.contrib.auth import get_user_model,authenticate, login
from password_manager.models import EntryPassword
from django.shortcuts import render
from account.service.otp import OTPService
from django.http import UnreadablePostError
import redis




class Authentication(MixinFormValidTemplate,FormView):
    model = get_user_model()
    form_class = OtpForm
    template_name = 'otp_auth.html'
    success_template = 'blank_page.html'
    context_object_name = "website"
    success_url = "/"
        
    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            if OTPService.verify_otp(form.cleaned_data['email'],form.cleaned_data['otp']):
                user = authenticate(
                    self.request,
                    username=form.cleaned_data['email'], 
                    otp=form.cleaned_data['otp']
                    )

                if user is not None:
                    login(self.request, user)
                    OTPService.delete_otp(form.cleaned_data['email'])
                    return self.form_valid(form)
                return self.form_invalid(form)
            else:
                form.errors["otp"] = "Пин-код не верный"
        return self.form_invalid(form)
    
    





class SendOTPView(View):
    user = get_user_model()
    
    def post(self, request, *args, **kwargs):
        user_email = request.POST["email"]
        try:
            if not self.user.objects.exclude(email = user_email).exists():
                self.user.objects.create_user(email=user_email)
            
            if OTPService.get_stored_otp(user_email):
                return HttpResponse("Письмо уже отправлино на почту", status=200)
            
            otp_code = OTPService.generate_otp(user_email)
            OTPService.send_otp_email(user_email, otp_code)
        
            return HttpResponse("Вам на почту пришел пин-код", status=201)
        except UnreadablePostError:
            return HttpResponse("Некорректные данные запроса", status=400)
