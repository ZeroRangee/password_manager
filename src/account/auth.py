from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model  
from account.service.otp import OTPService



UserModel = get_user_model()

class AuthBackend(ModelBackend):
    
    def authenticate(self, request, username=None,otp= None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if username is None or otp is None:
            return
        

        user = UserModel._default_manager.get_by_natural_key(username)
        
        if not user.is_staff:
            if OTPService.verify_otp(username, otp) and self.user_can_authenticate(user):
                return user


        elif user.check_password(password) and self.user_can_authenticate(user):
            return user