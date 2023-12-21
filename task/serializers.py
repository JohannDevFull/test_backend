from rest_framework import serializers
from .models import Task

class TaskSerializers( serializers.ModelSerializer ):
    class Meta:
        model = Task
        fields = ( 'id' , 'title' , 'description' , 'deadline' , 'status' , 'user_id' , 'created_at' )