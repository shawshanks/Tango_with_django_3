from django.contrib import admin
from .models import Category, Page, UserProfile


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


class CateAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CateAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)