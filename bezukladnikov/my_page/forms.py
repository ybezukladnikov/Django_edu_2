from django import forms
from .models import SportsGround
from django.core.exceptions import ValidationError


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


