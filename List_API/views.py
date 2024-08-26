from rest_framework import viewsets
from List_API.models import Task
from List_API.serializer import TaskSerializer


# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer