from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

def product_update(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form, 'product': product})

def product_delete(request, product_id):
    # Recupere o objeto Product que você deseja excluir ou retorne um erro 404 se não existir.
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        # Se a solicitação for um POST, isso significa que o usuário confirmou a exclusão.
        product.delete()
        return redirect('product_list')

    # Se a solicitação for um GET, exiba a página de confirmação de exclusão.
    return render(request, 'products/product_confirm_delete.html', {'product': product})

