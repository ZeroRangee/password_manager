from django import forms
from password_manager.models import EntryPassword

class EntryPasswordForm(forms.ModelForm):


    class Meta:
        model = EntryPassword
        fields = ['website_name','website_url','username','password']

