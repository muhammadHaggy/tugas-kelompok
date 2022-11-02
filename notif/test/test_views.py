from django.test import TestCase, Client
from django.urls import reverse
from notif.views import *
from notif.models import Item
from django.contrib.auth.models import User

def test_bayar_donasi_GET(self):
    self.client = Client()
    self.client.login(username='test', password='canwe123')

    response = self.c.get(reverse('donasi:bayar_donasi', args=[self.id]))

    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'notif.html')