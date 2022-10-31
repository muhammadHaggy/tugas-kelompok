from django.test import TestCase, Client
from django.urls import reverse
from donasi.views import *
from donasi.forms import Pembayaran
from django.contrib.auth.models import User
import json

class TestViews(TestCase):

    def test_show_donasi_GET(self):
        response = Client().get(reverse('donasi:show_donasi'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'donasi.html')

    def test_bayar_donasi_GET(self):
        c = Client()
        user = User.objects.create_user(username='test', password='canwe123')
        c.login(username='test', password='canwe123')

        donasi = Donasi.objects.create(
            penggalang = user,
            target = 0,
        )
        id = donasi.pk

        response = c.get(reverse('donasi:bayar_donasi', args=[id]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bayar_donasi.html')

    # def test_bayar_proses_POST(self):
    #     c = Client()
    #     user = User.objects.create_user(username='test', password='canwe123')
    #     c.login(username='test', password='canwe123')

    #     donasi = Donasi.objects.create(
    #         penggalang = user,
    #         target = 0,
    #         terkumpul = 0
    #     )
    #     id = donasi.pk

    #     url = '/donasi/bayar-proses/' + str(id)

    #     self.assertEquals(donasi.terkumpul, 100)
