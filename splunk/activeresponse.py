from __future__ import absolute_import
import requests

"""
    This file is placed in the ziften splunk app folder
"""

class Device:
    path = "ziften"

    def __init__(self, hosts_mapping):
        self.hosts_mapping = hosts_mapping

    def submit_action(self, settings, results):
        """
            Triggered by Splunk's submit
        """
        pass

    def run_action(self, settings, results):
        """
            Triggered by Splunk's 'Validate'
        """
        ziftenapi_url = "http://localhost:8000"

        payload = {
            "settings": settings,
            "results": results
        }

        requests.post(ziftenapi_url + '/api/enqueue', json=results)

    def undo_action(self):
        self.__log("I am undoing the action")

    def fetch_feedback(self):
        self.__log("I am fetching the feedback")

    def expiration(self):
        self.__log("I am running the expiration")

if __name__ == "__main__":
    device = Device("")
    device.submit_action({}, {})