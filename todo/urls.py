from django.urls import path

from todo.views import TaskListView, TagsListView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tags", TagsListView.as_view(), name="tag-list"),

]
app_name = "to_do"