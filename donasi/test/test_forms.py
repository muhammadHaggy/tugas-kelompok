from django.test import SimpleTestCase
from donasi.forms import Pembayaran
from donasi.views import *

class TestForms(SimpleTestCase):
    
    def test_form_pembayaran_valid(self):
        form = Pembayaran(data = {
            'nominal': 100
        })

        self.assertTrue(form.is_valid())


    def test_form_no_data(self):
        form = Pembayaran(data = {})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        