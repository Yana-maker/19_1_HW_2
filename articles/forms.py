
from django import forms


from .models import Article
from catalog.forms import StyleFormMixin


class ArticleForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'

