# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    age = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return "id: " + str(self.id) + ", first_name: " + self.first_name + ", last_name: " + self.last_name + ", email: " + self.email + ", created_at: " + str(self.created_at) + ", updated_at: " + str(self.updated_at)
