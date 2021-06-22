from django.urls import path

from petstagram.pets.views import list_pets, pet_details, like_pet, create_pet, edit_pet, delete_pet, comment_pet, \
    ListPetsView

urlpatterns = [
    path('', list_pets, name='list_pets'),
    # path('', ListPetsView.as_view(), name='list_pets'), # Class Base View
    path('details/<int:pk>', pet_details, name='pet_details'),
    path('like/<int:pk>', like_pet, name='pet_like'),
    path('create/', create_pet, name='create_pet'),
    path('edit/<int:pk>', edit_pet, name='edit_pet'),
    path('delete/<int:pk>', delete_pet, name='delete_pet'),
    path('comment/<int:pk>', comment_pet, name='comment_pet'),
]
