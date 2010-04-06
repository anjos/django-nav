from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.conf import settings
from django.contrib.auth.models import Group
from django.template import Template, Context

class Item(models.Model):
  """Describes a menu item in a website page"""

  name = models.CharField(_('Name'), max_length=256, null=False, blank=False,
      help_text=_('The name of the menu item. That is what will be displayed.'))
  description = models.CharField(_('Description'), max_length=1024, null=True, blank=True, help_text=_('This is the description of the menu item. It may be shown when you hover a menu item.'))
  url = models.CharField(_('URL'), max_length=2048, null=True, blank=True, help_text=_('The URL this menu item links to.'))
  parent = models.ForeignKey('self', null=True, blank=True, help_text=_('If you would like that this item comes under another one, select it here. Please note that the appearence of this item will then get conditioned to the appearence parent item as well.'))
  language = models.CharField(_('Language'), max_length=8, null=False, blank=False, help_text=_('Choose the language to which the name applies to.'), choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE)
  image = models.ImageField(_('Image'), upload_to='menus/%Y/%m',
      null=True, blank=True,
      help_text=_('If you would like this menu item to be represented by an image, upload it here.'),
      )
  staff = models.BooleanField(_('Staff only'), default=False,
      help_text=_('If you set this button, the item will be available only to users that have staff permission'))
  superuser = models.BooleanField(_('Superuser only'), default=False,
      help_text=_('If you set this button, the item will be available only to superusers (site administrators).'))
  groups = models.ManyToManyField(Group, 
      help_text=_('If you set this option, only users belonging to these groups will see this menu item.'))

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

  def get_url(self):
    """Returns the URL of this link, completely resolved.""" 
    return Template(self.url).render(Context())

  def get_name(self, language):
    """Returns the name for this menu item, in the desired language. Defaults
    to the main textual representation."""
    try: return item.itemtranslation_set.get(language=language).name
    except: return self.name

  def get_description(self, language):
    try: return item.itemtranslation_set.get(language=language).description
    except: return self.description

  def is_allowed(self, user):
    """Tells if the given user is allowed to see this menu item."""
    if not (self.superuser or self.staff or self.groups): return True

    # if any was set, we have to go through the permissions. note that all
    # conditions must apply. we do a logical AND.
    if self.superuser and not user.is_superuser: return False
    if self.staff and not user.is_staff: return False
    if self.groups and not [k for k in self.groups if k in user.groups]: 
      return False

    # if you survived until this point, it is because one of the above
    # conditions was true.
    return True

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

