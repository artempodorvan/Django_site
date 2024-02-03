# from .models import Articles
from .models import Articles1
from django.forms import ModelForm, TextInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles1
        fields = ['title', 'price', 'description', 'img']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Pizza'
            }),
            "price": TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Price'
            }),
            "description": TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'description'
            })
        }
