from django import forms
from .models import game

class GameUpload(forms.ModelForm):
    class Meta:
        model = game
        fields = ['Image_View', 'title', 'supports', 'description', 'HTML_file', 'JS_file', 'CSS_file']
        


class ReportForm(forms.Form):
    subject = forms.CharField(max_length=80)
    your_name = forms.CharField(max_length=50)
    your_email = forms.EmailField()
    browser_name = forms.CharField(required = True ,max_length=150)
    message = forms.CharField(required=True,widget=forms.Textarea)
    screenshot = forms.ImageField(required=False)
