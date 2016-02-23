import requests
import json

from django.core.management.base import BaseCommand, CommandError
from datacollection.models import AgentMessage
from export.models import ConsumerOffset
from django.conf import settings
from time import sleep


class Command(BaseCommand):
    help = 'Sync data with splunk'


    def add_arguments(self, parser):
         # Named (optional) arguments
        parser.add_argument('--reset-offset',
            action='store_true',
            dest='reset-offset',
            default=False,
            help='Reset offset of consumer')

        parser.add_argument('--max-rows',
            dest='max_rows',
            default=5,
            help='Max rows to sync')

        parser.add_argument('--service',
            dest='max_rows',
            default=5,
            help='Max rows to sync')



    def handle_loop(self, max_rows):
        rows = list(AgentMessage.objects.filter(id__gt=consumer.last_row_id).order_by('id')[:max_rows])
        row_count = len(rows)
        self.stdout.write("Sending data to splunk. Sending %s found rows after last_row_id %s" % (row_count, consumer.last_row_id))

        #TODO: add batch size

        dicts = [row.message_dict() for row in rows]
        self.sync_splunk(dicts)

        if len(rows) > 0:
            consumer.last_row_id = rows[-1].id
            consumer.save()
            self.stdout.write("Set last_row_id to %s" %(consumer.last_row_id,))

    def handle(self, *args, **options):
        if options['reset-offset']:
            c = ConsumerOffset.objects.get(consumer='splunk')
            c.last_row_id = 0
            c.save()
            self.stdout.write("Reseting consumer offset to 0.")
            return

        run_as_service = False

        if options['service']:
            run_as_service = True

        #options['poll_id']:
        consumer = ConsumerOffset.objects.get(consumer='splunk')

        max_rows = 5

        if 'max_rows' in options:
            max_rows = options['max_rows']

        if run_as_service:
            while True:
                self.handle_loop(max_rows)
                sleep(5)

        self.handle_loop(max_rows)



    def sync_splunk(self, log_data_list):

        headers = {
            "authorization": "Splunk %s" % settings.SPLUNK_API_TOKEN
        }

        url = "http://%s/services/collector" % settings.SPLUNK_API_URL

        #log_data = {"message_type": "http_test", "other": 1}

        rootevent = {
            # "time": ,
            "host": "ziften",
            "sourcetype": "concentrator",
            "source": "ziften"
        }

        data = ""
        for row in log_data_list:
            rootevent['event'] = row
            data = data + json.dumps(rootevent).encode('utf8')

        r = requests.post(url, data=data, headers=headers)

        print r
