from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    password = models.TextField()
    email = models.EmailField(unique=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Project(models.Model):
    PROJECT_MODELS = (
        ("YOLO-V8", 'YOLO-V8'),
        ("YOLO-V7", 'YOLO-V7'),
        ("YOLO-V6", 'YOLO-V6'),
        ("YOLO-V5", 'YOLO-V5'),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    project_image = models.ImageField(upload_to='project-images')
    project_name = models.CharField(max_length=100)
    project_model = models.CharField(max_length=20, choices=PROJECT_MODELS)
    is_public = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    changed_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name


class ColorSpace(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='colorspace')

    def __str__(self):
        return self.name
