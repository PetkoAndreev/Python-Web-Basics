from django.shortcuts import render, redirect

from recipes.recipe.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm, ViewRecipeForm
from recipes.recipe.models import Recipe


def home(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }

    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = CreateRecipeForm()

        context = {
            'form': form,
        }

        return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = EditRecipeForm(instance=recipe)

        context = {
            'recipe': recipe,
            'form': form,
        }

        return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'POST':
        recipe.delete()
        return redirect('home')

    else:
        form = DeleteRecipeForm(instance=recipe)

        context = {
            'recipe': recipe,
            'form': form,
        }

        return render(request, 'delete.html', context)


def details_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    form = ViewRecipeForm(instance=recipe)
    if request.method == 'POST':
        return redirect('home')
    else:
        context = {
            'recipe': recipe,
            'form': form,
            'recipe_ingredients': recipe.ingredients.split(", ")
        }

        return render(request, 'details.html', context)
