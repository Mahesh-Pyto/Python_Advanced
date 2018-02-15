# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Apps

# Create your views here.

def app_details(request):

    details = Apps.objects.get.all()
    return render(request,'app_details.html',{'details':details})
