from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.conf import settings

class Item(models.Model):
  """Describes a menu item in a website page"""

  name = models.CharField(_('Name'), max_length=256, null=False, blank=False,
      help_text=_('The name of the menu item. That is what will be displayed.'))
  description = models.CharField(_('Description'), max_length=1024, null=True, blank=True, help_text=_('This is the description of the menu item. It may be shown when you hover a menu item.'))
  url = models.CharField(_('URL'), max_length=2048, null=True, blank=True, help_text=_('The URL this menu item links to.'))
  parent = models.ForeignKey('self', null=True, blank=True, help_text=_('If you would like that this item comes under another one, select it here. Please note that the appearence of this item will then get conditioned to the appearence parent item as well.'))
  language = models.CharField(_('Language'), max_length=8, null=False, blank=False, help_text=_('Choose the language to which the name applies to.'), choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE)

  class Meta:
    verbose_name = _('menu item')
    verbose_name_plural = _('menu items')

  def depth(self):
    counter = 0
    x = self
    while x.parent:
      counter += 1
      x = x.parent
    return counter

  def __unicode__(self):
    if self.description:
      return ugettext(u'Menu item "%(name)s", %(description)s (depth %(depth)d)' % {'name':self.name, 'description':self.description, 'depth':self.depth()})
    else:
      return ugettext(u'Menu item "%(name)s" (depth %(depth)d)' % {'name':self.name, 'depth':self.depth()})

class ItemTranslation(models.Model):

  item = models.ForeignKey(Item)
  language = models.CharField(_('Language'), max_length=8, null=False, blank=False, help_text=_('Choose the language to which this variant applies to.'), choices=settings.LANGUAGES)
  name = models.CharField(_('Name'), max_length=256, null=False, blank=False,
      help_text=_('The name of the menu item. That is what will be displayed.'))
  description = models.CharField(_('Description'), max_length=1024, null=True, blank=True, help_text=_('This is the description of the menu item. It may be shown when you hover a menu item.'))

  class Meta:
    verbose_name = _('menu item translation')
    verbose_name_plural = _('menu item translations')

  def __unicode__(self):
    return self.item.__unicode__() + u' (' + self.language + u')'

def get_translation(item, variable, language):
  if item.language == language: return getattr(item, variable)
  try:
    return getattr(item.itemtranslation_set.get(language=language), variable)
  except: #no translation for that language available
    return getattr(item, variable)
