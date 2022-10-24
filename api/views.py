
from django.shortcuts import render,get_object_or_404,get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from api.models import Task
from api.serializers import TaskSerializer

# Create your views here.
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List':'/tast-list/',
        'Detail':'/task-details/<int:pk>',
        'Create':'/task-create',
        'Update':'/task-update/<int:pk>',
        'Delete':'/task-delete/<int:pk>'
    }
    return Response(api_urls)

@api_view(['GET'])
def get_all_tasks(request):
    tasks = Task.objects.all().order_by('-id')
    serialize = TaskSerializer(tasks,many=True)
    return Response(serialize.data,status=status.HTTP_200_OK)


@api_view(['GET'])  
def task_details(request,pk):
    task = get_list_or_404(Task, id=pk)
    serialize = TaskSerializer(task,many=True)
    return Response(serialize.data,status=status.HTTP_200_OK)


@api_view(['POST'])
def create_tasks(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_tasks(request,pk):
    task = get_object_or_404(Task, id=pk)
    if task.completed:
        return Response('Completed Tasks can not be updated',status=status.HTTP_400_BAD_REQUEST)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def delete_task(request,pk):
    task = get_object_or_404(Task, id=pk)
    if task.completed:
        return Response('Completed Tasks can not be deleted',status=status.HTTP_400_BAD_REQUEST)
    task.delete()
    
    return Response('Task deleted successfully',status=status.HTTP_200_OK)