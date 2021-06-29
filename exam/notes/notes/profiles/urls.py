from django.urls import path

from notes.profiles.views import profile_details, create_profile, delete_profile

urlpatterns = (
    path('', profile_details, name='profile details'),
    path('create/', create_profile, name='create profile'),
    path('delete/', delete_profile, name='delete profile'),
)
