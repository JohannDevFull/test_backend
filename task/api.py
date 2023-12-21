from .models import Task
from rest_framework import viewsets , permissions
from .serializers import TaskSerializers

class TaskViewSet( viewsets.ModelViewSet ):
    queryset = Task.objects.all()
    permissions_classes = [ permissions.AllowAny ]
    serializer_class = TaskSerializers