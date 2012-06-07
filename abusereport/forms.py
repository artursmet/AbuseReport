from models import AbuseReport
from django import forms
from captcha.fields import ReCaptchaField


class AbuseReportForm(forms.ModelForm):
    """
    Classic ModelForm with CaptchaField.
    """
    catpcha = ReCaptchaField(attrs={'theme': 'white'})

    class Meta:
        model = AbuseReport
        fields = ('author', 'author_email', 'reason')
        widgets = {
            'reason': forms.Textarea(),
        }
