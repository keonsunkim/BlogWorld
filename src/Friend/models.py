from django.db import models
from django.conf import settings

from django.utils.translation import ugettext_lazy as _

User = settings.AUTH_USER_MODEL


class FollowRelationShip(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following')
    followee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower')
    created = models.DateTimeField(verbose_name=_('follow created'),
                                   auto_now_add=False)

    class Meta:
        verbose_name = _('follow relationship')
        verbose_name_plural = _('follow relationships')
        unique_together = ('follower', 'followee')

    def __str__(self):
        return f'{self.follower} follows {self.followee}'
