
from distutils.log import Log
from django.shortcuts import render, redirect
from .models import Dog, DogPhoto, ActivityPhoto, Activity
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import ActivityForm

import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'sei426-dog-walker-bucket-photo'


# Create your views here.

def about(request):
    return render(request, 'about.html')

def landing(request):
    if request.user.is_authenticated: 
        return render(request, 'home.html')
    else: 
        return render(request, 'landing.html')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def dogs_index(request):
    ## Change this to .filter(userid) when needed
    dogs = Dog.objects.filter(user=request.user)
    return render(request, 'dogs/index.html', {'dogs': dogs})

@login_required
def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    activity_form = ActivityForm()
    return render(request, 'dogs/detail.html', {'dog': dog, 'activity_form': activity_form})

@login_required
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

# Meant for a general photo upload. May need to configure settings for 'main' profile picture

def add_dog_photo(request, dog_id):
    photo_file = request.FILES.get('photo_file')
    if photo_file:
        s3 = boto3.client('s3')
        ## key = name mod for file. 
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f'{S3_BASE_URL}{BUCKET}/{key}'
            photo = DogPhoto(url=url, dog_id=dog_id)
            photo.save()
        except Exception as error:
            print(f'error @ upload: {error}')
    return redirect('dog_detail', dog_id=dog_id)

def add_activity_photo(request, activity_id, dog_id):
    activity_photo = request.FILES.get('activity-photo')
    if activity_photo:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:12] + activity_photo.name[activity_photo.name.rfind('.'):]
        try:
            s3.upload_fileobj(activity_photo, BUCKET, key)
            url = f'{S3_BASE_URL}{BUCKET}/{key}'
            photo = ActivityPhoto(url=url, activity_id=activity_id)
            photo.save()
        except Exception as error:
            print(f'Error occured while uploading')
    return redirect('dog_detail', dog_id=dog_id)

class DogCreate(LoginRequiredMixin, CreateView):
    model = Dog
    fields = ('name', 'breed', 'coatcolor', 'notes', 'ownername', 'ownerphone', 'owneraddress')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DogUpdate(LoginRequiredMixin, UpdateView):
    model = Dog
    fields = '__all__'

class DogDelete(LoginRequiredMixin, DeleteView):
    model = Dog
    success_url = '/dogs/'

class ActivityDelete(LoginRequiredMixin, DeleteView):
    model = Activity
    success_url = '/dogs/'