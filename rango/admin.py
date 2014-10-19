from django.contrib import admin
from rango.models import Category, Page

admin.site.register(Category)


class PageAdmin(admin.ModelAdmin):
    fields = ['title', 'url', 'category', 'views']
    readonly_fields = ['views']

    list_display = fields

admin.site.register(Page, PageAdmin)
