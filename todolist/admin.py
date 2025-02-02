from django.contrib import admin
from . import models


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'email', 'phone']
    list_editable = ['phone']
    list_per_page = 20
    ordering = ['first_name', 'last_name']
    search_fields = ['id__startswith', 'last_name__istartswith', 'first_name__istartswith']
    
    @admin.display(ordering='last_name')
    def customer_name(self, customer):
        return f'{customer.first_name} {customer.last_name}'
    
    
@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'completed', 'created_at', 'customer']
    list_editable = ['completed']
    list_per_page = 20
    ordering = ['title', 'customer', 'completed']
    search_fields = ['title__istartswith', 'customer__first_name__istartswith', 'customer__last_name__istartswith']