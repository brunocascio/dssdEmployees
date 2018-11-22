# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from app.models import Employee, EmployeeType
from app.serializers import EmployeeSerializer, EmployeeTypeSerializer

# Create your views here.


class EmployeeTypeViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows employeetypes to be viewed or edited.
  """
  queryset = EmployeeType.objects.all()
  serializer_class = EmployeeTypeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows employees to be viewed or edited.
  """
  serializer_class = EmployeeSerializer
  queryset = Employee.objects.all()

  def get_queryset(self):
    queryset = Employee.objects.all()
    email = self.request.query_params.get('email', None)
    if email is not None:
      queryset = queryset.filter(email=email)
    return queryset