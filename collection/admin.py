from django.contrib import admin

from collection.models import Loonatic

class LoonaticAdmin(admin.ModelAdmin):
    model = Loonatic
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Loonatic, LoonaticAdmin)
