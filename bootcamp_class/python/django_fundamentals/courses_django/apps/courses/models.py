# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CustomManager(models.Manager):
    def custom_form_validator(self, form_data):
        errors = []
        course_name = form_data['course_name']
        desc = form_data['desc']

        if len(course_name) < 1:
            errors.append("Please enter course name ( > 5 characters )")
        elif len(course_name) < 5:
            errors.append("Please enter course name more than 5 characters")
        if len(desc) < 1:
            errors.append("Please enter description ( > 15 characters )")
        elif len(desc) < 15:
            errors.append("Please enter description more than 15 characters")

        try:
            course = Course.objects.get(course_name=course_name)
            errors.append('asdfr')
            return (False, errors)
        except:
            if len(errors) > 0:
                return (False, errors)
            else:
                course = Course.objects.create(name=course_name, description=desc)
                return (True, course.id)
        return (True, course.id)

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CustomManager()

    def __unicode__(self):
        return "name : " + self.name + ", description : " + ", created_at : " + str(self.created_at)