from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import HttpResponse

import base64
import extensions
import json
import extensionproto
import messages

from models import AgentMessage
from models import QueuedMesssage

@csrf_exempt
def index(request):
    """
        Endpoint to consume data from agents in XML wrappers
    """
    msg = ""
    try:
        xml = request.body
        protomsg = messages.xml_to_proto(xml)
        proto_type = type(protomsg).__name__
        msg = AgentMessage(message_type=proto_type, message=protomsg.SerializeToString())
        print 'Message %s received' % proto_type
        msg.save()
    except:
        print "failed to parse message" + msg

    return HttpResponse("")

@csrf_exempt
def enqueue(request):
    """ Take in some settings, generate a Protobuf, stick it on the queue
    """

    data = request.body
    payload = json.loads(data)
    action_type = payload["action_type"]
    message_type = "ExtensionCommand"
    message = None

    if action_type == "KILL":
        message = extensionproto.kill(payload)
    elif action_type == "CERT":
        message = extensionproto.cert(payload)
    elif action_type =="KILLPID":
        message = extensionproto.killpid(payload)
    elif action_type =="EJECTUSB":
        message = extensionproto.ejectusb(payload)

    if message:
        queued_message = QueuedMesssage(message_type=message_type, message=message)
        queued_message.save()

    return HttpResponse("")

@csrf_exempt
def dequeue(request, guid):
    msg = None
    xml = ""

    try:
        msg = QueuedMesssage.objects.filter(is_delivered=False)[0]
    except:
         pass

    if msg:
        encoded = base64.b64encode(msg.message)
        xml = '<pb type="ExtensionCommand">' + encoded + '</pb>'
        msg.is_delivered = True
        msg.save()
    return HttpResponse(xml)
