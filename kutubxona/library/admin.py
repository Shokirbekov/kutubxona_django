from django.contrib import admin
from .models import *

@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display = ("id", "ism", "kurs", "kitoblar_soni", "bitiruvchi")
    list_display_links = ("id", "ism")
    list_editable = ("kurs", "kitoblar_soni", "bitiruvchi")
    list_filter = ("bitiruvchi", "kurs")
    search_fields = ("id", "ism", "kitoblar_soni")
    search_help_text = "ID, ism va kitob soni bo'yicha qidiruv bering"

@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    list_display = ("id", "ism", "tirik", "kitob_soni", "yosh", "jins")
    list_display_links = ("id", "ism")
    list_editable = ("kitob_soni", "tirik")
    list_filter = ("tirik",)
    search_fields = ("id", "ism", "yosh")
    search_help_text = "ID, ism va yoshi bo'yicha qidiruv bering"

@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    autocomplete_fields = ("muallif",)
    list_display = ("id", "nom", "sahifa", "muallif")
    list_display_links = ("id", "nom")
    list_editable = ("sahifa",)
    search_fields = ("id", "nom", "muallif")
    search_help_text = "ID, nom va muallif bo'yicha qidiruv bering"

@admin.register(Admin)
class AdmAdmin(admin.ModelAdmin):
    list_display = ("id", "ism", "ish_vaqti")
    list_display_links = ("id", "ism")
    list_editable = ("ish_vaqti",)
    list_filter = ("ish_vaqti",)
    search_fields = ("id", "ism")
    search_help_text = "ID va ism bo'yicha qidiruv bering"

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    autocomplete_fields = ("talaba", "kitob", "admin")
    list_display = ("id", "talaba", "kitob", "admin", "olingan_sana", "qaytarish_sana", "qaytardi")
    list_display_links = ("id", "talaba")
    list_editable = ("qaytardi",)
    list_filter = ("qaytardi",)
    search_filter = ("id", "talaba", "admin", "kitob")
    search_help_text = "ID, Talaba ismi va Admin ismi bo'yicha qidiruv bering"