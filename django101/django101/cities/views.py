from django.http import HttpResponse
from django.shortcuts import render

from django101.cities.models import Person


def index(req):
    context = {
        'name': 'Petko',
        'people': Person.objects.all()
    }
    return render(req, 'index.html', context)


def list_phones(req):
    # return HttpResponse('Phones list')
    context = {
        'phones': [
            {
                'name': 'Huawei Mate 20 pro',
                'quantity': 10
            },
            {
                'name': 'Samsung Galaxy S10',
                'quantity': 5
            },
            {
                'name': 'Xiaomi RedMi 10',
                'quantity': 0
            },
        ]
    }

    context['message'] = 'Phones list'
    return render(req, 'phones.html', context)
