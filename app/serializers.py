# we can create serializer in models.py as well
# from .models import Employee, User
from rest_framework import serializers
from .models import *
# from django.contrib.auth.models import User

# class EmployeeSerializer(serializers.Serializer):
# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         # for access particular field we can do like this
#         fields = ['name', 'email']
#         # for access all fields we can do like this
#         fields = '__all__'

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
       model = ToDo
       fields = ('id', 'Title', 'Description', 'Date', 'Completed')

    # name = serializers.CharField(max_length=30)
    # email = serializers.EmailField(max_length=30)
    # password = serializers.CharField(max_length=30)
    # phone = serializers.CharField(max_length=10)

    # def create(self, validated_data):
    #     print("Create Method called")
    #     return Employee.objects.create(**validated_data)
    
    # def update(self, employee, validated_data):
    #     newEmployee = Employee(**validated_data)
    #     newEmployee.id = employee.id;
    #     newEmployee.save()
    #     return newEmployee

# this will access auth user in database
# class UserSerializer(serializers.Serializer):
# class UserSerializer(serializers.ModelSerializer):
#    class Meta:
#     model = User
#     fields = '__all__'
    # username = serializers.CharField(max_length=30)
    # email = serializers.EmailField(max_length=30)
    # password = serializers.CharField(max_length=30)
    # first_name = serializers.CharField(max_length=10)
    # last_name = serializers.CharField(max_length=10)
