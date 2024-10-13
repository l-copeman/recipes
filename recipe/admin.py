from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """Admin User"""
    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'method',)


admin.site.register(Comment)
