from django import forms
from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at',)

    def clean_description(self ):
        cleaned_data = self.cleaned_data.get('description')
        forbidden_words = ('казино', 'криптовалюта', 'крипта', 'биржа',
                           'дешево', 'бесплатно', 'обман', 'полиция', 'радар')

        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(
                    'Нельзя использовать запрещенные слова'
                )
        return cleaned_data
