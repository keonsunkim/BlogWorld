from django.db import models

from django.utils.translation import ugettext_lazy as _


class FilterTag(models.Model):
    slug = models.SlugField(verbose_name=_('tag slug'),
                            unique=True, max_length=35)
    word = models.CharField(verbose_name=_('tag word'),
                            max_length=35)
    created_at = models.DateTimeField(auto_now_add=False)

    class Meta:
        verbose_name = _('filter tag')
        verbose_name_plural = _('filter tags')


class FilterTagRelation(models.Model):
    filter_tag = models.ForeignKey(
        'Tag.FilterTag', on_delete=models.CASCADE)
    general_post = models.ForeignKey(
        'Post.GeneralPost', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=False)

    class Meta:
        verbose_name = _('filter tag relation')
        verbose_name_plural = _('filter tag relations')
