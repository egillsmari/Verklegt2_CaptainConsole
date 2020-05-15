from django import forms
from product.models import Platform, Category
from product.models import Product, ProductImage

def getCategories():
    categoryList = []
    for category in Category.objects.all():
        categoryList.append((category.id, category.name))
    return categoryList

def getPlatform():
    platformList = []
    for platform in Platform.objects.all():
        platformList.append((platform.id, platform.name))
    return platformList

class ProductImageForm(forms.Form):
    productImage = forms.CharField(max_length=255)
    productImage2 = forms.CharField(max_length=255)


    class Meta:
        model = ProductImage
        exclude = ['product_id']
        fields = ('productImage', 'productImage2')


class ProductAdd(forms.Form):
    name = forms.CharField(max_length=255)
    releaseDate = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    description = forms.CharField(max_length=255)
    price = forms.FloatField()
    category_id = forms.ChoiceField(choices=getCategories())
    platform_id = forms.ChoiceField(choices=getPlatform())
    condition = forms.ChoiceField(choices=[('Bad', 'Bad'),
                                           ('Medium', 'Medium'),
                                           ('Good', 'Good'),
                                           ('Mint', 'Mint')])
    class Meta:
        model = Product
        fields = ('name', 'releaseDate', 'description', 'price', 'category_id', 'platform_id', 'condition')




