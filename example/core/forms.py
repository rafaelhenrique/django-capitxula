from django import forms
from capitxula import Captcha


class FormExample(forms.Form):
    captcha = Captcha()
