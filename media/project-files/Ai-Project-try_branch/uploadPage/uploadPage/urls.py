from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('upload.urls')),

]

# from django.urls import path
# from upload import views
#
# urlpatterns = [
#     path('upload-zip/', views.upload_zip, name='upload_zip'),
# ]

