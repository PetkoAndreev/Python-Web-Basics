# Generated by Django 3.2.4 on 2021-06-06 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0006_auto_20210606_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Home', 'Home Stuff'), ('Work', 'Work Stuff')], max_length=20),
        ),
    ]
