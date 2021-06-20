from unittest.mock import patch

from django.test import TestCase, Client
from django.urls import reverse


class IndexTest(TestCase):
    @patch('lost_and_found.objects_posts.models.Post.objects')
    def test_example(self, postss_mock):
        postss_mock.all.return_value = [1]
        client = Client()
        response = client.get(reverse('index'))
        self.assertTemplateUsed('index.html')
        posts = response.context['posts']
