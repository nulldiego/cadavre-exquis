from django.contrib import admin

# Register your models here.
from .models import Cadavre, CadavrePart

# admin.site.register(Cadavre)
# admin.site.register(CadavrePart)

# Define the admin class
@admin.register(CadavrePart)
class CadavrePartAdmin(admin.ModelAdmin):
    list_display = ('cadavre', 'display_content', 'author')
    list_filter = ('cadavre', 'author')

class CadavrePartInline(admin.TabularInline):
    model = CadavrePart

@admin.register(Cadavre)
class CadavreAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'display_cadavre')
    inlines = [CadavrePartInline]