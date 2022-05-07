import random

from django.shortcuts import render
from datetime import datetime
from django.views import View
from django.http import HttpRequest, HttpResponse
from  random import random


class DatetimeView(View):
    def get(self, request: HttpRequest)-> HttpResponse:
        now = random()

        return HttpResponse(now)
