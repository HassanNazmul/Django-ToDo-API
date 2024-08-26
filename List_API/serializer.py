from rest_framework import serializers
from List_API.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = 'id, title, description, completed, priority, created_at'
        fields = '__all__'
