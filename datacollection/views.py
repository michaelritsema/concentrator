from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.shortcuts import HttpResponse
import time
import base64
import datetime

import time
import calendar
import uuid
import extensions

import messages
from messages.ExtensionCommand_pb2 import ExtensionCommand

from models import AgentMessage
from models import QueuedMesssage

@csrf_exempt
def index(request):
    xml = request.body
    protomsg = messages.xml_to_proto(xml)
    proto_type = type(protomsg).__name__
    msg = AgentMessage(message_type=proto_type, message=protomsg.SerializeToString())
    msg.save()
    return HttpResponse("")

@csrf_exempt
def enqueue(request):
    """ Take in some settings, generate a Protobuf, stick it on the queue
    """


    data = request.body
    print data
    return HttpResponse("")

    if 'cert' in request.GET:
        return enqueue_cert(request)

    data = request.body
    message = ExtensionCommand()
    message.timeStamp = int((datetime.datetime.now() - datetime.datetime(1970,1,1)).total_seconds())
    #message.extensionType = 1
    message.uuid = str(uuid.uuid1())
    message.serverJobID = 1
    message.correlationUUID = str(uuid.uuid1())
    message.extensionUUID = str(uuid.uuid1())
    message.command = 1
    message.messageVersion = 1
    #message.runLifetime = 1
    message.extensionObject = base64.decodestring(extensions.watchandkill)
    message.extensionParameters.extend(["10", "Calculator"])
    message.runType = 2
    queued_message = QueuedMesssage(message_type=type(message).__name__, message=message.SerializeToString())
    queued_message.save()

    return HttpResponse("")

@csrf_exempt
def enqueue_cert(request):
    """ Take in some settings, generate a Protobuf, stick it on the queue
    """

    message = ExtensionCommand()
    message.timeStamp = int((datetime.datetime.now() - datetime.datetime(1970,1,1)).total_seconds())
    #message.extensionType = 1
    message.uuid = str(uuid.uuid1())
    message.serverJobID = 1
    message.correlationUUID = str(uuid.uuid1())
    message.extensionUUID = str(uuid.uuid1())
    message.command = 1
    message.messageVersion = 1
    #message.runLifetime = 1
    message.extensionObject = base64.decodestring(extensions.collectcert)
    #message.extensionParameters.extend(["10", "Calculator"])
    message.runType = 1
    queued_message = QueuedMesssage(message_type=type(message).__name__, message=message.SerializeToString())
    queued_message.save()

    return HttpResponse("")


# example
# <pb type="AgentCommand">CMSSrpatKhABGLUsKh5jOlx3aW5kb3dzXHN5c3RlbTMyXG1zaHRtbC5kbGw=</pb>

@csrf_exempt
def dequeue(request, guid):
    #/control/{guid}
    try:
        msg = QueuedMesssage.objects.filter(is_delivered=False)[0]
    except:
         return HttpResponse("")

    encoded = base64.b64encode(msg.message)
    xml = '<pb type="ExtensionCommand">' + encoded + '</pb>'
    msg.is_delivered=True
    msg.save()
    return HttpResponse(xml)#extensions.watchandkill_real)
