from django.shortcuts import render
from app_ecommerce.models import *
# para crear views con class
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# para impedir ingresar a una pagina sin estar autenticado
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import *

# Create your views here.


def inicio(request):
    if request.user.is_authenticated:
        avatares = Avatar.objects.filter(user=request.user.id)
        img = avatares[0].img.url

        return render(request, 'app_ecommerce/index.html', {'url': img, 'user_login': avatares[0]})

    return render(request, 'app_ecommerce/index.html')


def yo(request):
    return render(request, 'app_ecommerce/yo.html')


class ProveedorList(ListView):
    model = Proveedor
    template_name = 'app_ecommerce/proveedor/proveedor_list.html'


class ProveedorDetalle(DetailView):
    model = Proveedor
    template_name = 'app_ecommerce/proveedor/proveedor_detalle.html'


class ProveedorCrear(LoginRequiredMixin, CreateView):
    model = Proveedor
    success_url = '/app_ecommerce/proveedor/list'
    fields = ['nombre', 'tipo']


class ProveedorEditar(LoginRequiredMixin, UpdateView):
    model = Proveedor
    success_url = '/app_ecommerce/proveedor/list'
    fields = ['nombre', 'tipo']


class ProveedorEliminar(LoginRequiredMixin, DeleteView):
    model = Proveedor
    success_url = '/app_ecommerce/proveedor/list'


class ProductoList(ListView):
    model = Producto
    template_name = 'app_ecommerce/producto/producto_list.html'


class ProductoDetalle(DetailView):
    model = Producto
    template_name = 'app_ecommerce/producto/producto_detalle.html'


class ProductoCrear(LoginRequiredMixin, CreateView):
    model = Producto
    success_url = '/app_ecommerce/producto/list'
    fields = ['nombre', 'marca', 'precio', 'stock']


class ProductoEditar(LoginRequiredMixin, UpdateView):
    model = Producto
    success_url = '/app_ecommerce/producto/list'
    fields = ['nombre', 'marca', 'precio', 'stock']


class ProductoEliminar(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = '/app_ecommerce/producto/list'


class ClienteList(ListView):
    model = Cliente
    template_name = 'app_ecommerce/cliente/cliente_list.html'


class ClienteDetalle(DetailView):
    model = Cliente
    template_name = 'app_ecommerce/cliente/cliente_detalle.html'


class ClienteCrear(LoginRequiredMixin, CreateView):
    model = Cliente
    success_url = '/app_ecommerce/cliente/list'
    fields = ['nombre', 'apellido', 'email', 'edad']


class ClienteEditar(LoginRequiredMixin, UpdateView):
    model = Cliente
    success_url = '/app_ecommerce/cliente/list'
    fields = ['nombre', 'apellido', 'email', 'edad']


class ClienteEliminar(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = '/app_ecommerce/cliente/list'


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user_login = authenticate(username=user, password=password)

            if user_login:
                login(request, user_login)

                return render(request, 'app_ecommerce/index.html', {'user_login': user_login})

        else:
            return render(request, 'app_ecommerce/index.html', {'mensaje': 'No has iniciado sesion'})

    else:
        form = AuthenticationForm()

    return render(request, 'app_ecommerce/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()

            return render(request, 'app_ecommerce/index.html', {'mensaje': 'Usuario creado'})

    else:
        form = FormularioRegistro()

    return render(request, 'app_ecommerce/register.html', {'form': form})


def edit_user(request):
    user = request.user

    if request.method == 'POST':
        form = FormularioRegistro(request.POST)

        if form.is_valid():
            info = form.cleaned_data

            user.username = info['username']
            user.email = info['email']
            user.password1 = info['password1']
            user.password2 = info['password1']
            user.save()

            return render(request, 'app_ecommerce/index.html')

    else:
        form = FormularioRegistro(
            initial={'username': user.username, 'email': user.email})

    return render(request, 'app_ecommerce/editar_user.html', {'form': form})
