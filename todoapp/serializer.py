# serializer.py
from rest_framework import serializers
from .models import Task  # Change the model name to Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
