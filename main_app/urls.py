from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dogs/', views.dogs_index, name='dog_index'),
    path('dogs/<int:dog_id>/', views.dogs_detail, name='dog_detail'),
    path('dogs/create/', views.DogCreate.as_view(), name='dog_create'),
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dog_update'),
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dog_delete'),
    path('dogs/<int:dog_id>/add_activity/',views.add_activity, name='add_activity'),
    path('dogs/<int:dog_id>/add_dog_photo/', views.add_dog_photo, name='add_dog_photo'),
    path('accounts/signup/', views.signup, name='signup'),
]
