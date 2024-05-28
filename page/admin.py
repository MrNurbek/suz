from django.contrib import admin
from page.models import *


class LogatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text')


# Register your models here.


admin.site.register(User)
admin.site.register(Logat, LogatAdmin)
