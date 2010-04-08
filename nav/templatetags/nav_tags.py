#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Seg 16 Mar 2009 18:32:11 CET 

"""An easy handle to bring menu items into your templates 
"""

import re
from django import template
from nav.models import * 
from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag
def get_name(item, language): return item.get_name(language)

@register.simple_tag
def get_description(item, language): return item.get_description(language)
  
class RootNavigationNode(template.Node):
  def __init__(self, user, var_name):
    self.user = template.Variable(user)
    self.var_name = var_name

  def render(self, context):
    try:
      items = [k for k in Item.objects.filter(parent=None).order_by('priority', 'name') if k.is_allowed(self.user.resolve(context))]
      context[self.var_name] = items 
    except template.VariableDoesNotExist:
      raise template.TemplateSyntaxError, \
          '"%s" is not a valid site user' % self.user
    return ''

@register.tag(name='menu_items')
def get_root_items(parser, token):
  # This version uses a regular expression to parse tag contents.
  try:
    # Splitting by None == splitting by spaces.
    tag_name, arg = token.contents.split(None, 1)
  except ValueError:
    raise template.TemplateSyntaxError, \
        "%r tag requires arguments" % token.contents.split()[0]
  m = re.search(r'^for ([\w\.]+) as (\w+)$', arg.strip())
  if not m:
    raise template.TemplateSyntaxError, \
        "%r tag has invalid arguments - review your code." % tag_name
  username, var_name = m.groups()
  return RootNavigationNode(username, var_name)
