from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as __
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(_("Name"), max_length=64)
    note = models.TextField(_("Note"), blank=True, null=True)

    def __unicode__(self):
        return self.name

class Bill(models.Model):
    date = models.DateTimeField(_("Date"), auto_now=True)
    user = models.ForeignKey(User, verbose_name=_("User"), null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name=_("Category"))
    value = models.FloatField(_("Value"))
    note = models.TextField(_("Note"), blank=True, null=True)

    def __unicode__(self):
        return "%s for %.2f by %s" % (self.category, self.value, self.user)
