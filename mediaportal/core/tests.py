from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch
from django.urls import reverse
from core.models import Page, ContentText


class PageListTestCase(APITestCase):

    def test_user_can_get_page_list(self):
        Page.objects.create(title='p1')
        Page.objects.create(title='p2')
        response = self.client.get(reverse('page-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        r = response.json()
        self.assertEqual('count' in r, True)
        self.assertEqual('previous' in r, True)
        self.assertEqual('next' in r, True)
        self.assertEqual('results' in r, True)
        self.assertEqual(r['results'][0]['url'].startswith('http'), True)

    @patch('core.tasks.increase_counter.delay')
    def test_user_can_get_page_detail(self, cel_task):
        t1 = ContentText.objects.create(title='t1', body='b1', counter=0)
        t2 = ContentText.objects.create(title='t2', body='b2', counter=0)
        p1 = Page.objects.create(title='p1')
        p1.texts.add(t2)
        p1.texts.add(t1)
        response = self.client.get(reverse('page-detail', args=[p1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        r = response.json()
        self.assertEqual(r == {'id': 1, 'title': 'p1', 'texts': [{'title': 't2', 'body': 'b2'}, {'title': 't1', 'body': 'b1'}], 'audios': [], 'videos': []}, True)
        self.assertEqual(cel_task.called, True)
