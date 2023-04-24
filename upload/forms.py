from django import forms


class UploadZipForm(forms.Form):
    zip_file = forms.FileField()
    file_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'file_name'}))

