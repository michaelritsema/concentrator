# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BootInfo.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = _descriptor.FileDescriptor(
  name='BootInfo.proto',
  package='',
  serialized_pb='\n\x0e\x42ootInfo.proto\x1a\x12PostgresType.proto\"\xbf\x02\n\x08\x42ootInfo\x12 \n\ttimeStamp\x18\x01 \x02(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x1b\n\tagentGUID\x18\x02 \x02(\tB\x08\x82\xb5\x18\x04uuid\x12\x1e\n\x0c\x61nalysisGUID\x18\x03 \x02(\tB\x08\x82\xb5\x18\x04uuid\x12\'\n\x10sessionStartTime\x18\x04 \x02(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x1d\n\x15sessionStartTimeTicks\x18\x05 \x02(\x03\x12&\n\x1eProcessTimeAtSessionStartTicks\x18\x06 \x02(\x03\x12\"\n\x0b\x62ootEndTime\x18\x07 \x02(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x18\n\x10\x62ootEndTimeTicks\x18\x08 \x02(\x03\x12\x0e\n\x06siteId\x18\t \x01(\t\x12\x16\n\x04uuid\x18\n \x01(\tB\x08\x82\xb5\x18\x04uuidB5\n\"com.ziften.server.protocol.messageB\x0f\x42ootInfoMessage')




_BOOTINFO = _descriptor.Descriptor(
  name='BootInfo',
  full_name='BootInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='BootInfo.timeStamp', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='agentGUID', full_name='BootInfo.agentGUID', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='analysisGUID', full_name='BootInfo.analysisGUID', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='sessionStartTime', full_name='BootInfo.sessionStartTime', index=3,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='sessionStartTimeTicks', full_name='BootInfo.sessionStartTimeTicks', index=4,
      number=5, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ProcessTimeAtSessionStartTicks', full_name='BootInfo.ProcessTimeAtSessionStartTicks', index=5,
      number=6, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bootEndTime', full_name='BootInfo.bootEndTime', index=6,
      number=7, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='bootEndTimeTicks', full_name='BootInfo.bootEndTimeTicks', index=7,
      number=8, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='siteId', full_name='BootInfo.siteId', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='BootInfo.uuid', index=9,
      number=10, type=9, cpp_type=9, label=1,
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
  serialized_start=39,
  serialized_end=358,
)

DESCRIPTOR.message_types_by_name['BootInfo'] = _BOOTINFO

class BootInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BOOTINFO

  # @@protoc_insertion_point(class_scope:BootInfo)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\"com.ziften.server.protocol.messageB\017BootInfoMessage')
_BOOTINFO.fields_by_name['timeStamp'].has_options = True
_BOOTINFO.fields_by_name['timeStamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_BOOTINFO.fields_by_name['agentGUID'].has_options = True
_BOOTINFO.fields_by_name['agentGUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_BOOTINFO.fields_by_name['analysisGUID'].has_options = True
_BOOTINFO.fields_by_name['analysisGUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_BOOTINFO.fields_by_name['sessionStartTime'].has_options = True
_BOOTINFO.fields_by_name['sessionStartTime']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_BOOTINFO.fields_by_name['bootEndTime'].has_options = True
_BOOTINFO.fields_by_name['bootEndTime']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_BOOTINFO.fields_by_name['uuid'].has_options = True
_BOOTINFO.fields_by_name['uuid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
# @@protoc_insertion_point(module_scope)
