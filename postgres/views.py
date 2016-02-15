from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import messages
from messages import *
import proto_to_dict
from datacollection.models import AgentMessage
from django.http import JsonResponse


def index(request):
    max = 10
    if 'max' in request.GET:
        max = request.GET['max']

    offset = 0

    if 'offset' in request.GET:
        offset = request.GET['offset']

    results = AgentMessage.objects.filter(message_type='OSXNetworkConnect', id__gte=offset).order_by('id')[:max]

    dicts = []

    for result in results:
        newdict = proto_to_dict.protobuf_to_dict(messages.proto_to_dict(result.message_type, result.message))
        newdict['message_type'] = result.message_type
        newdict['id'] = result.id
        newdict['insert_time'] = result.insert_time
        dicts.append(newdict)

    return JsonResponse(dicts, safe=False)
