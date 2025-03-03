from django.shortcuts import render
from password_manager.models import EntryPassword
from django.core.exceptions import ImproperlyConfigured


class MixinFormValidTemplate:
    success_template = None
    object = EntryPassword.objects.all()
    
    def get_success_template(self):
        if not self.success_template:
            raise ImproperlyConfigured("No template to response to. Provide a success_template")
        return str(self.success_template) 
    
    
    def form_valid(self, form):
        response = super().form_valid(form)
        return render(self.request, self.get_success_template(), context={
            self.context_object_name: self.object
        })
