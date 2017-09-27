# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_app.models import User

from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=200)
    users = models.ManyToManyField(User, related_name="cards")
