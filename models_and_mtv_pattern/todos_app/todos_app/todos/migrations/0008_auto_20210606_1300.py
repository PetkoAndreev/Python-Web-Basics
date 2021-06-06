# Generated by Django 3.2.4 on 2021-06-06 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0007_alter_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='person_responsible',
        ),
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
