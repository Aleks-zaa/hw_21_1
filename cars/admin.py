from django.contrib import admin
from cars.models import Product, Category, Blog


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    

@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")
    search_fields = ("title",)
