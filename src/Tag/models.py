from django.db import models

from django.utils.translation import ugettext_lazy as _

from .Post import GeneralPost


class FilterTags(models.Model):
    word = models.CharField(max_length=35)
    slug = models.SlugField(unique=True, max_length=35)
    created_at = models.DateTimeField(auto_now_add=False)
