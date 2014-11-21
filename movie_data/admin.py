__author__ = 'narota'
from django.contrib import admin
from movie_data.models import Genere


def get_generes(GenereAdmin, request, queryset):
    print "Custom Action"
get_generes.short_description = "Load data from 'movies.dat'"

class GenereAdmin(admin.ModelAdmin):
    list_display = ('pk', 'genere',)
    list_filter  = ('genere',)
    actions      = [get_generes]


admin.site.register(Genere, GenereAdmin)
