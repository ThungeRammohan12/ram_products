from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer


# POST - Add product
@api_view(['POST'])
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Product added successfully",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# GET - Search products
@api_view(['GET'])
def search_products(request):
    query = request.GET.get("query", "")
    products = Product.objects.filter(name__icontains=query)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)