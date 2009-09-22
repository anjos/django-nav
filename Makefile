# Dear emacs, this is -*- Makefile -*-
# Created by Andre Anjos <Andre.dos.Anjos@gmail.com>, 20-Mar-2007

# These are helpers
MAKE_MESSAGE=sw/django-admin.py makemessages --all --extension=html,py,txt
COMPILE_MESSAGE=sw/django-admin.py compilemessages
LANGUAGES=en pt_BR fr es
PYTHON=python2.5
PROJECT=nav

.PHONY: test clean 

# ACTION: Executes a simple cleanup (remove '~' files and pyc files) and then
# will compile the PO locale files.
all: simpleclean

# ACTION: Builds the PO locale files, by reading our source code and updating
# the existing message catalog. This will not compile the resulting PO source
# files.
strings:
	@echo "Updating language files...";
	@cd $(PROJECT); for l in $(LANGUAGES); do if [ ! -d locale/$$l ]; then mkdir -pv locale/$$l; fi; done;
	@cd $(PROJECT) && ../$(MAKE_MESSAGE);

# ACTION: This will literally compile the PO files into MO files, that can be
# loaded by your web application
compile:
	@echo "Compiling language files...";
	@cd $(PROJECT) && ../$(COMPILE_MESSAGE);

install_django:
	@./scripts/install_django.sh;

remove_django:
	@rm -rf sw*

languages: install_django strings compile

update_languages:
	@for l in $(LANGUAGES); do cp test/sw/nav*/nav/locale/$$l/LC_MESSAGES/django.po nav/locale/$$l/LC_MESSAGES/; done

test: 
	@cd test && ./run.sh

clean: remove_django
	find . -name '*~' -print0 | xargs -0 rm -vf 
	find . -name '*.py?' -print0 | xargs -0 rm -vf
	@cd test && ./cleanup.sh
	@rm -rf *.egg-info build temp
