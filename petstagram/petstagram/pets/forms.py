from django import forms

from petstagram.core.forms import BootstrapFormMixin
from petstagram.pets.models import Pet


class PetForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'some-class'
                }
            ),
            'age': forms.TextInput(
                attrs={
                    'type': 'range',
                }
            )
        }


class EditPetForm(PetForm):
    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'readonly': 'readonly'
                }
            )
        }
