from django.shortcuts import render, redirect

from notes.core.profile_utils import get_profile
from notes.note.models import Note
from notes.profiles.forms import CreateProfileForm


def profile_details(request):
    profile = get_profile()
    notes = Note.objects.all()

    context = {
        'profile': profile,
        'notes': notes,
    }

    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()

        context = {
            'form': form,
        }

        return render(request, 'home-no-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        profile.delete()
        Note.objects.all().delete()
        return redirect('home')
    else:

        context = {
        }

    return render(request, 'profile.html', context)
