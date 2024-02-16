from django.shortcuts import render
from app.models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
class SchoolList(ListView):
    model=School
    context_object_name='schools'
    ordering=['sname']
    #queryset=School.objects.filter(id=1)
    #template_name='app/school_list.html'

class SchoolDetail(DetailView):
    model=School
    context_object_name='sclobj'

class SchoolCreate(CreateView):
    model=School
    fields='__all__'

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'

class SchoolDelete(DeleteView):
    model=School
    context_object_name='scl'
    success_url=reverse_lazy('SchoolList')

    


