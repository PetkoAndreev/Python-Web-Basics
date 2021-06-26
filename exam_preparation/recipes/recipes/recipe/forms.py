from django import forms

from recipes.recipe.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class CreateRecipeForm(RecipeForm):
    pass


class EditRecipeForm(RecipeForm):
    pass


class DeleteRecipeForm(RecipeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'


class ViewRecipeForm(RecipeForm):
    pass
