from django import forms
from .models import images


class imagesCreationForm(forms.ModelForm):
    class Meta:
        model = images
        fields = ('title', 'url', 'description')
        widgets = {
            'url': forms.HiddenInput
        }


def clean_url(self):
    url = self.cleaned_data['url']
    valid_extensions = ['jpg', 'jpeg']
    extension = url.rsplit('.', 1)[1].lower()
    if extension not in valid_extensions:
        raise forms.ValidationError('the given url doesnot '
                                    'match valid image extensions')
    return url
