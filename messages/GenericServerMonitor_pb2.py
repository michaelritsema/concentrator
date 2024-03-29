# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GenericServerMonitor.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import PostgresType_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='GenericServerMonitor.proto',
  package='',
  serialized_pb='\n\x1aGenericServerMonitor.proto\x1a\x12PostgresType.proto\"\xd3\x03\n\x14GenericServerMonitor\x12 \n\ttimeStamp\x18\x01 \x02(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x1b\n\tagentGUID\x18\x02 \x02(\tB\x08\x82\xb5\x18\x04uuid\x12\x0e\n\x06siteId\x18\x03 \x01(\t\x12\x0f\n\x07logfile\x18\x04 \x02(\t\x12\x10\n\x08severity\x18\x05 \x02(\x05\x12\x0f\n\x07\x65ventId\x18\x06 \x02(\t\x12\x0c\n\x04tag0\x18\x07 \x01(\t\x12\x0c\n\x04tag1\x18\x08 \x01(\t\x12\x0c\n\x04tag2\x18\t \x01(\t\x12\x0c\n\x04tag3\x18\n \x01(\t\x12\x0c\n\x04tag4\x18\x0b \x01(\t\x12\x0c\n\x04tag5\x18\x0c \x01(\t\x12\x0c\n\x04tag6\x18\r \x01(\t\x12\x0c\n\x04tag7\x18\x0e \x01(\t\x12\x0c\n\x04tag8\x18\x0f \x01(\t\x12\x0c\n\x04tag9\x18\x10 \x01(\t\x12\x16\n\x04uuid\x18\x11 \x01(\tB\x08\x82\xb5\x18\x04uuid\x12\r\n\x05tag10\x18\x12 \x01(\t\x12\r\n\x05tag11\x18\x13 \x01(\t\x12\r\n\x05tag12\x18\x14 \x01(\t\x12\r\n\x05tag13\x18\x15 \x01(\t\x12\r\n\x05tag14\x18\x16 \x01(\t\x12\r\n\x05tag15\x18\x17 \x01(\t\x12\r\n\x05tag16\x18\x18 \x01(\t\x12\r\n\x05tag17\x18\x19 \x01(\t\x12\r\n\x05tag18\x18\x1a \x01(\t\x12\r\n\x05tag19\x18\x1b \x01(\tBA\n\"com.ziften.server.protocol.messageB\x1bGenericServerMonitorMessage')




_GENERICSERVERMONITOR = _descriptor.Descriptor(
  name='GenericServerMonitor',
  full_name='GenericServerMonitor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='GenericServerMonitor.timeStamp', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='agentGUID', full_name='GenericServerMonitor.agentGUID', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='siteId', full_name='GenericServerMonitor.siteId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='logfile', full_name='GenericServerMonitor.logfile', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='severity', full_name='GenericServerMonitor.severity', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eventId', full_name='GenericServerMonitor.eventId', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag0', full_name='GenericServerMonitor.tag0', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag1', full_name='GenericServerMonitor.tag1', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag2', full_name='GenericServerMonitor.tag2', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag3', full_name='GenericServerMonitor.tag3', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag4', full_name='GenericServerMonitor.tag4', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag5', full_name='GenericServerMonitor.tag5', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag6', full_name='GenericServerMonitor.tag6', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag7', full_name='GenericServerMonitor.tag7', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag8', full_name='GenericServerMonitor.tag8', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag9', full_name='GenericServerMonitor.tag9', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='GenericServerMonitor.uuid', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='tag10', full_name='GenericServerMonitor.tag10', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag11', full_name='GenericServerMonitor.tag11', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag12', full_name='GenericServerMonitor.tag12', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag13', full_name='GenericServerMonitor.tag13', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag14', full_name='GenericServerMonitor.tag14', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag15', full_name='GenericServerMonitor.tag15', index=22,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag16', full_name='GenericServerMonitor.tag16', index=23,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag17', full_name='GenericServerMonitor.tag17', index=24,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag18', full_name='GenericServerMonitor.tag18', index=25,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag19', full_name='GenericServerMonitor.tag19', index=26,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=51,
  serialized_end=518,
)

DESCRIPTOR.message_types_by_name['GenericServerMonitor'] = _GENERICSERVERMONITOR

class GenericServerMonitor(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GENERICSERVERMONITOR

  # @@protoc_insertion_point(class_scope:GenericServerMonitor)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\"com.ziften.server.protocol.messageB\033GenericServerMonitorMessage')
_GENERICSERVERMONITOR.fields_by_name['timeStamp'].has_options = True
_GENERICSERVERMONITOR.fields_by_name['timeStamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_GENERICSERVERMONITOR.fields_by_name['agentGUID'].has_options = True
_GENERICSERVERMONITOR.fields_by_name['agentGUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_GENERICSERVERMONITOR.fields_by_name['uuid'].has_options = True
_GENERICSERVERMONITOR.fields_by_name['uuid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
# @@protoc_insertion_point(module_scope)
