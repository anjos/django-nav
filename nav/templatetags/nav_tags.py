#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Seg 16 Mar 2009 18:32:11 CET 

"""An easy handle to translate menu items
"""

from django.template import Template, Context
from django import template
register = template.Library()
from nav.models import get_translation

@register.simple_tag
def item_trans(item, variable, language):
  return get_translation(item, variable, language)

@register.simple_tag
def render_template(url):
  return Template(url).render(Context())
