from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# from .models import Employee, User
# from .serializers import EmployeeSerializer, UserSerializer
from .serializers import *
from .models import *
# from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

# Create your views here.


# @csrf_exempt
# @api_view(['GET', 'POST'])
# def employeeListView(request):
#     if request.method == 'GET':
#         employee = Employee.objects.all()
#         serializer = EmployeeSerializer(employee, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         # data read
#         # jsonData = JSONParser().parse(request)  
#         serializer = EmployeeSerializer(data=request.data)
#         print(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# # @csrf_exempt
# @api_view(['DELETE', 'GET', 'PUT'])
# def employeeDetailView(request, pk):
#     try:
#         employee = Employee.objects.get(pk=pk)
        
#     except Employee.DoesNotExist:
#         return Response(status=404)
        
#     # print(employee)
#     if request.method == 'DELETE':
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     elif request.method == 'GET':
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         # jsonData = JSONParser().parse(request) 
#         serializer = EmployeeSerializer(employee, data=request.data)
#         print(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @csrf_exempt
# # api_view(['GET', 'POST'])
# def userListView(request):
#     user = User.objects.all()
#     # print(users)
#     serializera = UserSerializer(user, many=True)
#     return JsonResponse(serializera.data)

class ListToDo(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DetailToDo(generics.RetrieveUpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class CreateToDo(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DeleteToDo(generics.DestroyAPIView):  
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer