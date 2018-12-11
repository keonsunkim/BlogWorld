from django.contrib import admin

from .models import GeneralPost


class GeneralPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'created', 'last_edited')
    # [field.name for field in Book._meta.get_fields()]

admin.site.register(GeneralPost, GeneralPostAdmin)
