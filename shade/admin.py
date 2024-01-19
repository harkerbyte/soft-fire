from django.contrib import admin
from. models import Members

class Admin(admin.ModelAdmin):
    list_display=('firstname','lastname','date_joined')
    prepopulated_fields = {"slug": ("firstname" , "lastname")}
admin.site.register(Members,Admin)