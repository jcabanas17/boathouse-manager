from django.contrib import admin
from .models import Rower, Coxwain

# Register your models here.


class CoxwainAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'dob')
admin.site.register(Coxwain, CoxwainAdmin)

class RowerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'dob')
admin.site.register(Rower, RowerAdmin)