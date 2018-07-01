# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'polls/ComingSoon.html')

def SpringLoaded(request):
    return render(request, 'polls/SpringLoaded.html')

def Envelope(request):
    return render(request, 'polls/Envelope.html')
