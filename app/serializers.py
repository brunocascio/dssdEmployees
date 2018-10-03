from app.models import Employee, EmployeeType
from rest_framework import serializers

class EmployeeTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = EmployeeType
    fields = ('id', 'initials', 'description')

class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields = ('id', 'firstname', 'surname', 'email', 'employeetype', 'password')
    extra_kwargs = {'password': {'write_only': True}}