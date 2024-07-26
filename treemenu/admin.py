from django.contrib import admin

from treemenu.models import Menu


@admin.register(Menu)
class AdminMenu(admin.ModelAdmin):
    list_display = ('name', 'slug', 'named_url', 'parent')
    list_filter = ('name', 'id', 'parent')
    search_fields = ('name', 'slug', 'named_url')
    ordering = ('name',)
