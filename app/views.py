from django.shortcuts import render

# Create your views here.
from app.forms import *

from django.views.generic import FormView

from django.http import HttpResponse


class insertform(FormView):
    form_class = StudForm
    template_name = 'insertform.html'
    
    def form_valid(self,form):
        form.save()
        return HttpResponse('<h1>data inserted............</h1>')