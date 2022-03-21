from django.contrib import admin
from blog.models import Blog, CategoryPost
from django.utils.safestring import mark_safe

@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    fields = ['title', 'slug', 'category', 'content', 'image_preview', 'photo', 'datearticle', 'publish',]
    list_display = ['id', 'title', 'category', 'image_preview', 'publish',]
    readonly_fields = ['datearticle', 'image_preview',]
    list_display_links = ['title',]
    list_editable = ['publish',]
    list_filter = ['title', 'publish',]
    prepopulated_fields = {"slug": ("title",)}

    def image_preview(self, obj):
        if obj.photo:
            return mark_safe('<img src="{}" width="100" height="100" style="object-fit:contain" />'.format(obj.photo.url))
        else:
            return 'no photo'
    image_preview.short_description = 'Main photo'


@admin.register(CategoryPost)
class CategoryAdminPost(admin.ModelAdmin):
    list_display = ['id','name_category'] 
    list_display_links = ['name_category',]
    prepopulated_fields = {"slug": ("name_category",)} 