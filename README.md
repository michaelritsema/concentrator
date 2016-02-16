*Concentrator Setup*

- Bash commands
```{r, engine='bash', count_lines}
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata ConsumerOffset
python manage.py runserver 0.0.0.0:8000
```

- Update settings.py
-- SPLUNK_API_URL, SPLUNK_API_TOKEN

*Splunk Setup*

 - Point Splunk HTTP collector to the IP:PORT of the concentrator
 - Under Splunk Global Settings : Disable Splunk SSL unless you want to setup SSL on the server
 - Under Splunk Global Settings: Enable All Tokens
 - Generate an HTTP Token
 
*Centos 6.x*

- Centos 6.x needs Python 2.7
- http://toomuchdata.com/2014/02/16/how-to-install-python-on-centos/
- Now use "python2.7" and "pip2.7" as alternatives to "python" and "pip"
