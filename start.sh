#/usr/local/bin/gunicorn -w 1 -b :8000 --chdir=/opt/concentrator --env DJANGO_SETTINGS_MODULE=zjango.settings zjango.wsgi
/usr/local/bin/python2.7 /opt/concentrator/manage.py runserver 0.0.0.0:8000  &> /dev/null
/usr/local/bin/python2.7 /opt/concentrator/manage.py splunk --max-rows=20 --service