from django import forms
from .models import Place

class PlaceForm(forms.Form):
    title = forms.CharField(label="Назва", max_length=200)
    description = forms.CharField(label="Опис", widget=forms.Textarea)
    place_type = forms.CharField(label="Тип місця", max_length=100, required=False)
    location = forms.CharField(label="Локація", max_length=200, required=False)
    rating = forms.IntegerField(label="Рейтинг (1-5)", min_value=1, max_value=5)

    def clean_title(self):
        title = self.cleaned_data.get("title", "").strip()
        if not title:
            raise forms.ValidationError("Назва не може бути порожньою.")
        return title
