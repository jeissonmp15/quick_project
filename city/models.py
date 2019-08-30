from django.db import models
from django.utils.translation import ugettext_lazy as _


class City(models.Model):
    name = models.CharField(_('name'), max_length=50, db_index=True)
    code = models.CharField(_('code'), max_length=50, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('device')
        unique_together = ('name', 'code')
