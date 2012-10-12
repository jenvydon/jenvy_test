MANAGE=django-admin.py

tests:
    PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=jenvy_test.settings $(MANAGE) test contacts

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=jenvy_test.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=jenvy_test.settings $(MANAGE) syncdb --noinput