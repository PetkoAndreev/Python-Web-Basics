# Generated by Django 3.2.4 on 2021-06-26 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
