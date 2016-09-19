import requests
from requests import auth
import os
import json
import zipfile

#print dir(requests)


def enqueue():
	r = requests.post('http://localhost:8000/api/enqueue',json.dumps({
		'name':'Kill a Specific Process by PID',
		'ProcessIDs': "100 200 500 700"
		}))
	print r.content

def dequeue():
	r = requests.get('http://localhost:8000/api/control/BEEF')
	print r.content

def update_zeps():
	url = "http://10.0.10.236:8080/job/Dev-Extensions/ws/output/*zip*/output.zip"
	r = requests.get(url, stream=True, auth=(auth.HTTPBasicAuth("michael.ritsema", "netfiz_ritsema")))

	filename = '/tmp/extensions.zip'
	with open('/tmp/extensions.zip', 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024):
			if chunk:
				f.write(chunk)
	with zipfile.ZipFile(filename) as z:
		for name in z.namelist():
			if name.endswith('.zep'):
				data = z.open(name).read()
				requests.post('http://localhost:8000/api/zep', data)


if __name__ == "__main__":
	if os.sys.argv[1] == "enqueue":
		enqueue()
	if os.sys.argv[1] == "dequeue":
		dequeue()
	if os.sys.argv[1] == "update-zeps":
		update_zeps()
