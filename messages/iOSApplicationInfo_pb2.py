# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iOSApplicationInfo.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import PostgresType_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='iOSApplicationInfo.proto',
  package='',
  serialized_pb='\n\x18iOSApplicationInfo.proto\x1a\x12PostgresType.proto\"\x96\x01\n\x12iOSApplicationInfo\x12\x11\n\ttimestamp\x18\x01 \x02(\x03\x12\x11\n\tagentGUID\x18\x02 \x02(\t\x12\x0c\n\x04name\x18\x03 \x02(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\x12\x13\n\x0bisInstalled\x18\x05 \x02(\x05\x12\x0e\n\x06siteId\x18\x06 \x01(\t\x12\x16\n\x04uuid\x18\x07 \x01(\tB\x08\x82\xb5\x18\x04uuidB?\n\"com.ziften.server.protocol.messageB\x19iOSApplicationInfoMessage')




_IOSAPPLICATIONINFO = _descriptor.Descriptor(
  name='iOSApplicationInfo',
  full_name='iOSApplicationInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='iOSApplicationInfo.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='agentGUID', full_name='iOSApplicationInfo.agentGUID', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='iOSApplicationInfo.name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='iOSApplicationInfo.version', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isInstalled', full_name='iOSApplicationInfo.isInstalled', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='siteId', full_name='iOSApplicationInfo.siteId', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='iOSApplicationInfo.uuid', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=49,
  serialized_end=199,
)

DESCRIPTOR.message_types_by_name['iOSApplicationInfo'] = _IOSAPPLICATIONINFO

class iOSApplicationInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _IOSAPPLICATIONINFO

  # @@protoc_insertion_point(class_scope:iOSApplicationInfo)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\"com.ziften.server.protocol.messageB\031iOSApplicationInfoMessage')
_IOSAPPLICATIONINFO.fields_by_name['uuid'].has_options = True
_IOSAPPLICATIONINFO.fields_by_name['uuid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
# @@protoc_insertion_point(module_scope)
