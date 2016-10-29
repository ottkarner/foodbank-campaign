from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator


class Volunteer(models.Model):
    first_name = models.CharField(_('First name'), max_length=100)
    last_name = models.CharField(_('Last name'), max_length=100)
    age = models.PositiveIntegerField(_('Age'))
    phone = models.CharField(_('Phone'), max_length=100)
    email = models.EmailField(_('E-mail'), unique=True)
    is_group = models.BooleanField(_('Is group representative'), default=False)
    group_name = models.CharField(_('Group/organization name'), max_length=100,
            blank=True)
    participant_count = models.PositiveIntegerField(_('Participant count'),
            default=1, validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = _('Volunteer')
        verbose_name_plural = _('Volunteers')

    @property
    def name(self):
        template = u'{first_name} {last_name}'
        if self.is_group:
            template += u' (grupp, {participant_count} osalejat)'
        return template.format(**self.__dict__)

    def __unicode__(self):
        return self.name
