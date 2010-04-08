#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sex 05 Mar 2010 11:48:41 CET 

"""Creates repositories for the inital tests.
"""

from django.core.management import setup_environ
import settings
setup_environ(settings)

# This bit will create the superuser
from django.contrib.auth.models import User, Group

def make_group(name):
  for k in Group.objects.filter(name=name):
    print 'Deleting group "%s"' % k.name
    k.delete()
  group = Group()
  group.name = name
  group.save()
  print 'Created group "%s"' % (name)
  return group

def make_user(name, staff, admin, groups=[]):
  for k in User.objects.filter(username=name):
    print 'Deleting user "%s"' % k.username
    k.delete()

  user = User()
  user.username = name
  user.first_name = name.capitalize()
  user.last_name = name.capitalize() + 'ston'
  user.email = '%s@example.com' % name
  user.is_staff = staff
  user.is_active = True
  user.is_superuser = admin
  user.set_password(user.username)
  user.save()
  user.groups = groups
  user.save()
  print 'Created user "%s" with password "%s"' % (name, name)

make_user('admin', staff=True, admin=True)
make_user('staff', staff=True, admin=False)
make_user('normal', staff=False, admin=False)
test_group = make_group('Test Group')
make_user('grouped', staff=False, admin=False, groups=(test_group,))

