from django.shortcuts import render
from product.models import Product, ProductImage
from context.contextBuilder import manufacturerContext
from product.forms.form import ProductAdd, ProductImageForm
from django.shortcuts import render, redirect






# Create your views here.
'''Allows staff member to add product. This view adds the product Information'''
def addProduct(request):
    context = manufacturerContext(request)
    ProductFill = ProductAdd(data=request.POST)
    if request.method == 'POST':
        if ProductFill.is_valid():
            name = ProductFill.cleaned_data.get('name')
            releaseDate = ProductFill.cleaned_data.get('releaseDate')
            description = ProductFill.cleaned_data.get('description')
            price = ProductFill.cleaned_data.get('price')
            category_id = ProductFill.cleaned_data.get('category_id')
            platform_id = ProductFill.cleaned_data.get('platform_id')
            condition = ProductFill.cleaned_data.get('condition')
            Product.objects.create(name=name, releaseDate=releaseDate, description=description, price=price,
                                   category_id=category_id, platform_id=platform_id, condition=condition)
            return redirect('staff-addImage')
    else:
        ProductFill = ProductAdd()
    context['form'] = ProductFill
    return render(request, 'staff/addProduct.html', context)


'''Allows staff member to add product. This view adds the product image. Staff member must add 2 photos '''
def addImage(request):
    context = manufacturerContext(request)
    productImage = ProductImageForm(data=request.POST)
    if request.method == 'POST':
        if productImage.is_valid():
            image = productImage.cleaned_data.get('productImage')
            image2 = productImage.cleaned_data.get('productImage2')
            product = Product.objects.order_by('-id')[0]
            ProductImage.objects.create(productImage=image, product_id=product.id)
            ProductImage.objects.create(productImage=image2, product_id=product.id)
            return redirect('staff-index')
    else:
        productImage = ProductImageForm()
    context['form'] = productImage
    return render(request, 'staff/addImage.html', context)
