from django.shortcuts import render
from django.views import generic

from todo.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    template_name = "todo/tasks_list.html"


class TagsListView(generic.ListView):
    model = Tag
    paginate_by = 12

