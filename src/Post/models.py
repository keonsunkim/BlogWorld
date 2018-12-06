from django.db import models
from django.conf import settings

from django.utils.translation import ugettext_lazy as _
# for translation

User = settings.AUTH_MODEL


class GeneralPost(models.Model):
    author = models.ForeignKey(
        User, related_name='user_posts', on_delete=models.CASCADE)

    title = models.CharField(verbose_name=_('post title'),
                             null=False, blank=False, max_length=50)

    content = models.TextField(verbose_name=_('post content'),
                               blank=False, max_length=30000)

    created = models.DateTimeField(verbose_name=_('post created'),
                                   auto_now_add=True)

    last_edited = models.DateTimeField(verbose_name=_('post edited'),
                                       auto_now=True)

    class Meta:
        verbose_name = _('general post')
        verbose_name_plural = _('general posts')

    def __str__(self):
        return f'{self.pk}:{self.author}:{self.title}:{self.created}'
