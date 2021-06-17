from django.shortcuts import render, redirect

from todos_app.todos.forms import CreateTodoForm, UpdateTodoForm, TodoForm
from todos_app.todos.models import Todo


# from todos_app.todos.models.todo import Person


# def index(request):
#     context = {
#         'todos': Todo.objects.all(),
#         'form': CreateTodoForm(),
#     }
#
#     return render(request, 'index.html', context)
#
#
# def create_todo(request):
#     # text = request.POST['text']
#     # description = request.POST['description']
#     # owner_name = request.POST['owner']
#     # owner = Person.objects.filter(name=owner_name).first()
#     # if not owner:
#     #     owner = Person(name=owner_name)
#     #     owner.save()
#
#     # todo = Todo(
#     #     text=text,
#     #     description=description,
#     #     # owner=owner,
#     # )
#     # todo.save()
#     form = CreateTodoForm(request.POST)
#
#     if form.is_valid():
#         # cleaned data is available ONLY after is_valid()!!!
#         text = form.cleaned_data['text']
#         description = form.cleaned_data['description']
#         todo = Todo(
#             text=text,
#             description=description,
#             # owner=owner,
#         )
#         todo.save()
#
#     # print(Person.objects.raw("select * from todos_person"))
#
#         return redirect('/')
#
#     context = {
#         'todos': Todo.objects.all(),
#         'form': form,
#     }
#
#     return render(request, 'index.html', context)
#
#
# def change_todo_state(request, pk):
#     todo = Todo.objects.get(pk=pk)
#     todo.state = not todo.state
#     todo.save()
#     return redirect('/')

# Forms Lab
def index(request):
    context = {
        'todos': Todo.objects.all()
    }
    return render(request, 'todo_app/index.html', context)


def create_todo(request):
    form = TodoForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            # todo = Todo(
            #     title=form.cleaned_data['title'],
            #     description=form.cleaned_data['description'],
            #     state=False,
            # )
            # todo.save()
            # Forms
            form.save()  # Model forms
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'todo_app/create.html', context)


def show_form(request, form):
    context = {
        'form': form
    }

    return render(request, 'todo_app/edit.html', context)


def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    # form = UpdateTodoForm(request.POST, initial=todo)
    # Model form
    # form = TodoForm(
    #     request.POST,
    #     instance=todo,
    #     initial=todo.__dict__,
    # )

    if request.method == 'GET':
        return show_form(request, TodoForm(initial=todo.__dict__))

    else:
        form = TodoForm(
            request.POST,
            instance=todo,
            initial=todo.__dict__,
        )
        if form.is_valid():
            # todo.title = form.cleaned_data['title']
            # todo.description = form.cleaned_data['description']
            # todo.state = form.cleaned_data['state']
            # todo.save()
            form.save()  # Model form
            return redirect('index')
        return show_form(request, form)
        # return render(request, 'todo_app/edit.html', context)
