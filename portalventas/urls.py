
from django.contrib import admin
from django.urls import path,re_path,include

app_name = 'init_app'
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('',include('applications.Users.urls')),
    re_path('',include('applications.Producto.urls')),
    re_path('',include('applications.PaginaVenta.urls')),
    re_path('',include('applications.Proveedor.urls')),
    re_path('',include('applications.main.urls')),
    re_path('',include('applications.Compra.urls'))
]
