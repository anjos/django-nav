#!/bin/bash 
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sex 04 Abr 2008 14:36:05 CEST

if [ $# -gt 0 ]; then
  echo "usage: $0";
  exit 1;
fi

# Automatically set!
BASEDIR=`pwd`
python_version=`${PYTHON} -c 'import sys;print "%d.%d" % sys.version_info[0:2]'`
INSTALLDIR=${BASEDIR}/sw

# Versions
setuptools_egg=setuptools-0.6c9-py${python_version}.egg
setuptools=http://pypi.python.org/packages/${python_version}/s/setuptools/${setuptools_egg};

# This script will download and install all necessary software for us
[ -r sw ] && rm -f sw;
if [ -d ${INSTALLDIR}-python${python_version} ]; then
  echo "Directory ${INSTALLDIR}-python${python_version} exists. Upgrade only."
  echo "If you need re-installing, remove the 'sw*' directories manually."
  export UPGRADE='--upgrade'
else
  mkdir -pv ${INSTALLDIR}-python${python_version};
fi
cd `dirname ${INSTALLDIR}`;
ln -s `basename ${INSTALLDIR}`-python${python_version} `basename ${INSTALLDIR}`;

export PATH=${INSTALLDIR}:${PATH}
export PYTHONPATH=${INSTALLDIR}

# We install the setuptools
echo "### Installing ${setuptools_egg}..."
wget ${setuptools} 
sh ${setuptools_egg} --install-dir=${INSTALLDIR}
rm -f ${setuptools_egg}
export PATH=${INSTALLDIR}:${PATH}
echo "### Installation of ${setuptools_egg} is done!"

function install () {
  local package=$1;
  shift;
  echo "### Installing $package..."
  easy_install-${python_version} ${UPGRADE} --install-dir=${INSTALLDIR} $*;
  echo "### Installation of $package is done!"
}

install django django 

