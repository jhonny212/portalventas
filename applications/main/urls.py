from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main_app'
urlpatterns = [
    path('main/', views.main.as_view(),name='main'),
    path('', views.main.as_view(),name='main'),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)