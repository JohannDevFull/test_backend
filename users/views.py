from rest_framework import generics , authentication , permissions
from rest_framework.authtoken.views import ObtainAuthToken 
from users.serializers import UserSerializer , AuthTokenSerializer

from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes


@extend_schema(
  description='Crear usuario - hola mundo', 
  methods=["POST"]
)
class CreateUserView( generics.CreateAPIView  ):
  serializer_class = UserSerializer

@extend_schema(
  description='Actualizar usuario', 
  methods=["POST"]
)
class RetreiveUpdateUserView( generics.RetrieveUpdateAPIView ):
  serializer_class = UserSerializer
  authentication_classes = [authentication.TokenAuthentication]
  permissions_class = [permissions.IsAuthenticated]
  
  def get_object(self):
    # return Response({"message": "Hello, world!"})
    return self.request.user
  
@extend_schema(
  description='Generar token', 
  methods=["POST"]
)
class CreateTokenView( ObtainAuthToken ):
  serializer_class = AuthTokenSerializer
