from django.shortcuts import render, redirect, reverse
from .models import Pages

def todo_list(request):
    if request.method == 'POST':
        description = request.POST.get('description')

        if description:
            Pages.objects.create(description=description)

    object_list = Pages.objects.filter(is_done=False)
    return render(request, 'todo/todo_list.html', {'object_list': object_list})