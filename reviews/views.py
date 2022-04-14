from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReviewSerializer
from .models import Review
from products.models import Product

@api_view(['GET'])
def reviews_list(request):
    
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=200)

@api_view(['GET','POST','PUT','DELETE'])
def review_detail(request,pk):
    request.data.update({"product": pk})

    if request.method == 'GET':
        reviews = Review.objects.filter(product_id=pk)
        serializer = ReviewSerializer(reviews, many=True)
        return Response (serializer.data, status=200)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.data.product, status=400)
