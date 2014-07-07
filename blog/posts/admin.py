from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.forms import TextInput, Textarea
from blog.posts.models import Entry, Category


class CategoryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':20, 'cols':100})},
    }
    prepopulated_fields = { 'slug': ['title'] }
    list_display = ('title','author','slug','description','pub_date',)
    ordering = ('pub_date', 'author',)
    list_filter = ('author','pub_date')


class EntryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
    }
    prepopulated_fields = { 'slug': ['title'] }
    list_display = ('title','author','meta_description','meta_keywords','status','slug','pub_date',)
    ordering = ('status','pub_date')
    list_filter = ('status','pub_date')


admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)
