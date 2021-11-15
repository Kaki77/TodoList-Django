from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TodoList(models.Model):
    name=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published',auto_now_add=True)
    update_date=models.DateTimeField('last update date',auto_now=True)
    def __str__(self):
        return self.name

class TodoItem(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=400)
    pub_date=models.DateTimeField('date published',auto_now_add=True)
    update_date=models.DateTimeField('last update date',auto_now=True)
    finished=models.BooleanField(default=False)
    def __str__(self):
        return self.title

class TodoListHasTodoItem(models.Model):
    todolist=models.ForeignKey(TodoList,on_delete=models.CASCADE)
    todoitem=models.ForeignKey(TodoItem,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.todolist} : {self.todoitem}"

class UserHasTodoList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    todolist=models.ForeignKey(TodoList,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user} : {self.todolist}"