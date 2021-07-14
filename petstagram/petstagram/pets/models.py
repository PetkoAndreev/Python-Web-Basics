import os
from os.path import join

from django.conf import settings
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
    # image_url = models.URLField()
    image = models.ImageField(
        upload_to='pets',
    )

    # age = models.IntegerField(
    #     null=True,
    #     blank=True,
    #     validators=[
    #         # is_positive,
    #         models.Min(1),
    #     ]
    # )

    # Will be added after authentication lecture
    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     db_pet = Pet.objects.get(pk=self.id)
    #     # image_path = join(settings.MEDIA_ROOT, db_pet.image.url[len('/media/'):])
    #     image_path = join(settings.MEDIA_ROOT, str(db_pet.image))
    #     os.remove(image_path)
    #     return super().save(force_insert=force_insert, force_update=force_update, using=using,
    #                         update_fields=update_fields)

    # Display as one column with "," separator
    def __str__(self):
        return f'{self.name}, {self.age}, {self.type}'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    # Migrations needed
    # user_id = models.CharField(
    #     null=True,
    #     blank=True,
    # )
