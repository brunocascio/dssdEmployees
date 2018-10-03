# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class EmployeeType(models.Model):
  initials = models.CharField(max_length=5)
  description = models.CharField(max_length=100)

  class Meta:
    db_table = "employeetype"

  def __unicode__(self):
    return u"%s" % self.description


class Employee(models.Model):
  firstname = models.CharField(max_length=100)
  surname = models.CharField(max_length=100)
  email = models.EmailField()
  password = models.CharField(max_length=100)
  employeetype = models.ForeignKey(EmployeeType)

  class Meta:
    db_table = "employee"

  def __unicode__(self):
    return u"%s" % self.email
