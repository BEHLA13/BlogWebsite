from django.contrib import admin
from .models import Category,Blogs,Comment

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','category_name','created_at','updated_at')


class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','author','blog_image','status','is_featured',
    'created_at','updated_at')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('id','title','category__category_name','status')
    list_editable = ('is_featured',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Blogs,BlogsAdmin)
admin.site.register(Comment)