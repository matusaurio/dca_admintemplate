# _*_ coding: utf-8 _*_
import datetime
from django.shortcuts import render
from django.utils.timezone import now


def home(request):
    today = datetime.date.today()
    return render(request, "admintemplate/index.html", {'today': today, 'now': now()})


def home_files(request, filename):
    return render(request, filename, {}, content_type='text/plain')
