#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Ter 17 Mar 2009 14:54:20 CET 

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from models import * 

class ItemTranslationAdmin(admin.TabularInline):
  model = ItemTranslation
  max_num = len(settings.LANGUAGES) - 1 
  extra = len(settings.LANGUAGES) - 1 

def translations(item):
  return item.itemtranslation_set.count()

class ItemAdmin(admin.ModelAdmin):
  model = Item 
  list_display = ('name', 'url', 'parent', 'description', 'language', 'priority', 'user', translations, )
  fieldsets = (
      (None, 
        {
          'fields': ('name', 'url', 'parent', 'description', 'language', 'priority'),
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
  list_filter = ('language', 'priority',)
  ordering = ('priority', 'name')
  inlines = [ ItemTranslationAdmin, ]

# make it admin'able
admin.site.register(Item, ItemAdmin)

