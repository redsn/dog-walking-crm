from django.shortcuts import render, redirect
from .models import Dog, Activity

from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    pass

def dogs_index(request):
    pass

def dogs_detail(request):
    pass

def add_activity(request):
    pass

class DogCreate(CreateView):
    model = Dog
    fields = ('name', 'breed')
    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)

class DogUpdate(UpdateView):
    model = Dog
    fields = '__all__'


class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'

