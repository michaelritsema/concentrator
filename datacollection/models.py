from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

from django.utils.timezone import now
import messages
import proto_to_dict

class ProtobufField(models.BinaryField):

    description = "Protobuffers"

    def __init__(self, *args, **kwargs):
        super(ProtobufField, self).__init__(*args, **kwargs)

class AgentMessage(models.Model):
    insert_time = models.DateTimeField(auto_now_add=True)
    message_type = models.TextField()
    message = models.BinaryField()

    def message_dict(self):
        newdict = proto_to_dict.protobuf_to_dict(messages.proto_to_dict(self.message_type, self.message))
        newdict['message_type'] = self.message_type.lower()
        newdict['id'] = self.id
        # no serializable
        #newdict['insert_time'] = self.insert_time
        # lower case fields for splunk
        lowerdict = {}
        for k,v in newdict.iteritems():
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
        return str(messages.proto_to_dict(obj.message_type, obj.message))[:255]

    def message_dict(self, obj):
        return str(messages.proto_to_dict(obj.message_type, obj.message))


admin.site.register(QueuedMesssage, AgentMessageAdmin)
admin.site.site_header = 'Ziften Agent Concentrator'
admin.site.register(AgentMessage, AgentMessageAdmin)
