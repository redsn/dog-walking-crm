from django.shortcuts import render, redirect
from .models import Dog, Activity
from .forms import ActivityForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    pass

def dogs_index(request):
    pass

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

