from django.shortcuts import render

from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema , OpenApiParameter
from rest_framework.decorators import api_view,authentication_classes
from rest_framework.generics import get_object_or_404
from django.views.decorators.http import require_http_methods

from rest_framework import status 
from datetime import datetime

from rest_framework.authentication import TokenAuthentication

class ProductListAPIView(APIView):

  @authentication_classes([TokenAuthentication])
  def get(self, request):
      products = Product.objects.all()
      serializer = ProductSerializer(products, many=True)
      return Response(serializer.data)

  @extend_schema(
    description = "Crear un nuevo elemento",
    methods = ['POST'],
    parameters = [OpenApiParameter( 
      name='price', 
      description='Precio', 
      type = float ,
    ) , OpenApiParameter( 
      name='name', 
      description='Nombre', 
      type = str ,
    ) , OpenApiParameter( 
      name='description', 
      description='Descripción', 
      type = str ,
    ) ],
  )
  def post(self, request):

      if request.data['image'] != '':
        image_file = request.FILES['image']
        name_file = request.FILES['image'].name
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        name_file, extension = name_file.split('.')
        dir = 'images/imgs/media/'
        path = f"{dir}{name_file}_{timestamp}.{extension}"
        with open( path , 'wb+') as destination:
          for chunk in image_file.chunks():
              destination.write(chunk)
        url_media = 'media/'
        url = f"{url_media}{name_file}_{timestamp}.{extension}"

        product_data = {
          'name': request.data['name'],  # Asegúrate de tener los demás datos necesarios
          'price': request.data['price'],  # Asegúrate de tener los demás datos necesarios
          'description': request.data['description'],  # Asegúrate de tener los demás datos necesarios
          'path_img': path,
          'url_img': url,
        }
      else:
        product_data = {
          'name': request.data['name'],  # Asegúrate de tener los demás datos necesarios
          'price': request.data['price'],  # Asegúrate de tener los demás datos necesarios
          'description': request.data['description'],
        }

      serializer = ProductSerializer(data=product_data)
      
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailAPIView(APIView):

  def get(self, request, id):
    product = get_object_or_404(Product, id=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

  def put(self, request, id):
    
    if request.data['image'] != '':
      image_file = request.FILES['image']
      name_file = request.FILES['image'].name
      timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
      name_file, extension = name_file.split('.')
      dir = 'images/imgs/media/'
      path = f"{dir}{name_file}_{timestamp}.{extension}"
      with open( path , 'wb+') as destination:
        for chunk in image_file.chunks():
            destination.write(chunk)
      url_media = 'media/'
      url = f"{url_media}{name_file}_{timestamp}.{extension}"

      product_data = {
        'name': request.data['name'],
        'price': request.data['price'],
        'description': request.data['description'],
        'is_active': request.data['is_active'],
        'path_img': path,
        'url_img': url,
      }
    else:
      product_data = {
        'name': request.data['name'],
        'price': request.data['price'],
        'description': request.data['description'],
        'is_active': request.data['is_active'],
        'path_img': request.data['path_img'],
        'url_img': request.data['url_img'],
      }

    product = get_object_or_404( Product , id = id )
    serializer = ProductSerializer( product , data = product_data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class ProductAPIView(APIView):
  @extend_schema(
    description = "Detalle un nuevo elemento",
    methods = ['GET'],
  )
  @api_view([ "GET" ])
  @require_http_methods([ "GET" ]) 
  def detail(self, request, id):
    product = get_object_or_404(Product, id=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
