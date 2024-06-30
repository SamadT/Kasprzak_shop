from django.contrib import admin
from .models import Products, Buscket, Comments
# Register your models here.
"""
admin
admin@example.com
1234
"""

class Product_dict(admin.ModelAdmin):
    fieldsets = [
        ("Product_info", {"fields": ["tech"]})
    ]
admin.site.register(Products, Product_dict)


# class Buscket_list(admin.ModelAdmin):
#     fieldsets = [
#         ("Product_info", {"fields": ["tech"]})
#     ]
# admin.site.register(Buscket_list)

class Comments_list(admin.ModelAdmin):
    fieldsets = [
        ("Comment_info", {"fields": ["user_name", "comment", "pub_date"]})
    ]
    list_display = ["user_name", "comment", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["comment"]
admin.site.register(Comments, Comments_list)