from django import forms

class OtpForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Электронная почта"
            }
        )
    )
    otp = forms.CharField(
        max_length=6,
        widget=forms.TextInput(
            attrs={
                'placeholder': "Пин-код"
            }
        )
    )
