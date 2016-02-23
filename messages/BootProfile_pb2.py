# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BootProfile.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import PostgresType_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='BootProfile.proto',
  package='',
  serialized_pb='\n\x11\x42ootProfile.proto\x1a\x12PostgresType.proto\"\xf4\x01\n\x0b\x42ootProfile\x12 \n\ttimeStamp\x18\x01 \x02(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x1b\n\tagentGUID\x18\x02 \x02(\tB\x08\x82\xb5\x18\x04uuid\x12\x10\n\x08\x62ootTime\x18\x03 \x02(\x03\x12\x11\n\tloginTime\x18\x04 \x01(\x03\x12\x1e\n\x0c\x61nalysisGUID\x18\x05 \x01(\tB\x08\x82\xb5\x18\x04uuid\x12\x13\n\x0bpresmssTime\x18\x06 \x01(\x03\x12\x0e\n\x06siteId\x18\x07 \x01(\t\x12$\n\rbootStartTime\x18\x08 \x01(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x16\n\x04uuid\x18\t \x01(\tB\x08\x82\xb5\x18\x04uuidB8\n\"com.ziften.server.protocol.messageB\x12\x42ootProfileMessage')




_BOOTPROFILE = _descriptor.Descriptor(
  name='BootProfile',
  full_name='BootProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='BootProfile.timeStamp', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='agentGUID', full_name='BootProfile.agentGUID', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='bootTime', full_name='BootProfile.bootTime', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='loginTime', full_name='BootProfile.loginTime', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='analysisGUID', full_name='BootProfile.analysisGUID', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='presmssTime', full_name='BootProfile.presmssTime', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='siteId', full_name='BootProfile.siteId', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bootStartTime', full_name='BootProfile.bootStartTime', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='BootProfile.uuid', index=8,
      number=9, type=9, cpp_type=9, label=1,
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
  serialized_start=42,
  serialized_end=286,
)

DESCRIPTOR.message_types_by_name['BootProfile'] = _BOOTPROFILE

class BootProfile(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BOOTPROFILE

  # @@protoc_insertion_point(class_scope:BootProfile)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\"com.ziften.server.protocol.messageB\022BootProfileMessage')
_BOOTPROFILE.fields_by_name['timeStamp'].has_options = True
_BOOTPROFILE.fields_by_name['timeStamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_BOOTPROFILE.fields_by_name['agentGUID'].has_options = True
_BOOTPROFILE.fields_by_name['agentGUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_BOOTPROFILE.fields_by_name['analysisGUID'].has_options = True
_BOOTPROFILE.fields_by_name['analysisGUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_BOOTPROFILE.fields_by_name['bootStartTime'].has_options = True
_BOOTPROFILE.fields_by_name['bootStartTime']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_BOOTPROFILE.fields_by_name['uuid'].has_options = True
_BOOTPROFILE.fields_by_name['uuid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
# @@protoc_insertion_point(module_scope)
