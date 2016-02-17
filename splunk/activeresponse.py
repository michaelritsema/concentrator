from __future__ import absolute_import
import requests
import os

class Device:
    path = "ziften"

    def __init__(self, hosts_mapping):
        #TODO Move this to a config file
        self.hosts_mapping = hosts_mapping
        self.fortinet_ip = "10.0.20.150"
        self.ziftenapi_url = "http://localhost:8000"

    def submit_action(self, settings, results):
        """
            Triggered by Splunk's submit
        """
        pass

    def run_action(self, settings, results):
        """
            Triggered by Splunk's 'Validate'
        """

        action_type = settings.get('action_type', '')
        # USB,FIREWALL,KILL,ALL

        payload = {
            "settings": settings,
            "results": results,
            "action_type" : action_type
        }

        requests.post(self.ziftenapi_url + '/api/enqueue', json=payload)

        if action_type in ('FIREWALL', 'ALL'):
            self.fortinet(settings, results)

    def undo_action(self):
        self.__log("I am undoing the action")

    def fetch_feedback(self):
        self.__log("I am fetching the feedback")

    def expiration(self):
        self.__log("I am running the expiration")

    def fortinet(self, settings, results):
        # ipaddress must exist in query
        try:
            stmt = "/opt/splunk/bin/python /opt/splunk/etc/apps/search/bin/fortiquarantine.py " + self.fortinet_ip + " root " + results['ipaddress'] + ' > /dev/null 2>&1'
            os.system(stmt)
        except:
            pass



if __name__ == "__main__":
    device = Device("")
    #device.submit_action({}, {})
    #device.fortinet({},{'ipaddress':'127.0.0.1'})