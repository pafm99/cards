# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Card
from models import User

# Create your views here.
def dashboard(request):
    context = {
        'curr_user': User.objects.get(id = request.session['id']),
        'allcards': Card.objects.all() 
    }

    return render(request, 'cards_app/dashboard.html', context)

def new(request):
    return render(request, 'cards_app/new.html')

def create(request):
    user = User.objects.get(id=request.session['id'])
    user.cards.add(Card.objects.create(name=request.POST['name']))
    return redirect('/cards/')

def add(request, id):
    card =Card.objects.get(id=id)
    user = User.objects.get(id=request.session['id'])
    user.cards.add(card)
    return redirect('/cards/')
