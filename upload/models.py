from django.db import models
from project.models import Project


class UploadedZip(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project')
    zip_file = models.FileField(upload_to='project-files/')
    upload_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
