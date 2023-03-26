from django.contrib import admin
from .models import Category, Menu


@admin.register(Category)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    prepopulated_fields = {'slug': ("name",)}
    list_filter = ('menu',)
    fieldsets = (
        ('Добавьте новое меню:', {
            'fields': (('menu', 'parent'), 'name', 'slug')
            }),
            )


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ("name",)}