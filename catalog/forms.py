from django import forms
from catalog.models import Product, Version
from django.forms import BooleanField


class StileFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StileFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ("created_at", "created_user")

    def clean_description(self):
        cleaned_data = self.cleaned_data.get("description")
        forbidden_words = (
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        )

        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError("Нельзя использовать запрещенные слова")
        return cleaned_data


class VersionForm(StileFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
