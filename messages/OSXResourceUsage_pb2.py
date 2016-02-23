# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OSXResourceUsage.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import PostgresType_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='OSXResourceUsage.proto',
  package='',
  serialized_pb='\n\x16OSXResourceUsage.proto\x1a\x12PostgresType.proto\"\xe4\x0b\n\x10OSXResourceUsage\x12 \n\ttimeStamp\x18\x01 \x02(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x1b\n\tagentGUID\x18\x02 \x02(\tB\x08\x82\xb5\x18\x04uuid\x12\x0e\n\x03PID\x18\x03 \x01(\x05:\x01\x30\x12\x12\n\ntimeActive\x18\x04 \x02(\x04\x12\x15\n\rimageFilepath\x18\x05 \x01(\t\x12\x13\n\x0b\x61\x63\x63ountName\x18\x06 \x02(\t\x12\x12\n\ndomainName\x18\x07 \x02(\t\x12\x1a\n\x12totalProcessorTime\x18\x08 \x02(\x04\x12 \n\x18totalSystemProcessorTime\x18\t \x02(\x04\x12\x1b\n\x13totalSystemIdleTime\x18\n \x02(\x04\x12\'\n\x1ftotalSpikeTimeForegroundProcess\x18\x0b \x02(\x04\x12\x1f\n\x17totalSpikeProcessorTime\x18\x0c \x02(\x04\x12)\n!totalSpikeTimeBackgroundProcesses\x18\r \x02(\x04\x12%\n\x1dtotalSpikeSystemProcessorTime\x18\x0e \x02(\x04\x12 \n\x18totalSpikeSystemIdleTime\x18\x0f \x02(\x04\x12,\n$numTimesSpikeBackgroundMemorySampled\x18\x10 \x02(\r\x12\'\n\x1f\x61vgSpikePhysicalMemoryAvailable\x18\x11 \x02(\x01\x12\x1d\n\x15numTimesMemorySampled\x18\x12 \x02(\r\x12\x19\n\x11\x61vgWorkingSetSize\x18\x13 \x02(\x01\x12\"\n\x1a\x61vgPhysicalMemoryAvailable\x18\x14 \x02(\x01\x12\x1e\n\x16\x61vgPhysicalMemoryTotal\x18\x15 \x02(\x01\x12\x14\n\x0cimageFileMD5\x18\x16 \x01(\t\x12\x11\n\tsentBytes\x18\x17 \x02(\x04\x12\x15\n\rreceivedBytes\x18\x18 \x02(\x04\x12\x17\n\x0fsystemSentBytes\x18\x19 \x02(\x04\x12\x1b\n\x13systemReceivedBytes\x18\x1a \x02(\x04\x12\x13\n\x0b\x65lapsedTime\x18\x1b \x02(\x03\x12\"\n\x1anumberSampledResponseTimes\x18\x1c \x02(\r\x12\x17\n\x0fsumResponseTime\x18\x1d \x02(\x04\x12\x16\n\x0espikeSentBytes\x18\x1e \x02(\x04\x12\x1a\n\x12spikeReceivedBytes\x18\x1f \x02(\x04\x12\x1e\n\x16spikeNetworkTimeSystem\x18  \x02(\x04\x12\x1c\n\x14spikeSystemSentBytes\x18! \x02(\x04\x12!\n\x19spikesSystemReceivedBytes\x18\" \x02(\x04\x12&\n\x1enumTimesSpikeWorkingSetSampled\x18# \x02(\r\x12)\n!spikeNetworkTimeForegroundProcess\x18$ \x02(\x04\x12\x1e\n\x16\x61vgSpikeWorkingSetSize\x18% \x02(\x01\x12\x19\n\x11readTransferCount\x18& \x02(\x04\x12\x1a\n\x12writeTransferCount\x18\' \x02(\x04\x12\x1f\n\x17systemReadTransferCount\x18( \x02(\x04\x12 \n\x18systemWriteTransferCount\x18) \x02(\x04\x12$\n\x1cspikeIOTimeForegroundProcess\x18* \x02(\x04\x12\x1e\n\x16spikeReadTransferCount\x18+ \x02(\x04\x12\x1f\n\x17spikeWriteTransferCount\x18, \x02(\x04\x12\x19\n\x11spikeIOTimeSystem\x18- \x02(\x04\x12$\n\x1cspikeSystemReadTransferCount\x18. \x02(\x04\x12%\n\x1dspikeSystemWriteTransferCount\x18/ \x02(\x04\x12\x0e\n\x06siteId\x18\x30 \x01(\t\x12\x16\n\x04uuid\x18\x31 \x01(\tB\x08\x82\xb5\x18\x04uuidB=\n\"com.ziften.server.protocol.messageB\x17OSXResourceUsageMessage')




