from __future__ import unicode_literals

from django.db import models
import re, bcrypt

# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def validate_and_create_user(self, form_data):
        errors = []

        name = form_data['name']
        email = form_data['email']
        password = form_data['password']
        confirm_password = form_data['confirm_password']

        if len(name) < 1:
            errors.append('Name cannot be blank.')
        if len(name) < 2:
            errors.append('Name must be longer than 2 characters.')
        if len(email) < 1:
            errors.append('Email cannot be blank.')
        elif not EMAIL_REGEX.match(email):
            errors.append('You must enter a valid email address!')
        if len(password) < 1:
            errors.append('Password cannot be blank.')
        if len(password) < 3:
            errors.append('Password must be at least 3 characters long.')
        if len(confirm_password) < 1:
            errors.append('Confirm password cannot be blank.')
        if password != confirm_password:
            errors.append('Passwords do not match!')

        if errors:
            return (False, errors)

        # REMEMBER TO HASH THE PASSWORD
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user = self.create(name=name, email=email, pw_hash=pw_hash, permission_level='STUDENT')
        
        # user = {
        #     'name': name,
        #     'email': email,
        #     'password': password,
        #     'pw_hash': password,
        #     'permission_level': 'STUDENT'
        # }
        
        # if not 'users' in request.session:
        #     request.session['users'] = [user]
        # else:
        #     request.session['users'].append(user)
        #     request.session.modified = True

        # if 'user_id' not in request.session:
        #     user_id = False
        # else:
        #     user_id = request.session['users'][user_id]

        return (True, user)
        # return redirect('/users/<user_id>/show'


class User(models.Model):
    # def __init__(self):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=500)
    permission_level = models.CharField(max_length=255)
    # courses = models.ManyToManyField(Course)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return self.email
        
