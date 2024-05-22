from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, reverse_lazy
from todo.models import Tag, Task


class PrivateManufactureViewTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

        Task.objects.create(
            name="Do smth",
            content="Do smth very fast",
            datetime="2024-05-29 09:25:00",
            deadline="2024-05-29 10:25:00",
            is_done=False
        )


    def test_task_delete_get_succses_redirect(self):
        url = reverse("to_do:task-delete", args=["1"])
        response = self.client.post(path=url)
        self.assertRedirects(response, reverse("to_do:index"))
