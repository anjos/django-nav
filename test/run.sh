#!/bin/bash 
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Seg 14 Set 2009 16:49:23 CEST

export PYTHON=`which python2.5`
start_dir=`pwd`

source ./setup.sh
./install.sh

if [ ! -d project ]; then
  django-admin.py startproject project;
  rm -f project/settings.py;
  ln -s ../settings.py project/settings.py;
  rm -f project/urls.py;
  ln -s ../urls.py project/urls.py;

  # base django project installation
  cd project;
  ${PYTHON} manage.py syncdb --noinput;
  ${PYTHON} manage.py createsuperuser --email=andre.dos.anjos@gmail.com 
  mkdir templates;
  ln -s ../../base.html templates/base.html;
  cd ${start_dir};

  # and prepare the database for a manual inspection
  ${PYTHON} sw/djanmenus*/djanmenus/test_initial.py
fi

if [ ! -d media ]; then
  mkdir media;
  cd media;
  ln -s ../sw/Django*/django/contrib/admin/media django;
  svn co http://django-rosetta.googlecode.com/svn/trunk/rosetta/templates/rosetta rosetta
  cd ${start_dir};
fi

# update the translation strings
cd sw/djanmenus*/djanmenus;
django-admin.py compilemessages
cd ${start_dir};

# now run all tests
cd project;
${PYTHON} -m compileall .
${PYTHON} manage.py test djanmenus;
# and let the webserver running
${PYTHON} manage.py runserver 8080;
cd ${start_dir};

