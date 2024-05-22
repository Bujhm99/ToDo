from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    template_name = "todo/tasks_list.html"


class TagsListView(generic.ListView):
    model = Tag
    template_name = "todo/tags_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do:tags-list")
    template_name = "todo/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do:tags-list")
    template_name = "todo/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("to_do:tags-list")
    template_name = "todo/tag_confirm_delete.html"

