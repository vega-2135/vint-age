from django.contrib import admin

from .models import Category, Product, Review, Wishlist

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
        "category",
        "price",
        "rating",
        "image",
    )

    ordering = ("sku",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Displays fields and values
    for Review model in admin panel.
    """
    list_display = ('author', 'content', 'product', 'created_on')
    search_fields = ['author', 'created_on']
    list_filter = ['created_on']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Wishlist)
