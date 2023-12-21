from django.urls import path
from .import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home),
    path('book/',views.booklist,name='booklist'),
]
if(settings.DEBUG):
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)