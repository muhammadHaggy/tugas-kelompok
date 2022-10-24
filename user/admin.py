from django.contrib import admin
from moderation.admin import ModerationAdmin
from donasi.models import Donasi
# Register your models here.

class GalangDanaAdmin(ModerationAdmin):
    list_display = ('penggalang', 'nama', 'target') 
    def has_add_permission(self, request, obj=None) -> bool:
        if (request.user.is_superuser):
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None) -> bool:
        return True
      

admin.site.register(Donasi, GalangDanaAdmin)