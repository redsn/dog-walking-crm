from django.shortcuts import render, redirect
from .models import Dog, Activity
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import ActivityForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    ## Change this to .filter(userid) when needed
    dogs = Dog.objects.filter()
    return render(request, 'dogs/index.html', {'dogs': dogs})


def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    activity_form = ActivityForm()
    return render(request, 'dogs/detail.html', {'dog': dog, 'activity_form': activity_form})

def add_activity(request, dog_id):
    form = ActivityForm(request.POST)
    if form.is_valid():
        new_activity = form.save(commit=False)
        new_activity.dog_id = dog_id
        new_activity.save()
    return redirect('dog_detail', dog_id=dog_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else: 
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class DogCreate(CreateView):
    model = Dog
    fields = ('name', 'breed', 'coatcolor', 'notes', 'ownername', 'ownerphone', 'owneraddress')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DogUpdate(UpdateView):
    model = Dog
    fields = '__all__'


class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'


