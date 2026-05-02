from django.contrib import admin

from .models import Category, Size, Product, productSize, productImage

class productSizeInline(admin.TabularInline):
    model = productSize
    extra = 1

class productImageInline(admin.TabularInline):
    model = productImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'color', 'price']
    list_filter = ['category', 'color']
    search_fields = ['name', 'color', 'description']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [productSizeInline, productImageInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Product, ProductAdmin)