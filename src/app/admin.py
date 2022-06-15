from django.contrib import admin

from app.models import Orang

@admin.register(Orang)
class OrangAdmin(admin.ModelAdmin):
    list_display = ['parent', 'nama', 'jenis_kelamin']