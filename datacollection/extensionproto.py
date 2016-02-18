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

    message.extensionObject = base64.decodestring(extensions.watchandkill)
    message.extensionParameters.extend(["10", filename])
    message.runType = 2

    return message.SerializeToString()


def cert(payload):
    """
    Collect Cert
    """
    message = defaults()

    message.extensionObject = base64.decodestring(extensions.collectcert)
    message.runType = 1

    return message.SerializeToString()

def killpid(payload):
    """
    Kill Process by PID
    """

    message = defaults()
    pid = payload["results"]["pid"]
    message.extensionObject = base64.decodestring(extensions.killpid)
    message.extensionParameters.extend([str(pid)])
    message.runType = 1

    return message.SerializeToString()


