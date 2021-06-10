from django.shortcuts import render, redirect

from petstagram.pets.models import Pet, Like


def list_pets(request):
    all_pets = Pet.objects.all()
    # all_pets = Pet.objects.filter(type=Pet.TYPE_CHOICE_CAT) # Show only cats

    context = {
        'pets': all_pets
    }

    return render(request, 'pets/pet_list.html', context)


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()

    context = {
        'pet': pet
    }

    return render(request, 'pets/pet_detail.html', context)


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(
        pet=pet
    )
    like.save()
    return redirect('pet_details', pet.id)
