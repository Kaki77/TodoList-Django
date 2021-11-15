from django.contrib import admin
from .models import TodoList
from .models import TodoItem
from .models import TodoListHasTodoItem
from .models import UserHasTodoList
# Register your models here.

admin.site.register(TodoList)
admin.site.register(TodoItem)
admin.site.register(TodoListHasTodoItem)
admin.site.register(UserHasTodoList)