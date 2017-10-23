from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from captcha.fields import CaptchaField


class UserCreateForm(UserCreationForm):

    captcha = CaptchaField()
    mobile = forms.CharField(max_length=50, required=True, help_text='Required.')

    class Meta:
        fields = ('username', 'mobile', 'email', 'password1', 'password2', 'captcha')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Name'
        self.fields['email'].label = 'Email Address'
        self.fields['mobile'].label = 'Mobile Number'
        self.fields['captcha'].label = 'Captcha'
        for fieldname in ['username', 'mobile', 'email', 'password1', 'password2', 'captcha']:
            self.fields[fieldname].help_text = None


class PasswordResetRequestForm(forms.Form):
    email_or_username = forms.CharField(label=("Email Or Username"), max_length=254)