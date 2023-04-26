from django import forms
from app.models import *
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['topic_name','name','url']
        #exclude=['email']
        widgets={'url':forms.PasswordInput,'name':forms.Textarea(attrs={'cols':5,'rows':5})}
        labels={'un':'username','url':'password'}
        help_texts={'topic_name':'cricket','name':'dhoni'}

class AccessForm(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'