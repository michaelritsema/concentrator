from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse

import base64
import extensions
import json
import extensionproto
import messages

from models import AgentMessage
from models import QueuedMesssage
from models import Zext

from zepreader import ZextContainer
import sys

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
    print data
    payload = json.loads(data)
    name = payload["name"]
    z = None
    
    try: 
        z = Zext.objects.get(name=name)
    except:
        return HttpResponse("No extension loaded with name: "+ name)
    message_type = "ExtensionCommand"
    ext = z.extension_text
    # TODO: THIS NEEDS TO BE UNICODE

    message = extensionproto.create(str(ext),z.param_list(),payload)
    
    agentguid ="<NOT SET>"
    if "agentguid" in payload:
        agentguid = payload["agentguid"]

    if message:
        queued_message = QueuedMesssage(agentguid=agentguid, message_type=message_type, message=message)
        queued_message.save()


    return HttpResponse("" + z.name)


@csrf_exempt
def dequeue(request, guid):
    msg = None
    xml = ""

    print 'dequeue'
    try:
        msg = QueuedMesssage.objects.filter(agentguid=guid,is_delivered=False)[0]
    except:
        print 'fail'
        pass

    if msg:
        encoded = base64.b64encode(msg.message)
        xml = '<pb type="ExtensionCommand">' + encoded + '</pb>'
        msg.is_delivered = True
        msg.save()
    return HttpResponse(xml)


@csrf_exempt
def zep(request):
    """
    Upload a ZEP file
    Test: curl --data @"/Users/michaelritsema/virtual-projects/splunk-conf/concentrator/datacollection/powershell/scripts/GetSystemMemory.zep" http://localhost:8000/api/zep

    """

    data=request.body
    
    msg = Zext(zep=data)
    msg.save() #double save required
    print msg.name
    try:
        Zext.objects.filter(name=msg.name).delete()
    except:
        print sys.exc_info()[0]

    msg.save()

    return HttpResponse(msg.name) 


    