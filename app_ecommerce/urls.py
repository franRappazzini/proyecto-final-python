from django.urls import path
from app_ecommerce.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', inicio, name='inicio'),
    path('yo/', yo, name='yo'),

    path('proveedor/list', ProveedorList.as_view(), name='proveedor_list'),
    path(r'^(?P<pk>\d+)$', ProveedorDetalle.as_view(), name='proveedor_detalle'),
    path(r'^create$', ProveedorCrear.as_view(), name='proveedor_crear'),
    path(r'^update/(?P<pk>\d+)$', ProveedorEditar.as_view(),
         name='proveedor_editar'),
    path(r'^delete/(?P<pk>\d+)$', ProveedorEliminar.as_view(),
         name='proveedor_eliminar'),

    path('producto/list', ProductoList.as_view(), name='producto_list'),
    path(r'producto/^(?P<pk>\d+)$',
         ProductoDetalle.as_view(), name='producto_detalle'),
    path(r'producto/^create$', ProductoCrear.as_view(), name='producto_crear'),
    path(r'producto/^update/(?P<pk>\d+)$', ProductoEditar.as_view(),
         name='producto_editar'),
    path(r'producto/^delete/(?P<pk>\d+)$', ProductoEliminar.as_view(),
         name='producto_eliminar'),

    path('cliente/list', ClienteList.as_view(), name='cliente_list'),
    path(r'cliente/^(?P<pk>\d+)$',
         ClienteDetalle.as_view(), name='cliente_detalle'),
    path(r'cliente/^create$', ClienteCrear.as_view(), name='cliente_crear'),
    path(r'cliente/^update/(?P<pk>\d+)$', ClienteEditar.as_view(),
         name='cliente_editar'),
    path(r'cliente/^delete/(?P<pk>\d+)$', ClienteEliminar.as_view(),
         name='cliente_eliminar'),

    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(
        template_name='app_ecommerce/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('edit_user/', edit_user, name='edit_user'),
]
