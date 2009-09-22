=====================
 Developing Djanmenu
=====================

Follow these steps:

1. To start testing and see what is currently available, just say ``make
   test``. The first time you run this script you will be asked for a dummy
   adminstrator username and password. Just fill in values of your liking.
   Point your browser to http://localhost:8080/menu/, photos, or
   calendar to checkout what is there;
2. To update the language files, say ``make languages``;
3. To modify the language files, go into test mode and re-direct your browser
   to http://localhost:8080/rosetta. Enter your username and password defined
   during step 1. Please note that after modifying the translations at the
   given web address, **only the test version** of the PO gettext catalogs
   will be modified. To update the project directory from the test directory,
   just do ``make update_languages``. This will copy the modified PO files into
   the official area. You may ``make clean`` again after that point, if it
   suits you;
4. The command ``make clean`` will basically wipe-out everything that is not
   part of the GIT checkout, so be aware.

