from django.urls import path

from todo.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagsListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    is_task_done
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("update/<int:pk>", TaskUpdateView.as_view(), name="task-update"),
    path("delete/<int:pk>", TaskDeleteView.as_view(), name="task-delete"),


    path("tags", TagsListView.as_view(), name="tags-list"),
    path("tags/create/",
         TagCreateView.as_view(),
         name="tag-create"),
    path("tags/<int:pk>/update/",
         TagUpdateView.as_view(),
         name="tag-update"),
    path("tags/<int:pk>/delete/",
         TagDeleteView.as_view(),
         name="tag-delete"),

    path("change-done/<int:pk>", is_task_done, name="task-is-done"),

]
app_name = "to_do"
