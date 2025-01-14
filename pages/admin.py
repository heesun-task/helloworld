from django.contrib import admin
from .models import ToDoList
from .models import Item

admin.site.register(ToDoList)
admin.site.register(Item)
