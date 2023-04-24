import os

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from project.models import Project, ColorSpace
from upload.models import UploadedZip
from project.forms import CreateProjectForm
from django.http import HttpResponse
from dotenv import load_dotenv
import zipfile
from backend.veri_hazirlama import VeriHazirlama

load_dotenv()  # loading .env file


# if user is not logged in, don't show the page.
# this function returns current user's projects.
# project function
@login_required
def projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        'projects': projects,
    }
    return render(request, 'project/project.html', context)


# when you want to create a new project, this function will be call.
# this function work with forms. Forms get from forms.py.
# if method==post, get values from form and create a new row in our database. Then save.
# if method==get, forms will load. And return a form with htmx library.(search about it)
def create_project(request):
    if request.method == 'POST':
        project_image = request.FILES['project_image']
        project_name = request.POST['project_name']
        project_model = request.POST['project_model']
        if not project_image:
            return HttpResponse('please load a image')
        elif not project_name:
            return HttpResponse('please fill in all the fields')
        elif not project_model:
            return HttpResponse('please fill in all the fields')
        else:
            project = Project.objects.create(owner_id=request.user.id,
                                            project_image=project_image,
                                            project_name=project_name,
                                            project_model=project_model)
            project.save()
            return redirect('/')
    else:
        form = CreateProjectForm()
        context = {
            'form': form,
        }
        return render(request, 'project/partials/create-project.html', context)


# when user click a project this function will work
# if method is post, first get old datas selected project
# then if user wants change the current datas get input datas.
# if user don't want change the old photo, set project_image as old project-image
# then update new datas to database and redirect project detail page again
# if method is get load project informations
def project_detail(request, pk):
    if request.method == 'POST':
        instance = Project.objects.get(id=pk)
        project_name = request.POST['name_input']
        project_model = request.POST['model_choice']
        if request.POST['image-input']:
            project_image = request.POST['image-input']
        else:
            project_image = instance.project_image
        Project.objects.update(project_name=project_name,
                               project_model=project_model,
                               project_image=f'project-images/{project_image}')

        return redirect(f'/project/{pk}')
    else:
        project = Project.objects.get(id=pk)
        try:
            file = UploadedZip.objects.get(project_id=pk)
            context = {
                'project': project,
                'file': file,
            }
        except UploadedZip.DoesNotExist:
            context = {
                'project': project,
            }
        return render(request, 'project/project-detail.html', context)


# when the user want to delete a project, this function will be work.
# first get the selected project
# then get project image path
# create a try except to be sure deleting item.
# use os.remove() for delete item
# after that delete the project from database and redirect home link
def delete_project(request, pk):
    project = Project.objects.get(id=pk)  # get project object
    try:
        project_file = UploadedZip.objects.get(project_id=pk)
        project_image_path = f'C:/Users/ali.yildirim/projects/aiproject/web{project.project_image.url}' # get item path
        project_file_path = f'C:/Users/ali.yildirim/projects/aiproject/web{project_file.zip_file.url}'
        # change this path when you deploy the website !!!!
        os.remove(project_image_path)  # remove item
        os.remove(project_file_path)  # remove file
        print('the image successfully deleted')  # print successful
    except UploadedZip.DoesNotExist:
        project = Project.objects.get(id=pk)  # get project object
        project_image_path = f'C:/Users/ali.yildirim/projects/aiproject/web{project.project_image.url}' # get item path
        os.remove(project_image_path)  # remove item
        print('the image successfully deleted')  # print successful
    except OSError as error:
        print(f'Error deleting file {project_image_path}: {error}')  # print error
        print(f'Error deleting file {project_file_path}: {error}')  # print error

    project.delete()  # delete from database
    return redirect('/')


def file_detail(request, pk):
    zip = UploadedZip.objects.get(id=pk)
    with zipfile.ZipFile(zip.zip_file, 'r') as zip_file:
        list = zip_file.namelist()
        context = {
            'zip': zip,
            'zip_list': list,
            'pk': pk,
        }
    return render(request, 'project/file-detail.html', context)


def file_image(request, pk, file_name):
    zip = UploadedZip.objects.get(id=pk)
    with zipfile.ZipFile(zip.zip_file, 'r') as myzip:
        img_info = myzip.getinfo(file_name).filename
        with myzip.open(img_info) as image:
            img = image.read()
            return HttpResponse(content=img, content_type='image/jpeg')



# when user want to choose color space, this function will work
# get pk in url, and c_space -> write this param in your redirect url
# first get current project
# define try except block for getting choice
# if c_space not null get choice
# else get original image from database
def color_space(request, pk, c_space=None):
    project = Project.objects.get(id=pk)
    try:
        image = ColorSpace.objects.get(name=c_space)
    except ColorSpace.DoesNotExist:
        image = ColorSpace.objects.get(name='original')
    context = {
        'project': project,
        'image': image.image,
        'image_name': image.name,
    }
    return render(request, 'project/colorspace.html', context)


def change_image(request, color_space):
    image = ColorSpace.objects.get(name=color_space).image
    return render(request, 'project/return-image.html', {'image': image})


def apply_all(request, pk):
    return HttpResponse(f"<div class='alert' id='closeBtn'>Colorspace applied for all images successfully"
                        f"<a href='/project/colorspace/{pk}'>"
                        f"<i class='fa-solid fa-xmark'></i>"
                        f"</a>"
                        "</div>")


def control_data(request, zip_id):
    zip_file = UploadedZip.objects.get(id=zip_id).zip_file
    load_dotenv()
    size = (2160, 3840)
    path = f"{os.getenv('FILE')}{zip_file.url}" '/media/project-files/zipname'
    control = VeriHazirlama(path=path, size=size).remove()
    return render(request, 'project/partials/_control-data.html', context={'result': control})


def convert_data(request, zip_id, class_dict):
    pass