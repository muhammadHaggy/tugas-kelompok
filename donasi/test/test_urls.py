from django.test import SimpleTestCase
from django.urls import reverse, resolve
from donasi.views import *

class TestUrls(SimpleTestCase):
    
    def test_show_donasi(self):
        url = reverse('donasi:show_donasi')
        self.assertEquals(resolve(url).func, show_donasi)


    def test_bayar_donasi(self):
        url = reverse('donasi:bayar_donasi', args=[1])
        self.assertEquals(resolve(url).func, bayar_donasi)
    

    def test_bayar_proses(self):
        url = reverse('donasi:bayar_proses', args=[1])
        self.assertEquals(resolve(url).func, bayar_proses)
    

    def test_get_data_donasi(self):
        url = reverse('donasi:get_data_donasi')
        self.assertEquals(resolve(url).func, get_data_donasi)
    
    
    def test_get_data_donasi_id(self):
        url = reverse('donasi:get_data_donasi_id', args=[1])
        self.assertEquals(resolve(url).func, get_data_donasi_id)