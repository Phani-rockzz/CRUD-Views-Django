from django.shortcuts import render
from django.urls import reverse_lazy
#importing the different views
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.http import HttpResponse
#importing the model
from app import models

# Create your views here.

class IndexView(TemplateView):
    template_name = 'app/index.html'

# list view example
class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.school




# detail view example
class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.school
    template_name = 'app/schooldetails.html'


class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.school


class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.school

class SchoolDeleteView(DeleteView):
    model = models.school
    template_name = 'app/school_confirm_delete.html'
    success_url = reverse_lazy("app:list")
