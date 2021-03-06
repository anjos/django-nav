#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Ter 17 Mar 2009 14:54:20 CET 

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.utils.safestring import mark_safe
from django.conf import settings
from order.admin import OrderedModelAdmin
import django.forms

from models import * 

class TranslateTextInput(django.forms.widgets.TextInput):
  def __init__(self, *args, **kwargs):
    super(TranslateTextInput, self).__init__(*args, **kwargs)

  def render(self, name, value, attrs=None):
    attrs['size'] = attrs.get('size', 50)
    v = super(TranslateTextInput, self).render(name, value, attrs)
    v += u' <a href="#" onclick="translate(\'%s\');" title="%s"><img src="http://www.google.com/options/icons/translate.gif" width="16" height="16"/></a>' % \
        (name, ugettext(u'Suggest a translation using Google!'))
    
    return mark_safe(v)

class ItemTranslationForm(django.forms.ModelForm):
  name = django.forms.CharField(widget=TranslateTextInput)
  description = django.forms.CharField(widget=TranslateTextInput)

  class Meta:
    model = ItemTranslation

  class Media:
    js = ('http://www.google.com/jsapi', 'nav/js/translate.js')

class ItemTranslationAdmin(admin.TabularInline):
  model = ItemTranslation
  formset = django.forms.models.inlineformset_factory(Item, ItemTranslation)
  form = ItemTranslationForm #do not forget that!
  max_num = len(settings.LANGUAGES) - 1 
  extra = len(settings.LANGUAGES) - 1 
  
def translations(item):
  return item.itemtranslation_set.count()
translations.short_description = _(u'Translations')

def img(self):
  if self.has_image():
    return '<img src="%(src)s" height="%(height)d" width="%(width)d"/>' % \
        {
          'src': self.get_image_url(),
          'height': self.image_height,
          'width': self.image_width,
        }
  return u'(None)' 
img.short_description = _(u'Image') 
img.allow_tags = True

class ItemAdmin(OrderedModelAdmin):
  model = Item 
  list_display = ('name', 'url', 'parent', 'description', 'language', 'user', translations, img, 'move_up_down_links')
  fieldsets = (
      (None, 
        {
          'fields': ('name', 'url', 'parent', 'description', 'language', 'sites'),
        }
      ),
      (_(u'Images'),
        { 
          'classes': ('collapse',),
          'fields': ('image_url', 'image', 'image_width', 'image_height',),
        }
      ),
      (_(u'Permissions'), 
        {
          'classes': ('collapse',),
          'fields': ('user', 'groups'), 
        }
      ),
    )
  list_filter = ('language',)
  inlines = [ ItemTranslationAdmin, ]

# make it admin'able
admin.site.register(Item, ItemAdmin)

