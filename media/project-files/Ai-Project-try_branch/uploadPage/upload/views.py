from django.shortcuts import render, redirect
from .forms import UploadZipForm
from .models import UploadedZip

def upload_zip(request):
    if request.method == 'POST':
        form = UploadZipForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_zip = UploadedZip(zip_file=request.FILES['zip_file'], name=request.POST['name'])
            uploaded_zip.save()
            return redirect('upload_success')
    else:
        form = UploadZipForm()
    return render(request, 'upload_zip.html', {'form': form})

def upload_success(request):

    return render(request, 'upload_success.html')

