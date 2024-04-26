from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Taskserializer
from .models import Task
# Create your views here.

@api_view(['GET'])
def apioverview(request):
    api_urls={
        'List':'/task-list/',
        'detail':'/detail-view/<str:pk>/',
        'create':'/task-create/',
        'update':'/task-update/<str:pk>/',
        'delete':'/task-delete/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
    tasks = Task.objects.all()
    serializer = Taskserializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detailview(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = Taskserializer(tasks,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer = Taskserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def update(request,pk):
    task = Task.objects.get(id=pk)
    updated = Taskserializer(instance=task,data=request.data)
    if updated.is_valid():
        updated.save()
    return Response(updated.data)

@api_view(['DELETE'])
def delete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('item deleted')
