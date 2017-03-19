from django.contrib import admin

from .models import Category,BlogPost

class BlogPostAdmin(admin.ModelAdmin):
		list_display=['id','title','author','publish_date','category','publish','created','updated']
		list_filter=['author','publish','category','updated']
		list_editable=['title']
		search_fields=['title','content']
		list_per_page=1






admin.site.register(Category)
admin.site.register(BlogPost,BlogPostAdmin)