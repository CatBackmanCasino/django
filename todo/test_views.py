from django.test import TestCase
from .models import Item


class TestViews(TestCase):
    
    def test_get_todo_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item(self):
        response = self.client.get('/add_item')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        item = Item.objects.create(name='test todo item')
        response = self.client.get('/edit/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')
