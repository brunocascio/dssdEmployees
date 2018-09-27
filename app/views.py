# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from app.models import Product, ProductType
from app.serializers import ProductSerializer, ProductTypeSerializer

# Create your views here.


class ProductTypeViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows producttypes to be viewed or edited.
  """
  queryset = ProductType.objects.all()
  serializer_class = ProductTypeSerializer


class ProductViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows products to be viewed or edited.
  """
  queryset = Product.objects.all()
  serializer_class = ProductSerializer