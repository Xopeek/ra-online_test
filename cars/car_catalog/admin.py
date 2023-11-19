from django.contrib import admin

from car_catalog.models import Mark, Model


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    pass


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    pass

# Register your models here.
