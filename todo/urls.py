from django.urls import path

from todo.views import (
    TaskListView,
    TagsListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),


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

]
app_name = "to_do"