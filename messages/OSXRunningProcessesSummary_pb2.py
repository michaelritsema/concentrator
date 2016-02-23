# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OSXRunningProcessesSummary.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import PostgresType_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='OSXRunningProcessesSummary.proto',
  package='',
  serialized_pb='\n OSXRunningProcessesSummary.proto\x1a\x12PostgresType.proto\"\x98\x04\n\x1aOSXRunningProcessesSummary\x12 \n\ttimeStamp\x18\x01 \x02(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x1b\n\tagentGUID\x18\x02 \x02(\tB\x08\x82\xb5\x18\x04uuid\x12\x0e\n\x06siteId\x18\x03 \x01(\t\x12)\n\x12startMonitorPeriod\x18\x04 \x02(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\'\n\x10\x65ndMonitorPeriod\x18\x05 \x02(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x15\n\rimageFilepath\x18\x06 \x03(\t\x12\x14\n\x0cimageFileMD5\x18\x07 \x03(\t\x12 \n\tFirstSeen\x18\x08 \x03(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x1f\n\x08LastSeen\x18\t \x03(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x1f\n\x17NumInstancesSeenAtStart\x18\n \x03(\x05\x12%\n\x1dNumInstancesStillRunningAtEnd\x18\x0b \x03(\x05\x12!\n\x19NumInstancesCreatedDuring\x18\x0c \x03(\x05\x12$\n\x1cNumInstancesTerminatedDuring\x18\r \x03(\x05\x12\x13\n\x0b\x61\x63\x63ountName\x18\x0e \x03(\t\x12\x0e\n\x06\x64omain\x18\x0f \x03(\t\x12\x16\n\x04uuid\x18\x10 \x01(\tB\x08\x82\xb5\x18\x04uuid\x12\x19\n\x07rpsUUID\x18\x11 \x01(\tB\x08\x82\xb5\x18\x04uuidBG\n\"com.ziften.server.protocol.messageB!OSXRunningProcessesSummaryMessage')




_OSXRUNNINGPROCESSESSUMMARY = _descriptor.Descriptor(
  name='OSXRunningProcessesSummary',
  full_name='OSXRunningProcessesSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='OSXRunningProcessesSummary.timeStamp', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='agentGUID', full_name='OSXRunningProcessesSummary.agentGUID', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='siteId', full_name='OSXRunningProcessesSummary.siteId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='startMonitorPeriod', full_name='OSXRunningProcessesSummary.startMonitorPeriod', index=3,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='endMonitorPeriod', full_name='OSXRunningProcessesSummary.endMonitorPeriod', index=4,
      number=5, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='imageFilepath', full_name='OSXRunningProcessesSummary.imageFilepath', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imageFileMD5', full_name='OSXRunningProcessesSummary.imageFileMD5', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FirstSeen', full_name='OSXRunningProcessesSummary.FirstSeen', index=7,
      number=8, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='LastSeen', full_name='OSXRunningProcessesSummary.LastSeen', index=8,
      number=9, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='NumInstancesSeenAtStart', full_name='OSXRunningProcessesSummary.NumInstancesSeenAtStart', index=9,
      number=10, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='NumInstancesStillRunningAtEnd', full_name='OSXRunningProcessesSummary.NumInstancesStillRunningAtEnd', index=10,
      number=11, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='NumInstancesCreatedDuring', full_name='OSXRunningProcessesSummary.NumInstancesCreatedDuring', index=11,
      number=12, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='NumInstancesTerminatedDuring', full_name='OSXRunningProcessesSummary.NumInstancesTerminatedDuring', index=12,
      number=13, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accountName', full_name='OSXRunningProcessesSummary.accountName', index=13,
      number=14, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='domain', full_name='OSXRunningProcessesSummary.domain', index=14,
      number=15, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='OSXRunningProcessesSummary.uuid', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='rpsUUID', full_name='OSXRunningProcessesSummary.rpsUUID', index=16,
      number=17, type=9, cpp_type=9, label=1,
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
  serialized_start=57,
  serialized_end=593,
)

DESCRIPTOR.message_types_by_name['OSXRunningProcessesSummary'] = _OSXRUNNINGPROCESSESSUMMARY

class OSXRunningProcessesSummary(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OSXRUNNINGPROCESSESSUMMARY

  # @@protoc_insertion_point(class_scope:OSXRunningProcessesSummary)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\"com.ziften.server.protocol.messageB!OSXRunningProcessesSummaryMessage')
_OSXRUNNINGPROCESSESSUMMARY.fields_by_name['timeStamp'].has_options = True
_OSXRUNNINGPROCESSESSUMMARY.fields_by_name['timeStamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_OSXRUNNINGPROCESSESSUMMARY.fields_by_name['agentGUID'].has_options = True
_OSXRUNNINGPROCESSESSUMMARY.fields_by_name['agentGUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_OSXRUNNINGPROCESSESSUMMARY.fields_by_name['startMonitorPeriod'].has_options = True
_OSXRUNNINGPROCESSESSUMMARY.fields_by_name['startMonitorPeriod']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_OSXRUNNINGPROCESSESSUMMARY.fields_by_name['endMonitorPeriod'].has_options = True
_OSXRUNNINGPROCESSESSUMMARY.fields_by_name['endMonitorPeriod']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_OSXRUNNINGPROCESSESSUMMARY.fields_by_name['FirstSeen'].has_options = True
_OSXRUNNINGPROCESSESSUMMARY.fields_by_name['FirstSeen']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_OSXRUNNINGPROCESSESSUMMARY.fields_by_name['LastSeen'].has_options = True
_OSXRUNNINGPROCESSESSUMMARY.fields_by_name['LastSeen']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_OSXRUNNINGPROCESSESSUMMARY.fields_by_name['uuid'].has_options = True
_OSXRUNNINGPROCESSESSUMMARY.fields_by_name['uuid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_OSXRUNNINGPROCESSESSUMMARY.fields_by_name['rpsUUID'].has_options = True
_OSXRUNNINGPROCESSESSUMMARY.fields_by_name['rpsUUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
# @@protoc_insertion_point(module_scope)
