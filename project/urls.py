from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.projects, name='project'),
    path('create-project/', views.create_project, name='create-project'),
    path('project/<int:pk>', views.project_detail, name='project-detail'),
    path('project/<int:pk>/delete/', views.delete_project, name='delete-project'),
    path('project/colorspace/<int:pk>', views.color_space, name='color-space'),
    path('project/colorspace/<str:color_space>', views.change_image, name='change_image'),
    path('project/apply/<int:pk>', views.apply_all, name='apply_all'),
    path('project/file-detail/<int:pk>', views.file_detail, name='file_detail'),
    path('project/<int:pk>/<str:file_name>/', views.file_image, name='file_image'),
    path('project/control-data/<int:zip_id>/', views.control_data, name='control_data'),
    
]
