from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskForm
from todo.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    template_name = "todo/tasks_list.html"

class TaskCreateView(generic.CreateView):
    form_class = TaskForm
    success_url = reverse_lazy("to_do:index")
    template_name = "todo/task_form.html"


class TaskUpdateView( generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("to_do:index")
    template_name = "todo/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("to_do:index")
    template_name = "todo/task_confirm_delete.html"


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


def is_task_done(request, pk) -> HttpResponseRedirect:
    task = Task.objects.get(id=pk)
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(
        reverse_lazy("to_do:index",)
    )