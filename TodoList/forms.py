from django.forms import ModelForm
from TodoList.models import TodoList
from TodoList.models import TodoItem
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class TodoListForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super(TodoListForm,self).__init__(*args,**kwargs)
        self.fields['name'].label="Name"
    class Meta:
        model=TodoList
        fields=('name',)

        
class TodoItemForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super(TodoItemForm,self).__init__(*args,**kwargs)
        self.fields['title'].label="Title"
        self.fields['description'].label="Description"
    class Meta:
        model=TodoItem
        fields=('title','description')

class registerForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super(registerForm,self).__init__(*args,**kwargs)
        self.fields['email'].required=True
    class Meta:
        model=User
        fields=('username','password1','password2','email','first_name','last_name')