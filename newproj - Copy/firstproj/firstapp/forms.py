from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django_recaptcha.fields import ReCaptchaField




class userform(forms.ModelForm):
    password = forms.CharField(max_length=100,widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password']
    captcha = ReCaptchaField()




# class media(forms.ModelForm):
#     class Meta:
#         model = media
#         firlds ="__all__"
    



