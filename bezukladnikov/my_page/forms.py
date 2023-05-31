from django import forms
from .models import *

class AddPostForm(forms.Form):
    '''
    Если нужны русские поля для формы, то добавляем
    параметр label=русское_название
    '''
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255, label="URL")
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows': 10}))
    is_published = forms.BooleanField(required=False, initial=True)
    city = forms.ModelChoiceField(queryset=City.objects.all(), empty_label="City not selected")