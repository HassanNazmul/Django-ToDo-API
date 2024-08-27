from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filter

from List_API.models import Task
from List_API.serializer import TaskSerializer


# Create your views here.
# Custom Filter and Ordering
class TaskFilter(filter.FilterSet):
    category_name = filter.CharFilter(field_name='category__name', lookup_expr='icontains')

    class Meta:
        model = Task
        fields = ['priority', 'completed', 'category_name', 'status']

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # filterset_fields = ['priority', 'completed'] # Commented out to use custom filter
    filterset_class = TaskFilter
    ordering_fields = ['created_at', 'due_date', 'priority', 'status']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
