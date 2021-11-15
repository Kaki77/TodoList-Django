from django.shortcuts import redirect,render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from TodoList.models import TodoList,TodoItem,TodoListHasTodoItem,UserHasTodoList
from django.contrib import messages
from .forms import TodoListForm,TodoItemForm,registerForm
from django.contrib.auth.decorators import login_required
# Create your views here.

################################################################################################


@login_required
def index(request):
    lists=UserHasTodoList.objects.filter(user=request.user)
    return render(request,'TodoList/index.html',{'lists':lists})


def register(request):
    if not(request.user.is_authenticated):
        form=registerForm()
        if(request.method=='POST'):
            form=registerForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Inscription réussi")
                return HttpResponseRedirect(reverse('login'))
        else:  
            return render(request,'registration/register.html',{'form':form})
    else:
        return HttpResponseRedirect(reverse('TodoList:index'))

################################################################################################


@login_required
def createTodoList(request):
    form=TodoListForm()
    if(request.method=='POST'):
        form=TodoListForm(request.POST)
        if form.is_valid():
            list=form.save()
            UserHasTodoList.objects.create(user=request.user,todolist=list)
            messages.success(request,"Ajout effectué")
            return HttpResponseRedirect(reverse('TodoList:index'))
    else:  
        return render(request,'TodoList/addTodoList.html',{'form':form})


@login_required
def updateTodoList(request,pk_list):
    if UserHasTodoList.objects.filter(user=request.user,todolist=pk_list):
        list=TodoList.objects.get(pk=pk_list)
        if(request.method=='POST'):
            form=TodoListForm(request.POST,instance=list)
            if form.is_valid():
                new_list=form.save()
                UserHasTodoList.objects.filter(user=request.user,todolist=list).update(todolist=new_list)
                messages.success(request,"Update effectué")
                return HttpResponseRedirect(reverse('TodoList:index'))
        else:  
            form=TodoListForm(instance=list)
            return render(request,'TodoList/updateTodoList.html',{'form':form,'pk_list':pk_list})   
    else:
        messages.error(request,'Access Denied')
        return HttpResponseRedirect(reverse('TodoList:index'))


@login_required
def readTodoList(request,pk_list):
    if UserHasTodoList.objects.filter(user=request.user,todolist=pk_list):
        list=TodoListHasTodoItem.objects.filter(todolist=pk_list)
        return render(request,'TodoList/readTodoList.html',{'list':list,'pk_list':pk_list})
    else:
        messages.error(request,'Access Denied')
        return HttpResponseRedirect(reverse('TodoList:index'))

@login_required
def deleteTodoList(request,pk_list):
    if UserHasTodoList.objects.filter(user=request.user,todolist=pk_list):
        list=TodoList.objects.get(pk=pk_list)
        list.delete()
        messages.success(request,'Supression effectué')
        return redirect('TodoList:index')
    else:
        messages.error(request,'Access Denied')
        return HttpResponseRedirect(reverse('TodoList:index'))


################################################################################################


@login_required
def addTodoItem(request,pk_list):
    if UserHasTodoList.objects.filter(user=request.user,todolist=pk_list):
        form=TodoItemForm()
        if(request.method=='POST'):
            form=TodoItemForm(request.POST)
            if form.is_valid():
                item=form.save()
                list=TodoList.objects.get(pk=pk_list)
                linktab=TodoListHasTodoItem.objects.create(todolist=list,todoitem=item)
                linktab.save()
                messages.success(request,"Ajout effectué")
                return HttpResponseRedirect(reverse('TodoList:readTodoList',kwargs={'pk_list':pk_list}))
        else:  
            return render(request,'TodoList/addTodoItem.html',{'form':form,'pk_list':pk_list})
    else:
        messages.error(request,'Access Denied')
        return HttpResponseRedirect(reverse('TodoList:index'))


@login_required
def updateTodoItem(request,pk_list,pk_item):
    if UserHasTodoList.objects.filter(user=request.user,todolist=pk_list):
        item=TodoItem.objects.get(pk=pk_item)
        if(request.method=='POST'):
            form=TodoItemForm(request.POST,instance=item)
            if form.is_valid():
                list=TodoList.objects.get(pk=pk_list)
                new_item=form.save()
                TodoListHasTodoItem.objects.filter(todolist=list,todoitem=item).update(todoitem=new_item)
                messages.success(request,"Update effectué")
                return HttpResponseRedirect(reverse('TodoList:readTodoList',kwargs={'pk_list':pk_list}))
        else:  
            form=TodoItemForm(instance=item)
            return render(request,'TodoList/updateTodoItem.html',{'form':form,'pk_list':pk_list,'pk_item':pk_item})
    else:
        messages.error(request,'Access Denied')
        return HttpResponseRedirect(reverse('TodoList:index'))


@login_required
def deleteTodoItem(request,pk_list,pk_item):
    if UserHasTodoList.objects.filter(user=request.user,todolist=pk_list):
        item=TodoItem.objects.get(pk=pk_item)
        item.delete()
        messages.success(request,"Supression effectué")
        return redirect('TodoList:readTodoList',pk_list=pk_list)
    else:
        messages.error(request,'Access Denied')
        return HttpResponseRedirect(reverse('TodoList:index'))


@login_required
def toggleFinished(request,pk_list,pk_item):
    if UserHasTodoList.objects.filter(user=request.user,todolist=pk_list):
        item=TodoItem.objects.get(pk=pk_item)
        item.finished=not(item.finished)
        item.save()
        return HttpResponseRedirect(reverse('TodoList:readTodoList',kwargs={'pk_list':pk_list}))
    else:
        messages.error(request,'Access Denied')
        return HttpResponseRedirect(reverse('TodoList:index'))
