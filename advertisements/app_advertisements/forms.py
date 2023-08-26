from django import forms
from app_advertisements.models import Advertisement

class AdvertisementForm(forms.ModelForm):
    title = forms.CharField(max_length=64)
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control form-control-lg'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control form-control-lg'}))
    auction = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control form-control-lg'}))

    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']


    