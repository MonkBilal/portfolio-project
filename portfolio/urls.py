
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobs.urls'), name='jobs'),
    path('blog/',include('blog.urls'), name='blog'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
