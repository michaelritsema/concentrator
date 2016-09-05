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
- https://github.com/h2oai/h2o-2/wiki/installing-python-2.7-on-centos-6.3.-follow-this-sequence-exactly-for-centos-machine-only
```
yum install wget
wget https://bootstrap.pypa.io/ez_setup.py -O - | python2.7
wget https://bootstrap.pypa.io/get-pip.py -O - | python2.7
```


- Now use "python2.7" and "pip2.7" as alternatives to "python" and "pip"

*Setting up as Service:*

- concentrator must be installed at /opt/concentrator
- mv /opt/concentrator/init.d/concentrator /etc/init.d/concetrator
- chmod 755 /etc/init.d/concentrator
- chmod 755 /opt/concentrator 


*Tips*
Editing python in vim
```:set tabstop=8 expandtab shiftwidth=4 softtabstop=4```

