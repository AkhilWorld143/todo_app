from django.contrib import admin
from crud.models import *

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_date']

admin.site.register(Task, TaskAdmin)
