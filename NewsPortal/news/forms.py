from django import forms
from django.core.exceptions import ValidationError
from .models import Post
from django.utils.translation import gettext_lazy as _

class PostForm(forms.ModelForm):
   title = forms.CharField(max_length=255, label='Заголовок:')

   class Meta:
       model = Post
       fields = [
           'title',
           'content',
           #'rating',
           'author',
           'cathegory',
           # 'is_news',
       ]
       labels = {
           'content': _('Текст'),
           'author': _('Автор:'),
           'cathegory': _('Категории:'),
       }

   def clean(self):
       cleaned_data = super().clean()
       content = cleaned_data.get("description")
       if content is not None and len(text) < 20:
           raise ValidationError({
               "content": "Статья/новость не может быть менее 20 символов."
           })

       # title = cleaned_data.get("title")
       # if len(title) > 255:
       #     raise ValidationError(
       #         "Заголовок не должно быть длиннее 255 символов."
       #     )

       return cleaned_data
