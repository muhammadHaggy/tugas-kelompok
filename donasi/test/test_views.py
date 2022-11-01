from django.test import TestCase, Client
from django.urls import reverse
from donasi.views import *
from django.contrib.auth.models import User

class TestViews(TestCase):

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(username='test', password='canwe123')
        self.donasi = Donasi.objects.create(
            penggalang = self.user,
            target = 0,
            terkumpul = 0
        )
        self.id = self.donasi.pk


    def test_show_donasi_GET(self):
        response = self.c.get(reverse('donasi:show_donasi'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'donasi.html')


    def test_bayar_donasi_GET(self):
        self.c.login(username='test', password='canwe123')

        response = self.c.get(reverse('donasi:bayar_donasi', args=[self.id]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bayar_donasi.html')


    def test_bayar_proses_POST(self):
        self.c.login(username='test', password='canwe123')
        nominal = 100

        self.c.post(reverse('donasi:bayar_proses', args=[self.id]), {'nominal':[nominal]})
        donasi = Donasi.objects.get(pk = self.id)
        mendonasikan = Mendonasikan.objects.all().last()

        self.assertEquals(donasi.terkumpul, 100)
        self.assertEquals(mendonasikan.donatur, self.user)
        self.assertEquals(mendonasikan.penerima, donasi)
        self.assertEquals(mendonasikan.nominal, nominal)


    def test_get_data_donasi_GET(self):
        response = self.c.get(reverse('donasi:get_data_donasi'))

        donasi = Donasi.objects.filter(is_approved=True)
        data = []
        for item in donasi:
            item.urlFoto = item.foto.url
            data.append({'pk': item.pk, 'fields': {'deskripsi': item.deskripsi, 'is_approved': item.is_approved, 'nama': item.nama, 'penggalang': item.penggalang.username, 'target': item.target, 'tipe': item.tipe, 'urlFoto': item.urlFoto, 'terkumpul': item.terkumpul,}}) 
        data = {'data': data}

        self.assertEquals(response.status_code, 200)
        self.assertJSONEqual(response.content, data)


    def test_get_data_donasi_id_GET(self):
        response = self.c.get(reverse('donasi:get_data_donasi_id', args=[self.id]))

        jumlah = Donasi.objects.get(pk = self.id).terkumpul
        jumlah = {'jumlah': jumlah}

        self.assertEquals(response.status_code, 200)
        self.assertJSONEqual(response.content, jumlah)
