from django.contrib import admin

from collection.models import Loonatic, Social

class LoonaticAdmin(admin.ModelAdmin):
    model = Loonatic
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Loonatic, LoonaticAdmin)

class SocialAdmin(admin.ModelAdmin):
    model = Social
    list_display = ('network', 'username',)

admin.site.register(Social, SocialAdmin)
