"""
    Utilities to help in generating extension protobufs to send to agent
"""
from messages.ExtensionCommand_pb2 import ExtensionCommand
import datetime
import base64
import uuid
import re
import extensions

def create(ext, params,payload):
    message = ExtensionCommand()
    message.timeStamp = int((datetime.datetime.now() - datetime.datetime(1970,1,1)).total_seconds())
    message.uuid = str(uuid.uuid1())
    message.serverJobID = 1
    message.correlationUUID = str(uuid.uuid1())
    message.extensionUUID = str(uuid.uuid1())
    message.command = 1
    message.messageVersion = 1
    message.extensionObject = ext

    # include all payload values that match params list
    if 'RAW' in payload:
        message.extensionParameters.extend([payload['RAW']])
            
    for p in params:
        print "checking parameter:" + p["name"]
        if p['name'] in payload:
            print "added parameter: " + p['name'] 
            message.extensionParameters.extend([payload[p['name']]])
    return message.SerializeToString()
            
     