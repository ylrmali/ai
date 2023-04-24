from django import forms

class UploadZipForm(forms.Form):
    zip_file = forms.FileField()
    name = forms.CharField()
