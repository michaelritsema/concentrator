__all__= ['ActiveX_pb2', 'AgentCommandResponse_pb2', 'AgentCommand_pb2', 'AgentMessage_pb2', 'AgentSettingsResponse_pb2', 'AgentSettings_pb2', 'AgentStatus_pb2', 'AppStartTime_pb2', 'ApplicationPerformance_pb2', 'AutoRuns_pb2', 'AutoStarts_pb2', 'Binary_pb2', 'BootAnalysis_pb2', 'BootInfo_pb2', 'BootProfile_pb2', 'CorrelationAlert_pb2', 'EventLogRecord_pb2', 'EventNetConnect_pb2', 'ExecReportStatistics_pb2', 'ExtensionCatalogRequest_pb2', 'ExtensionCatalogResponse_pb2', 'ExtensionCommandResponse_pb2', 'ExtensionCommand_pb2', 'ExtensionRunNow_pb2', 'ExtensionRunResults_pb2', 'FileContents_pb2', 'FrameHeader_pb2', 'GenericServerMonitor_pb2', 'InstalledPrograms_pb2', 'InterferingProcess_pb2', 'InternalMessage_pb2', 'IpfixEncapsulation_pb2', 'LogFileEntry_pb2', 'LogonNotifications_pb2', 'NetworkConnect_pb2', 'NetworkDataIP_pb2', 'NetworkDataPID_pb2', 'ODBCDrivers_pb2', 'ODBCSources_pb2', 'OSXAgentCommandResponse_pb2', 'OSXAgentStatus_pb2', 'OSXAutoStart_pb2', 'OSXBootAnalysis_pb2', 'OSXBootProfile_pb2', 'OSXEventLogRecord_pb2', 'OSXFileContents_pb2', 'OSXInstalledPrograms_pb2', 'OSXNetworkConnect_pb2', 'OSXPolicyStatus_pb2', 'OSXProcessInventory_pb2', 'OSXRemediateResponse_pb2', 'OSXResourceUsage_pb2', 'OSXRunningProcessesSummary_pb2', 'OSXSoftwareInventory_pb2', 'OSXSystemInventoryDiskDrives_pb2', 'OSXSystemInventoryLogicalDisks_pb2', 'OSXSystemInventoryNetworkAdapters_pb2', 'OSXSystemInventory_pb2', 'OSXUpdateAvailable_pb2', 'OSXUpdateSettings_pb2', 'OSXUpdate_pb2', 'OfficePlugins_pb2', 'Policies_pb2', 'PolicyStatus_pb2', 'Policy_pb2', 'PostgreSQLLogFileEntry_pb2', 'PostgresType_pb2', 'ProcessEnd_pb2', 'ProcessInventory_pb2', 'RemediateResponse_pb2', 'Remediate_pb2', 'ResourceUsage_pb2', 'RunningProcessesSummary_pb2', 'Services_pb2', 'ShutdownProfile_pb2', 'SystemInventoryDiskDrives_pb2', 'SystemInventoryLogicalDisks_pb2', 'SystemInventoryNetworkAdapters_pb2', 'SystemInventory_pb2', 'SystemPerformance_pb2', 'TestProtobufV1_pb2', 'TestProtobufV2_pb2', 'WinSat_pb2', 'WindowsUpdateAvailable_pb2', 'WindowsUpdateServers_pb2', 'WindowsUpdateSettings_pb2', 'WindowsUpdate_pb2', 'iOSApplicationInfo_pb2', 'iOSDeviceInfo_pb2', 'iOSProcessInfo_pb2']

import xml.etree.ElementTree as ET
import base64
from messages import *

"""
    Tools from marshalling agent message
"""

def decode_from_xml(http_body):
    """ Decodes the XML Post of the agent into the protobuf name and b64 encoded protobuf
    """

    root = ET.fromstring(http_body)
    return root.attrib['type'], root.text

def xml_to_proto(xml):
    """ Converts XML wrapper and returns Proto
    """
    message_type, message = decode_from_xml(xml)
    return proto_to_dict(message_type, message, True)

def proto_to_dict(message_type, message, is_b64encoded=False):
    """ Returns the protobuf message serialized to the Python Object
        E.g, PolicyStatus_pb2.PolicyStatus() with the method
            .ParseFromString(b64string) called
    """
    if is_b64encoded:
        message = base64.decodestring(message)

    decoded = getattr(globals()[message_type + "_pb2"], message_type)()
    decoded.ParseFromString(message)

    return decoded

def get_test_xml():
    return """<pb HMAC="RWy40loOnuwO3k2kY52bTcH5PPc=" type="OSXPolicyStatus">CICUvcLnjNboARIkRjMxNDZBQTQtRkI1Qy00QUFFLTkyRDctOTA3MUJBRTA4QzM0GAEgww8oBDIAOgBCAEjDD1IgMGFiMjQwZTg2MDBmYjdlNGNlZjkyZGYyZDhmYzI5NGZaJGU4NGQ0MmJhLWZhZDUtNDIzOC04NmI1LTY4ZDk4Y2YxYWZkOGIA</pb>"""

if __name__ == "__main__":
    http_body = get_test_xml()
    print xml_to_proto(http_body)