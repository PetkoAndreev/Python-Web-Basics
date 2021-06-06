# Generated by Django 3.2.4 on 2021-06-05 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0004_auto_20210605_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='categories',
            field=models.ManyToManyField(to='todos.Category'),
        ),
    ]
