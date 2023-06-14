from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


# class AddPostForm(forms.Form):
#     '''
#     Данная форма создана как пример для показа возможности
#     создать форму без привязки к базе данных.
#     Если нужны русские поля для формы, то добавляем
#     параметр label=русское_название
#     '''
#     title = forms.CharField(max_length=255)
#     slug = forms.SlugField(max_length=255, label="URL")
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows': 10}))
#     is_published = forms.BooleanField(required=False, initial=True)
#     city = forms.ModelChoiceField(queryset=City.objects.all(), empty_label="City not selected")

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # вызов конструктора базового класса
        self.fields['city'].empty_label = "Category not selected"
    class Meta:
        model = SportsGround
        # fields = '__all__' # Берем все поля из таблицы, кроме тех, что заполняются автоматически
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'city']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        '''
        Пользовательская валидация данных, которые пользователь вносит в форму.
        Сначала отрабатывают стандартные валидаторы согласно полю таблицы.
        А потом уже пользовательские. Обязательно должно содержать
        первое слово clean и через нижнее подчеркивание имя поля,
        которое мы хотим проверить.
        '''
        title = self.cleaned_data['title']
        _MAX_LENGTH = 200
        if len(title) > _MAX_LENGTH:
            raise ValidationError(f'Length exceeds {_MAX_LENGTH} characters')

        return title


class RegisterUserForm(UserCreationForm):
    # Название данныех полей можно посмотреть в админ панели через инспектор элементов.
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    capatcha = CaptchaField()