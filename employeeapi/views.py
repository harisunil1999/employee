from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from employeeapi.models import Employee
from employeeapi.serializers import EmployeeSerializer


class EmployeeView(ModelViewSet):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()
    model=Employee
    
