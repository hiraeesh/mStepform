from django.contrib import admin
from .models import FormData

@admin.register(FormData)
class FormDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'age', 'occupation')
    search_fields = ('name', 'email', 'phone', 'address', 'occupation')
