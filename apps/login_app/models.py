# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
# Create your models here.

class UserManager(models.Manager):
    def loginVal(self, postData):
        results = {'status': True, 'errors': [], 'user': None}
        users = self.filter(email = postData['email'])
        if len(users) < 1:
            results['status'] = False
        else:
            if bcrypt.checkpw(postData['password'].encode(), users[0].password.encode()):
                results['user'] = users[0]
            else:
                results['status'] = False
        return results

    def creator(self, postData):
        user = self.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()))
        return user
    def validate(self, postData):
        results = {'status': True, 'errors': []}
        if len(postData['first_name']) < 3:
            results['errors'].append('Your First Name is Too Short')
            results['status'] = False
        if len(postData['last_name']) < 3:
            results['errors'].append('Your Last Name is Too Short')
            results['status'] = False
        if not re.match("[^@]+@[^@]+\.[^@]+", postData['email']):
            results['errors'].append('Your email is not valid')
            results['status'] = False
        if postData['password'] != postData['c_password']:
            results['errors'].append("Your passwords don't match")
            results['status'] = False
        if len(postData['password']) < 5:
            results['errors'].append('Your passwords is too short')
            results['status'] = False            
        if len(self.filter(email = postData['email'])) > 0:
            results['errors'].append('User already exists')
            results['status'] = False
        #check for characters in the future to avoid users from registering with non aplha characters
        return results


        print results
class User(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    password = models.CharField(max_length= 200)
    objects = UserManager()
