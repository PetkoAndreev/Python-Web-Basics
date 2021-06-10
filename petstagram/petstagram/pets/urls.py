from django.urls import path

from petstagram.pets.views import list_pets, pet_details, like_pet

urlpatterns = [
    path('', list_pets, name='list_pets'),
    path('details/<int:pk>', pet_details, name='pet_details'),
    path('like/<int:pk>', like_pet, name='pet_like'),
]
