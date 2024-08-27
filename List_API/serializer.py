from rest_framework import serializers
from List_API.models import Task, TaskCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCategory
        # fields = ['id', 'name']
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=TaskCategory.objects.all(), source='category', write_only=True)

    class Meta:
        model = Task
        # fields = ['id', 'title', 'description', 'completed', 'priority', 'due_date', 'category', 'category_id', 'created_at']
        fields = '__all__'