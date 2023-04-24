from django.urls import path
from . import views

urlpatterns = [
    path('upload-zip/', views.upload_zip, name='upload_zip'),
    path('upload_success/', views.upload_success, name='upload_success'),
]

# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('uploadPage.urls')),
# ]

