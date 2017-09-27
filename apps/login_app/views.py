# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from models import User


# Create your views here.
# index -> '/'
def index(request):
    # User.objects.all().delete()
    return render(request, "login_app/index.html")

#register -> '/register'
def register(request):
    results = User.objects.validate(request.POST)
    if results['status'] == True:
        user = User.objects.creator(request.POST)
        messages.success(request, "User was created")
    else:
        for error in results['errors']:
            messages.error(request, error)
    return redirect('/')

def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status'] == False:
        messages.error(request, "Email and/or Password are incorrect")
        return redirect('/')
    request.session['email'] = results['user'].email
    request.session['first_name'] = results['user'].first_name
    request.session['id'] = results['user'].id
    return redirect("/cards/")


def logout(request):
    request.session.flush()
    return redirect('/')