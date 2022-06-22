from django.contrib import admin
from django.urls import path
from file_storage.views import file_show,file_upload
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', file_upload.as_view(template_name ='file_storage/base.html'), name="page1"), 
    path('file_show/',file_show.as_view(template_name='success.html'), name='file_show'), 
    
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
