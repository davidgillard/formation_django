# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

#from django.shortcuts import render

# Create your views here.

#from django.shortcuts import render
from django.http import HttpResponse

def index(request):
        message = "Salut tout le monde"
        return HttpResponse(message)