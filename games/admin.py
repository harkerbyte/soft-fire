from django.contrib import admin
from games.models import game

@admin.register(game)


class Admin(admin.ModelAdmin):
    list_display = [ 'title', 'author','supports', 'created', 'tweaked']
    list_filter = ['author','supports', 'created']
    search_fields = ['title', 'author', 'created', 'HTML_file']
    prepopulated_fields = {'title':('url',)}
    date_hierarchy = 'created'
    