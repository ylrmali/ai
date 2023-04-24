from django.urls import path
from . import views

app_name = 'upload'

urlpatterns = [
    path('<int:pk>', views.upload_zip, name='upload_zip'),
    path('upload_success/', views.upload_success, name='upload_success'),
]

