from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe


from . import models


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'telegram_username', 'create_at', 'id']


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    save_as = True

    save_on_top = True
    list_display = ('id', 'title', 'slug', 'created_at', 'get_image')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('tags',)
    readonly_fields = ('created_at', 'get_image')
    fields = ('title', 'slug', 'tags', 'author', 'content', 'image',
              'get_image', 'created_at')

    def get_image(self, obj):
        """Возвращает картинку новости в админке"""
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75"')
        else:
            return '-'

    get_image.short_description = 'Фото'
