from django.contrib import admin

from .models import FilterTag, FilterTagRelation

admin.site.register(FilterTag)
admin.site.register(FilterTagRelation)
