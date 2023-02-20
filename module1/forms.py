from django.forms import ModelForm
from .models import imagedata


class UploadForm(ModelForm):
    class Meta:
        model = imagedata
        fields = '__all__'
