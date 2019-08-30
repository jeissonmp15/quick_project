from django.db import models
from django.utils.translation import ugettext_lazy as _


class Company(models.Model):
    name = models.CharField(_('name'), max_length=50, db_index=True)
    nit = models.CharField(_('nit'), max_length=50, db_index=True, unique=True)
    address = models.CharField(_('address'), max_length=100, db_index=True)
    city = models.ForeignKey(
        'city.City', related_name='company_city_set', verbose_name=_('city'), on_delete=models.CASCADE, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('company')
