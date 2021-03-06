import imp
from django.contrib import admin
from .models import Stories, Categories, Chapter, Character, Bookmark, Genre, Language, Rating, Universe, Tag, Type, Author, Editor

from import_export import resources
# Register your models here.


class StoriesResource(resources.ModelResource):

    class Meta:
        model = Stories
class EditorInline(admin.StackedInline):
    model = Editor
    max_num = 3


class AuthorInline(admin.StackedInline):
    model = Author
    max_num = 3

class StoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'cover', 'summary', 'status','released_at', 'created_at', 'updated_at')
    inlines = [
        AuthorInline, EditorInline
    ]
    resource_class = StoriesResource

    # fieldsets = (
    #     (None, {
    #         "fields": ('title', 'slug', 'category','featured_image', 'featured_image_caption', 'content',),
    #     }),
    #     ('Topics and Tags',{
    #         'classes': ('collapse',),
    #         'fields': ('tags', 'topics'),
    #     }),
    #     ('SEO', {
    #         'classes': ('collapse',),
    #         'fields': ('seo_title', 'seo_keywords', 'seo_description',)
    #     }),
    #     ('Publish', {
    #         'classes': ('collapse',),
    #         'fields': ('status', 'published_at', 'deleted_at')
    #     })
    # )
    # prepopulated_fields = {"slug": ("title",)}
    
    # autocomplete_fields = ['tags', 'title']

admin.site.register(Tag)
admin.site.register(Type)
admin.site.register(Categories)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Rating)
admin.site.register(Bookmark)
admin.site.register(Chapter)
admin.site.register(Character)
admin.site.register(Universe)

admin.site.register(Stories, StoriesAdmin)
