from django.shortcuts import render

from .models import Product
from .serializers import ProductSerializer

from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from django.views.decorators.http import require_http_methods


class ProductList( generics.ListAPIView , generics.CreateAPIView  ):
  serializer_class = ProductSerializer

  @extend_schema(description="Obtener todos los elementos")
  @require_http_methods([ "GET" ])
  @permission_classes([IsAuthenticated])
  def ListPrducts(self, request, format=None):
    snippets = Product.objects.all()
    serializer = ProductSerializer(snippets, many=True)
    return Response(serializer.data)

  @extend_schema(description="Crear un nuevo elemento")
  @require_http_methods([ "POST" ])
  def CreateProduct( self, request , format=None ):
    # serializer = Product(data=request.data)
    return Response({"message": "Hello, world!"})
    image_file = request.FILES['image']
    # Aquí puedes validar la imagen o guardarla en el sistema de archivos o en una base de datos
    # Ejemplo de guardado en el sistema de archivos
    with open('ruta/donde/guardar/imagen/nombre_archivo.jpg', 'wb+') as destination:
        for chunk in image_file.chunks():
            destination.write(chunk)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail( generics.RetrieveUpdateDestroyAPIView ):
  model = Product
  serializer_class = ProductSerializer
  lookup_field = "id"
  queryset = Product.objects.all()

  @extend_schema(description="Obtener un elemento por su ID")
  @require_http_methods(['GET'])
  def RetrieveProduct(self, request, id, format=None):
    return Response({"message": "Hello, world!"})
    queryset = self.get_object(id)
    serializer = ProductSerializer(queryset)
    return Response(serializer.data)

  @extend_schema(description="Actualizar un elemento por su ID")
  @require_http_methods(['PUT'])
  def UpdateProduct(self, request, id, format=None):
      product = self.get_object(id)
      serializer = ProductSerializer(product, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  @extend_schema(description="Eliminar un elemento por su ID")
  @require_http_methods(['DELETE'])
  def DestroyPrduct(self, request, id, format=None):
      product = self.get_object(id)
      product.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)


