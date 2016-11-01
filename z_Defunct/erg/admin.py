from django.contrib import admin
from models import ErgTest, ErgScore

# Register your models here.
class ErgTestAdmin(admin.ModelAdmin):
    list_display = ('test_type', 'date')
admin.site.register(ErgTest, ErgTestAdmin)

class ErgScoreAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
admin.site.register(ErgScore, ErgScoreAdmin)