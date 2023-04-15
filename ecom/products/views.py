from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product
from products.api.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status


class ProductAV(APIView):
    
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(data={
                "msg":"Data Saved",
                "details":serializer.data
            },status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                "msg":"Data Invalid",
                "details":serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)
            
class ProductDetailsAV(APIView):
    
    def get(self,request,pk):
        if pk is None:
            raise ValueError("Product ID not mentioned...")

        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        
        return Response(serializer.data)
    
    def put(self,request,pk):
        if pk is None:
            raise ValueError("Product ID not mentioned...")
        
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data={
                "msg":"Prodcut updated",
                "details":serializer.data
            },status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        if pk is None:
            raise ValueError("Product ID not mentioned...")
        try:
            product = Product.objects.get(id=pk)
            product.delete()
            return Response({
                "msg":"Deleted",
            },status=status.HTTP_200_OK)
            
        except Product.DoesNotExist:
            return Response({
                "msg":"Object not found..."
            },status=status.HTTP_404_NOT_FOUND)
        
        
        