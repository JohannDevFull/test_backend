from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

class Test(APIView):
    
    @extend_schema(description="Obtener todos los elementos")
    def get(self, request):
        # Lógica para obtener todos los elementos del recurso
        # por ejemplo, una consulta a la base de datos
        elementos = ...  # Obtener los elementos desde la base de datos
        # Serializar los datos si es necesario
        return Response({"data": elementos})
    
    @extend_schema(description="Crear un nuevo elemento")
    def post(self, request):
        # Lógica para crear un nuevo elemento
        # por ejemplo, guardar datos en la base de datos
        # request.data contiene los datos enviados en la solicitud POST
        nuevo_elemento = ...  # Crear un nuevo elemento con los datos recibidos
        return Response({"message": "Elemento creado correctamente"}, status=status.HTTP_201_CREATED)
    
    @extend_schema(description="Obtener un elemento por su ID")
    def get(self, request, id):
        # Lógica para obtener un elemento por su ID
        elemento = ...  # Obtener el elemento con el ID proporcionado
        return Response({"data": elemento})
    
    @extend_schema(description="Actualizar un elemento por su ID")
    def put(self, request, id):
        # Lógica para actualizar un elemento por su ID
        elemento = ...  # Obtener el elemento con el ID proporcionado
        # Actualizar el elemento con los datos recibidos
        return Response({"message": "Elemento actualizado correctamente"})
    
    @extend_schema(description="Eliminar un elemento por su ID")
    def delete(self, request, id):
        # Lógica para eliminar un elemento por su ID
        elemento = ...  # Obtener el elemento con el ID proporcionado
        # Eliminar el elemento de la base de datos
        return Response({"message": "Elemento eliminado correctamente"})

