from django.shortcuts import render, redirect
from .forms import UploadZipForm
from .models import UploadedZip


def upload_zip(request, pk):
    if request.method == 'POST':
        zip_file = request.FILES['upload']
        name = request.POST['file_name']

        uploaded_zip = UploadedZip.objects.create(project_id=pk, zip_file=zip_file, name=name)
        uploaded_zip.save()
        return redirect(f'/project/{pk}')
    else:
        return render(request, 'upload/upload_zip.html')


def upload_success(request):
    return render(request, 'upload/upload_success.html')

