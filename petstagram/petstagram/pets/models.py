from django.core.exceptions import ValidationError
from django.db import models


# Custom validator - more complex variant
# def is_positive(value):
#     if value <= 0:
#         raise ValidationError


class Pet(models.Model):
    TYPE_CHOICE_DOG = 'dog'
    TYPE_CHOICE_CAT = 'cat'
    TYPE_CHOICE_PARROT = 'parrot'

    TYPE_CHOICES = (
        (TYPE_CHOICE_DOG, 'Dog'),
        (TYPE_CHOICE_CAT, 'Cat'),
        (TYPE_CHOICE_PARROT, 'Parrot'),
    )
    type = models.CharField(
        max_length=6,
        choices=TYPE_CHOICES,
    )
    name = models.CharField(
        max_length=6,
    )
    age = models.PositiveIntegerField()
    description = models.TextField()
    image_url = models.URLField()

    # age = models.IntegerField(
    #     null=True,
    #     blank=True,
    #     validators=[
    #         # is_positive,
    #         models.Min(1),
    #     ]
    # )

    # Display as one column with "," separator
    # def __str__(self):
    #     return f'{self.name}, {self.age}, {self.type}'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    # Migrations needed
    # user_id = models.CharField(
    #     null=True,
    #     blank=True,
    # )
