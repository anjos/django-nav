#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Seg 21 Set 2009 14:44:04 CEST 

"""
"""

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

from nav.models import *

names = ['First', 'Second', 'Third', 'Fourth']
urls = ['{% url rosetta-home %}', '{% url root %}', '{% url admin "" %}', '/']
trans_pt = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto']
trans_fr = ['Première', 'Deuxième', 'Troisième', 'Quatrième']

for a in names:
  i = names.index(a)
  x = Item(name=a, description='%s menu item' % a, url=urls[i], parent = None,
    language='en')
  x.save()
  t = ItemTranslation(item=x, language='pt-br', name=trans_pt[i], 
      description='%s item de menu' % trans_pt[i])
  t.save()
  t = ItemTranslation(item=x, language='fr', name=trans_fr[i], 
      description='%s entrée du menu' % trans_fr[i])
  t.save()

