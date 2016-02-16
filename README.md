*Concentrator Setup*

- Bash commands
```{r, engine='bash', count_lines}
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata ConsumerOffset
python manage.py run server 0.0.0.0:8000
```

- Update settings.py
-- SPLUNK_API_URL, SPLUNK_API_TOKEN

*Splunk Setup*

 - Point Splunk HTTP collector to the IP:PORT of the concentrator
 - Under Splunk Global Settings : Disable Splunk SSL unless you want to setup SSL on the server
 - Under Splunk Global Settings: Enable All Tokens
 - Generate an HTTP Token
 

*Centos 6.x Needs > Python 2.7*
Instrunctions for building and install Python 3 on Centos6.x: http://www.shayanderson.com/linux/install-python-3-on-centos-6-server.htm
