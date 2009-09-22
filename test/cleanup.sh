#!/bin/bash 
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Ter 15 Set 2009 11:34:07 CEST
find . -name '*~' -print0 | xargs -0 rm -f
find . -name '*.pyc' -print0 | xargs -0 rm -f
rm -rf sw*
rm -rf project
rm -rf media 
