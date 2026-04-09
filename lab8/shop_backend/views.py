from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .serializers import ProductSerializer
serializer_class = ProductSerializer


from .models import Category, Product


def _serialize_category(category: Category) -> dict:
    return {
        'id': category.id,
        'name': category.name,
    }


def _serialize_product(product: Product) -> dict:
    return {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'rating': product.rating,
        'images': product.images,
        'link': product.link,
        'likes': product.likes,
        'categoryId': product.category_id,
    }


def api_overview(request):
    return JsonResponse(
        {
            'message': 'Lab 8 shop API',
            'endpoints': {
                'products': '/api/products/',
                'product_detail': '/api/products/<id>/',
                'categories': '/api/categories/',
                'category_detail': '/api/categories/<id>/',
                'category_products': '/api/categories/<id>/products/',
            },
        }
    )


def products(request):
    data = [_serialize_product(product) for product in Product.objects.select_related('category')]
    return JsonResponse(data, safe=False)


def product_detail(request, product_id):
    product = get_object_or_404(Product.objects.select_related('category'), pk=product_id)
    return JsonResponse(_serialize_product(product))


def categories(request):
    data = [_serialize_category(category) for category in Category.objects.all()]
    return JsonResponse(data, safe=False)


def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return JsonResponse(_serialize_category(category))


def category_products(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    data = [_serialize_product(product) for product in category.products.all()]
    return JsonResponse(data, safe=False)

def filter_ascending(request):
    data = [_serialize_product(product) for product in Product.objects.order_by('price')]
    return JsonResponse(data, safe=False)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def get_discount(request, pk):
    product = get_object_or_404(Product, pk=pk)
    price = float(product.price)
    discount_price = round(price * 0.9, 2)
    
    return Response({
        "price": price,
        "discount": discount_price
    })
