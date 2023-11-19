import xml.etree.ElementTree

import requests
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from car_catalog.forms import MarkForm
from car_catalog.models import Mark, Model


@csrf_exempt
def update_autoru_cars(request):

    Mark.objects.all().delete()
    Model.objects.all().delete()

    url = 'https://auto-export.s3.yandex.net/auto/price-list/catalog/cars.xml'
    response = requests.get(url)

    if response.status_code == 200:
        root = xml.etree.ElementTree.fromstring(response.content)

        for mark_element in root.iter('mark'):
            mark_name = mark_element.get('name')
            mark, created = Mark.objects.get_or_create(name=mark_name)

            for folder_element in mark_element.iter('folder'):
                model_name = folder_element.get('name').split(',')[0].strip()
                Model.objects.get_or_create(name=model_name, mark=mark)

        return redirect('index')

    return JsonResponse(
        {'status': 'error', 'message': 'Failed'}
    )


def index(request):
    marks = Mark.objects.all().order_by('name')
    models = []

    if request.method == 'POST':
        mark_name = request.POST.get('name', None)
        if mark_name:
            mark = Mark.objects.get(name=mark_name)
            models = Model.objects.filter(mark=mark).order_by('name')

    form = MarkForm()
    context = {
        'form': form,
        'models': models,
        'marks': marks
    }
    return render(request, 'index.html', context)
