from __future__ import unicode_literals

import datetime
from django.contrib import admin

from django.db import models

class ConsumerOffset(models.Model):
    consumer = models.TextField() #splunk-default
    last_row_id = models.BigIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __unicode__(self):
        return "consumer:" + self.consumer + " last row_id" + ":" + str(self.last_row_id)

admin.site.register(ConsumerOffset)