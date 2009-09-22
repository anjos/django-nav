#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Ter 17 Mar 2009 14:54:20 CET 

from django.contrib import admin
from djanmenus.models import * 

def translations(item):
  return item.itemtranslation_set.count()

class ItemAdmin(admin.ModelAdmin):
  model = Item 
  list_display = ('name', 'url', 'parent', 'description', 'language',
      translations, )
  list_filter = ('language', 'parent', )

# make it admin'able
admin.site.register(Item, ItemAdmin)

class ItemiTranslationAdmin(admin.ModelAdmin):
  model = ItemTranslation
  list_display = ('name', 'description', 'language', )
  list_filter = ('language', ) 

admin.site.register(ItemTranslation, ItemiTranslationAdmin)
