from django import forms
from django.core.exceptions import ValidationError

from app_advertisements.models import Advertisement

class AdvertisementForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['description'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['image'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['price'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['auction'].widget.attrs['class'] = 'form-check-input'

    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']

    def title_name_exception(self):
        title = self.cleaned_data['title']
        if title.startwith('?'):
            raise ValidationError('Неверное название. Заголовок не должен начинаться с "?"')
        return title