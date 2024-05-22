from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from todo.models import Tag


class TagViewTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

        Tag.objects.create(
            name="pushong",
        )

    def test_tag_create_get_succses_redirect(self):
        url = reverse("to_do:tag-create")
        response = self.client.post(path=url, data={
            "name": "Sport",
        })
        self.assertRedirects(response, reverse("to_do:tags-list"))

    def test_tag_update_get_succses_redirect(self):
        url = reverse("to_do:tag-update", args=["1"])
        response = self.client.post(path=url, data={
            "name": "pushong2",
        })
        self.assertRedirects(response, reverse("to_do:tags-list"))

    def test_tag_delete_get_succses_redirect(self):
        url = reverse("to_do:tag-delete", args=["1"])
        response = self.client.post(path=url)
        self.assertRedirects(response, reverse("to_do:tags-list"))
