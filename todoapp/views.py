from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializer import TaskSerializer

@api_view(['GET'])
def list_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response({'status': 200, 'data': serializer.data})

@api_view(['GET'])
def get_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        serializer = TaskSerializer(task)
        return Response({'status': 200, 'data': serializer.data})
    except Task.DoesNotExist:
        return Response({'status': 404, 'message': 'Task not found'})

@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 201, 'data': serializer.data})
    return Response({'status': 400, 'message': 'Invalid data'})

@api_view(['PUT', 'PATCH'])
def update_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'data': serializer.data})
        return Response({'status': 400, 'message': 'Invalid data'})
    except Task.DoesNotExist:
        return Response({'status': 404, 'message': 'Task not found'})

@api_view(['DELETE'])
def delete_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
        return Response({'status': 200, 'message': 'Task deleted successfully'})
    except Task.DoesNotExist:
        return Response({'status': 404, 'message': 'Task not found'})
