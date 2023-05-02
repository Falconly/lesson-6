from django.contrib import admin
from .models import *


# Register your models here.

class WorkersAdmin(admin.ModelAdmin):
    list_display = ('id', 'fio', 'position', 'telephone')
    search_fields = ('fio',)
    ordering = ('id',)


admin.site.register(Worker, WorkersAdmin)
