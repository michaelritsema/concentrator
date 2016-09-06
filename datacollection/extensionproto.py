"""
    Utilities to help in generating extension protobufs to send to agent
"""
from messages.ExtensionCommand_pb2 import ExtensionCommand
import datetime
import base64
import uuid
import re
import extensions

def defaults():
    message = ExtensionCommand()
    message.timeStamp = int((datetime.datetime.now() - datetime.datetime(1970,1,1)).total_seconds())
    message.uuid = str(uuid.uuid1())
    message.serverJobID = 1
    message.correlationUUID = str(uuid.uuid1())
    message.extensionUUID = str(uuid.uuid1())
    message.command = 1
    message.messageVersion = 1
    return message

def kill(payload):
    """
    Kill Process
    """

    message = defaults()
    imagefilepath = payload["results"]["imagefilepath"]
    filename = re.sub(".*\\\\","", imagefilepath)
    message.extensionObject = base64.decodestring(extensions.killprocessbyfilename)
    message.extensionParameters.extend([filename])
    message.runType = 1
    return message.SerializeToString()

def start_service(payload):
    """
    Start Service
    """

    message = defaults()
    service_name = payload["results"]["name"]
    message.extensionObject = base64.decodestring(extensions.startservice)
    message.extensionParameters.extend([service_name])
    message.runType = 1
    return message.SerializeToString()    

def stop_service(payload):
    """
    Start Service
    """

    message = defaults()
    service_name = payload["results"]["name"]
    message.extensionObject = base64.decodestring(extensions.stopservice)
    message.extensionParameters.extend([service_name])
    message.runType = 1
    return message.SerializeToString()        