_OSXRESOURCEUSAGE = _descriptor.Descriptor(
  name='OSXResourceUsage',
  full_name='OSXResourceUsage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='OSXResourceUsage.timeStamp', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='agentGUID', full_name='OSXResourceUsage.agentGUID', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='PID', full_name='OSXResourceUsage.PID', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeActive', full_name='OSXResourceUsage.timeActive', index=3,
      number=4, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imageFilepath', full_name='OSXResourceUsage.imageFilepath', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accountName', full_name='OSXResourceUsage.accountName', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='domainName', full_name='OSXResourceUsage.domainName', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='totalProcessorTime', full_name='OSXResourceUsage.totalProcessorTime', index=7,
      number=8, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='totalSystemProcessorTime', full_name='OSXResourceUsage.totalSystemProcessorTime', index=8,
      number=9, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='totalSystemIdleTime', full_name='OSXResourceUsage.totalSystemIdleTime', index=9,
      number=10, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='totalSpikeTimeForegroundProcess', full_name='OSXResourceUsage.totalSpikeTimeForegroundProcess', index=10,
      number=11, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='totalSpikeProcessorTime', full_name='OSXResourceUsage.totalSpikeProcessorTime', index=11,
      number=12, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='totalSpikeTimeBackgroundProcesses', full_name='OSXResourceUsage.totalSpikeTimeBackgroundProcesses', index=12,
      number=13, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='totalSpikeSystemProcessorTime', full_name='OSXResourceUsage.totalSpikeSystemProcessorTime', index=13,
      number=14, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='totalSpikeSystemIdleTime', full_name='OSXResourceUsage.totalSpikeSystemIdleTime', index=14,
      number=15, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numTimesSpikeBackgroundMemorySampled', full_name='OSXResourceUsage.numTimesSpikeBackgroundMemorySampled', index=15,
      number=16, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avgSpikePhysicalMemoryAvailable', full_name='OSXResourceUsage.avgSpikePhysicalMemoryAvailable', index=16,
      number=17, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numTimesMemorySampled', full_name='OSXResourceUsage.numTimesMemorySampled', index=17,
      number=18, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avgWorkingSetSize', full_name='OSXResourceUsage.avgWorkingSetSize', index=18,
      number=19, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avgPhysicalMemoryAvailable', full_name='OSXResourceUsage.avgPhysicalMemoryAvailable', index=19,
      number=20, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avgPhysicalMemoryTotal', full_name='OSXResourceUsage.avgPhysicalMemoryTotal', index=20,
      number=21, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imageFileMD5', full_name='OSXResourceUsage.imageFileMD5', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sentBytes', full_name='OSXResourceUsage.sentBytes', index=22,
      number=23, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='receivedBytes', full_name='OSXResourceUsage.receivedBytes', index=23,
      number=24, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='systemSentBytes', full_name='OSXResourceUsage.systemSentBytes', index=24,
      number=25, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='systemReceivedBytes', full_name='OSXResourceUsage.systemReceivedBytes', index=25,
      number=26, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='elapsedTime', full_name='OSXResourceUsage.elapsedTime', index=26,
      number=27, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numberSampledResponseTimes', full_name='OSXResourceUsage.numberSampledResponseTimes', index=27,
      number=28, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sumResponseTime', full_name='OSXResourceUsage.sumResponseTime', index=28,
      number=29, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spikeSentBytes', full_name='OSXResourceUsage.spikeSentBytes', index=29,
      number=30, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spikeReceivedBytes', full_name='OSXResourceUsage.spikeReceivedBytes', index=30,
      number=31, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spikeNetworkTimeSystem', full_name='OSXResourceUsage.spikeNetworkTimeSystem', index=31,
      number=32, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spikeSystemSentBytes', full_name='OSXResourceUsage.spikeSystemSentBytes', index=32,
      number=33, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spikesSystemReceivedBytes', full_name='OSXResourceUsage.spikesSystemReceivedBytes', index=33,
      number=34, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numTimesSpikeWorkingSetSampled', full_name='OSXResourceUsage.numTimesSpikeWorkingSetSampled', index=34,
      number=35, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spikeNetworkTimeForegroundProcess', full_name='OSXResourceUsage.spikeNetworkTimeForegroundProcess', index=35,
      number=36, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avgSpikeWorkingSetSize', full_name='OSXResourceUsage.avgSpikeWorkingSetSize', index=36,
      number=37, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='readTransferCount', full_name='OSXResourceUsage.readTransferCount', index=37,
      number=38, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='writeTransferCount', full_name='OSXResourceUsage.writeTransferCount', index=38,
      number=39, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='systemReadTransferCount', full_name='OSXResourceUsage.systemReadTransferCount', index=39,
      number=40, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='systemWriteTransferCount', full_name='OSXResourceUsage.systemWriteTransferCount', index=40,
      number=41, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spikeIOTimeForegroundProcess', full_name='OSXResourceUsage.spikeIOTimeForegroundProcess', index=41,
      number=42, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spikeReadTransferCount', full_name='OSXResourceUsage.spikeReadTransferCount', index=42,
      number=43, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spikeWriteTransferCount', full_name='OSXResourceUsage.spikeWriteTransferCount', index=43,
      number=44, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spikeIOTimeSystem', full_name='OSXResourceUsage.spikeIOTimeSystem', index=44,
      number=45, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spikeSystemReadTransferCount', full_name='OSXResourceUsage.spikeSystemReadTransferCount', index=45,
      number=46, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spikeSystemWriteTransferCount', full_name='OSXResourceUsage.spikeSystemWriteTransferCount', index=46,
      number=47, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='siteId', full_name='OSXResourceUsage.siteId', index=47,
      number=48, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='OSXResourceUsage.uuid', index=48,
      number=49, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=47,
  serialized_end=1555,
)

DESCRIPTOR.message_types_by_name['OSXResourceUsage'] = _OSXRESOURCEUSAGE

class OSXResourceUsage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OSXRESOURCEUSAGE

  # @@protoc_insertion_point(class_scope:OSXResourceUsage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\"com.ziften.server.protocol.messageB\027OSXResourceUsageMessage')
_OSXRESOURCEUSAGE.fields_by_name['timeStamp'].has_options = True
_OSXRESOURCEUSAGE.fields_by_name['timeStamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_OSXRESOURCEUSAGE.fields_by_name['agentGUID'].has_options = True
_OSXRESOURCEUSAGE.fields_by_name['agentGUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_OSXRESOURCEUSAGE.fields_by_name['uuid'].has_options = True
_OSXRESOURCEUSAGE.fields_by_name['uuid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
# @@protoc_insertion_point(module_scope)
