from django.test import TestCase
from django.urls import reverse, resolve
from notif.models import Item

class ModelTest(TestCase):

    def testNotifModel(self):
        self.item = Item.objects.create(
            title = "We Can",
            description = "Test Notifikasi Penggalangan Dana"
        )

        assert self.item.title == "We Can"
        assert self.item.description == "Test Notifikasi Penggalangan Dana"