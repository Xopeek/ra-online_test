from django.urls import path

from car_catalog.views import index, update_autoru_cars

urlpatterns = [
    path('', index, name='index'),
    path(
        'update_autoru_catalog/',
        update_autoru_cars,
        name='update_autoru_catalog'
    ),
]
