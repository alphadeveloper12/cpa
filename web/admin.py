from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register the BlogCategory model
@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')
    prepopulated_fields = {'slug': ('name',)}


# Register the BlogPost model
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', 'display_image', 'tags', 'slug')  # Add 'image' to list_display
    list_filter = ('categories', 'created_at', 'author')
    search_fields = ('title', 'content')

    # Function to display the image in the admin
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image.url)
        else:
            return 'No Image'

    display_image.short_description = 'Image'

@admin.register(CPACategory)
class CPACategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(CPALink)
class CPALinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category', 'created_at')
