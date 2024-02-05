from django.contrib import admin
from .models import blog_category,contact_info,SubscribedUser,blog_post,blog_comment
# Register your models here.

admin.site.register(blog_category)
admin.site.register(contact_info)
admin.site.register(SubscribedUser)
admin.site.register(blog_post)
admin.site.register(blog_comment)