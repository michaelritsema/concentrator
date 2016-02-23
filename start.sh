#! /bin/sh
#/usr/local/bin/gunicorn -w 1 -b :8000 --chdir=/opt/concentrator --env DJANGO_SETTINGS_MODULE=zjango.settings zjango.wsgi
/usr/local/bin/python2.7 /opt/concentrator/manage.py runserver --settings zjango.local_settings 0.0.0.0:8001  &> /dev/null &
/usr/local/bin/python2.7 /opt/concentrator/manage.py splunk --settings zjango.local_settings --max-rows=20 --service  &> /dev/null &