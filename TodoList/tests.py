from datetime import time
from django.test import TestCase
from .models import TodoList
from .models import TodoItem
from .models import TodoListHasTodoItem
from django.utils import timezone
# Create your tests here.

class TodoListTest(TestCase):
    def test_add_todolist(self):
        time=timezone.now()
        todolist=TodoList.objects.create(author='Me',pub_date=time,update_date=time)
        self.assertEqual(todolist.author,'Me')
        self.assertEqual(todolist.pub_date,time)
        self.assertEqual(todolist.update_date,time)

class TodoItemTest(TestCase):
    def test_add_todoitem(self):
        todoitem=TodoItem.objects.create(title='todoitem',description='description')
        self.assertEqual(todoitem.title,'todoitem')
        self.assertEqual(todoitem.description,'description')

class TodoListHasTodoItemTest(TestCase):
    def test_add(self):
        todolist=TodoList.objects.create(author='Me',pub_date=timezone.now(),update_date=timezone.now())
        todoitem=TodoItem.objects.create(title='todoitem',description='description')
        add=TodoListHasTodoItem.objects.create(todolist_id=todolist.id,todoitem_id=todoitem.id)
        self.assertEqual(add.todolist_id,todolist.id)
        self.assertEqual(add.todoitem_id,todoitem.id)