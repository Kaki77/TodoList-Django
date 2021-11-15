from django.urls import path
from . import views

app_name = 'TodoList'
urlpatterns = [
    path('',views.index,name="index"),
    path('createTodoList/', views.createTodoList, name='createTodoList'),
    path('<int:pk_list>/updateTodoList/', views.updateTodoList, name='updateTodoList'),
    path('<int:pk_list>/', views.readTodoList, name='readTodoList'),
    path('<int:pk_list>/deleteTodoList/', views.deleteTodoList, name='deleteTodoList'),
    path('<int:pk_list>/addTodoItem/', views.addTodoItem, name='addTodoItem'),
    path('<int:pk_list>/item/<int:pk_item>/updateTodoItem/', views.updateTodoItem, name='updateTodoItem'),
    path('<int:pk_list>/item/<int:pk_item>/deleteTodoItem/', views.deleteTodoItem, name='deleteTodoItem'),
    path('<int:pk_list>/item/<int:pk_item>/toggleFinished/', views.toggleFinished, name='toggleFinished'),
]