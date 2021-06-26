from recipes.recipe.models import Recipe


def get_recipe():
    recipe = Recipe.objects.all()
    if recipe:
        pass

    return recipe
