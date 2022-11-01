from django.test import TestCase, Client
from donasi.models import Donasi, Mendonasikan
from django.contrib.auth.models import User

class TestViews(TestCase):

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(username='test', password='canwe123')
        self.donasi = Donasi.objects.create(
            penggalang = self.user,
            nama = 'test donasi',
            target = 0,
            terkumpul = 0
        )
        self.id = self.donasi.pk
        self.nominal = 100
        self.mendonasikan = Mendonasikan.objects.create(
            donatur = self.user,
            penerima = self.donasi,
            nominal = self.nominal
        )

    
    def test_donasi_creation(self):
        self.assertEquals(self.donasi.penggalang.username, 'test')

    
    def test_mendonasikan_creation(self):
        self.assertEquals(self.mendonasikan.donatur.username, 'test')

    
    def test_donasi_str(self):
        self.assertEquals(str(self.donasi), 'test donasi')

    
    def test_mendonasikan_str(self):
        self.assertEquals(str(self.mendonasikan), 'test')
