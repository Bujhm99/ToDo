from django.db import models



class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> models.CharField:
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255, unique=False)
    content = models.TextField(unique=False)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True, unique=False)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self) -> models.CharField:
        return f"Task: {self.name} is done: {self.is_done}"

    class Meta:
        ordering = ("is_done", "-datetime",)
