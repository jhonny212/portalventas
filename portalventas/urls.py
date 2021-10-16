
from django.contrib import admin
from django.urls import path,re_path,include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', TemplateView.as_view(template_name='base-content.html'),),
    re_path('',include('applications.Users.urls')),
    re_path('',include('applications.PaginaVenta.urls')),
]
