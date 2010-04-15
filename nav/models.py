import os, datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from django.template import Template, Context
from order.models import OrderedModel

def upload_path(object, original):
  """Tells the FileField how to choose a name for this file."""
  size = '%dx%d' % (object.image.width, object.image.height)
  return os.path.join('menus', datetime.date.today().strftime('%Y/%m'), 
      size, original)

class Item(OrderedModel):
  """Describes a menu item in a website page"""
  
  login_choices = (
      ('X', _(u'Any user')),
      ('L', _(u'Authenticated')),
      ('N', _(u'Anonymous')),
      ('A', _(u'Administrator')),
      ('S', _(u'Staff')),
      ('G', _(u'Belonging to a group')),
      )

  name = models.CharField(_('Name'), max_length=256, null=False, blank=False,
      help_text=_('The name of the menu item. That is what will be displayed.'))

  description = models.CharField(_('Description'), max_length=1024, null=True, blank=True, help_text=_('This is the description of the menu item. It may be shown when you hover a menu item.'))

  url = models.CharField(_('URL'), max_length=2048, null=True, blank=True, help_text=_('The URL this menu item links to.'))

  parent = models.ForeignKey('self', null=True, blank=True, help_text=_('If you would like that this item comes under another one, select it here. Please note that the appearence of this item will then get conditioned to the appearence parent item as well.'))

  language = models.CharField(_('Language'), max_length=8, null=False, blank=False, help_text=_('Choose the language to which the name applies to.'), choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE)

  image = models.ImageField(_('Image'), upload_to=upload_path, null=True, blank=True, help_text=_('If you would like this menu item to be represented by an image, upload it here.'), height_field='image_height', width_field='image_width')

  image_url = models.URLField(_('Image URL'), null=True, blank=True, help_text=_(u'If you set this option to an URL, it will be used <b>instead</b> of the image field. Please note you should also set the width and height of the image.'))

  image_width = models.PositiveIntegerField(_('Width'), null=True, blank=True, help_text=_(u'The width of the image to display. This setting overrides values provided by the image itself.'))
  
  image_height = models.PositiveIntegerField(_('Height'), null=True, blank=True, help_text=_(u'The height of the image to display. This setting overrides values provided by the image itself.'))

  user = models.CharField(_('User type'), default='X', max_length=1, choices=login_choices, help_text=_('Set this to determine if the item will be showed only to a subgroup of users.'))

  groups = models.ManyToManyField(Group, null=True, blank=True,
      help_text=_('If you have set "For users in a group" as the user type choice, select here the groups of users which will see this menu item. Otherwise, this parameter is ignored.'))

  sites = models.ManyToManyField(Site, null=True, blank=True,
      help_text=_('Select here the sites to which this item is effective.'))

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

  def get_url(self, context):
    """Returns the URL of this link, completely resolved.""" 
    return Template(self.url).render(context)

  def get_name(self, language):
    """Returns the name for this menu item, in the desired language. Defaults
    to the main textual representation."""
    try: return self.itemtranslation_set.get(language=language).name
    except: return self.name

  def get_description(self, language):
    try: return self.itemtranslation_set.get(language=language).description
    except: return self.description

  def is_allowed(self, user):
    """Tells if the given user/site is allowed to see this menu item."""
    if Site.objects.get_current() not in self.sites.all(): return False

    if self.user == 'X': return True
    elif self.user == 'L' and user.is_authenticated(): return True
    elif self.user == 'N' and not user.is_authenticated(): return True
    elif self.user == 'A' and user.is_superuser: return True
    elif self.user == 'S' and user.is_staff: return True
    elif self.user == 'G' and self.groups.all() and \
      [k for k in self.groups.all() if k in user.groups.all()]: return True

    # if you missed all other entries, you cannot see this one...
    return False

  def has_image(self):
    """Says if we have an image to display or not."""
    return bool(self.image_url or self.image)

  def get_image_url(self):
    """Returns the image URL, if there is one."""
    if self.image_url: return self.image_url
    elif self.image: return self.image.url
    return None

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

