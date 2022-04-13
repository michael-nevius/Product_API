from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product

@api_view(['GET', 'POST'])
def products_list(request):
    if request.method == 'GET':
        products = products.objects.all()
        serilizer = ProductSerializer(products, many=True)   
        return Response(serilizer.data)

    elif request.method == 'POST':
        serilizer = ProductSerializer(data=request.data)
        serilizer.is_valid(raise_exception=True)
        serilizer.save()
        return Response(serilizer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])    
def product_detail(request, pk):
    product = get_object_or_404(product,pk=pk)
    if request.method == 'GET':
        serializer = ProductSerializer(product);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)