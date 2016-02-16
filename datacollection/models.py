from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

from django.utils.timezone import now
import messages
import proto_to_dict
import time
import socket
import struct
import base64
import ipaddr

class ProtobufField(models.BinaryField):

    description = "Protobuffers"

    def __init__(self, *args, **kwargs):
        super(ProtobufField, self).__init__(*args, **kwargs)


class AgentMessage(models.Model):
    insert_time = models.DateTimeField(auto_now_add=True)
    message_type = models.TextField()
    message = models.BinaryField()

    def format_ip(self, bytes):

        b = ipaddr.Bytes(base64.b64decode(bytes))
        ip = ""
        if len(b) == 4:
            ip = ipaddr.IPv4Address(b)
        else:
            ip = ipaddr.IPv6Address(b)
        return str(ip)


    def format_dict(self, message_type, data_dict):

        if message_type in ("NetworkConnect", "OSXNetworkConnect") :
            data_dict["IPAddress"] = self.format_ip(data_dict["IPAddress"])
            if "IPSourceAddress" in data_dict:
                data_dict["IPSourceAddress"] = self.format_ip(data_dict["IPSourceAddress"])

        data_dict["message_type"] = message_type.lower()
        if "agentGUID" in data_dict:
            data_dict["agentGUID"] = data_dict["agentGUID"].strip("{}").lower()
        timestamp = time.time()
        if "timeStamp" in data_dict:
            data_dict["clienttime"] = data_dict["timeStamp"]/ 10000000 - 11644473600
            data_dict["servertime"] = timestamp
            del data_dict["timeStamp"]
        if "eventType" in data_dict:
            data_dict["evnttype"] = data_dict["eventType"]
            del data_dict["eventType"]
        if "eventtype" in data_dict:
            data_dict["evnttype"] = data_dict["eventtype"]
            del data_dict["eventtype"]
        data_dict["organizational_unit"] = "<OU>"

        return data_dict

    def message_dict(self):
        newdict = proto_to_dict.protobuf_to_dict(messages.proto_to_dict(self.message_type, self.message))
        newdict['id'] = self.id
        # no serializable
        #newdict['insert_time'] = self.insert_time
        # lower case fields for splunk

        formatted_dict = self.format_dict(self.message_type, newdict)

        lowerdict = {}
        for k,v in formatted_dict.iteritems():
            lowerdict[k.lower()] = v
        return lowerdict


class QueuedMesssage(models.Model):
    insert_time = models.DateTimeField(auto_now_add=True)
    message_type = models.TextField()
    message = models.BinaryField()
    is_delivered = models.BooleanField(default=False)

class AgentMessageAdmin(admin.ModelAdmin):
    list_display = ('insert_time', 'message_type','message_dict_short')
    readonly_fields = ('insert_time', 'message_type', 'message_dict')
    list_filter = ('message_type', )
    list_per_page = 5

    def message_dict_short(self, obj):
        return str(obj.message_dict())[:255]

    def message_dict(self, obj):
        return str(str(obj.message_dict()))


admin.site.register(QueuedMesssage, AgentMessageAdmin)
admin.site.site_header = 'Ziften Agent Concentrator'
admin.site.register(AgentMessage, AgentMessageAdmin)
