from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .serializers import taskSeri
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class taskAPI (APIView):
    permission_classes= [IsAuthenticated]
    def get (self, request):
        tasks=Task.objects.filter(user = request.user.id)
        task_seri=taskSeri (tasks, many=True)
        return Response(task_seri.data)
    def post (self, request):
        request.data['user'] = request.user.id
        task_seri=taskSeri (data=request.data)
        if task_seri.is_valid():
            task_seri.save ()
            return Response(task_seri.data)
        else:
            return Response(task_seri.errors)
    def patch(self, request):
        task_id=request.data.get ("id", None)
        uslov =Task.objects.get (id=task_id, user = request.user.id)
        task_seri= taskSeri (uslov, data=request.data, partial=True)
        if task_seri.is_valid ():
            task_seri.save()
            return Response(task_seri.data)
        else:
            return Response(task_seri.errors)
    def delete (self, request):
        task_id=request.data.get ("id", None)
        try:
            id = Task.objects.get(id = task_id,user = request.user.id)
            id.delete()
        except Task.DoesNotExist:
            return Response({"info":"Zadacata ne postoi"})
        return Response({"info":"Zadacata e izbrisana"})
        

class taskid (APIView):
    permission_classes= [IsAuthenticated]
    def get (self, request):
        if request.GET.get("id", None):
            id= int (request.GET.get ("id",0))
            taski=Task.objects.get (id=id,user = request.user.id)
            taskiap= taskSeri(taski)
            return Response (taskiap.data)
        return Response({"error":"Fali id na task"})

class taskcom(APIView):
    permission_classes= [IsAuthenticated]
    def get (self, request):
        if request.GET.get("status", None): 
            status = bool(request.GET.get("status", False))
            taskc=Task.objects.filter (completed=status,user = request.user.id)
            taskcap= taskSeri(taskc)
            return Response (taskcap.data)
        return Response ({"error":"Fali status  na task"})

class promena (APIView):
    permission_classes= [IsAuthenticated]
    def post (self, request):
        id = Task.objects.get (id=request.data.get ("id",None, user = request.user.id))
        if id.completed ==True:
            id.completed = False
        else:
            id.completed = True
        id.save ()
        task_seri=taskSeri (id)
        return Response (task_seri.data) 
    
class KlasaPermisii(APIView):
    permission_classes= [IsAuthenticated]
    def get(self, request):
        print(request.user)
        return Response({"info": "uspesen request"})