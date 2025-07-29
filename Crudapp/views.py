from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required


@login_required
def product_list(request):
    products = Product.objects.filter(user_name=request.user.username)
    return render(request, 'Crudapp/product_list.html', {'products': products})


@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # 💥 add request.FILES
        if form.is_valid():
            product = form.save(commit=False)
            product.user_name = request.user.username  # 💥 new
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'Crudapp/product_form.html', {'form': form})


@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk, user_name=request.user.username)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)# 💥 add files
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'Crudapp/product_form.html', {'form': form})


@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk, user_name=request.user.username)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'Crudapp/product_confirm_delete.html', {'product': product})


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'Crudapp/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('product_list')
    else:
        form = AuthenticationForm()
    return render(request, 'Crudapp/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
