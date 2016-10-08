from django import forms
from captchula import Captcha


class FormExample(forms.Form):
    captcha = Captcha()
