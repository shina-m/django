#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from addressbook.models import Person

class PersonList(ListView):
    model = Person

class PersonCreate(CreateView):
    model = Person
    success_url = reverse_lazy('person_list')
    fields = ['first_name', 'last_name', 'email']

class PersonUpdate(UpdateView):
    model = Person
    success_url = reverse_lazy('person_list')
    fields = ['first_name', 'last_name', 'email']

class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('person_list')

class PersonIndex(TemplateView):
    template_name = "addressbook/person_index2.html"