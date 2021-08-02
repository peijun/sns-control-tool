from django import forms
from PIL import Image

class PostForm(forms.Form):
    title = forms.CharField(required=True)
    content = forms.CharField(required=True,widget=forms.Textarea)
    image1 = forms.ImageField(required=False)
    image2 = forms.ImageField(required=False)
    image3 = forms.ImageField(required=False)
    image4 = forms.ImageField(required=False)
