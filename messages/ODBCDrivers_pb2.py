# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ODBCDrivers.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import PostgresType_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ODBCDrivers.proto',
  package='',
  serialized_pb='\n\x11ODBCDrivers.proto\x1a\x12PostgresType.proto\"\xcd\x01\n\x0bODBCDrivers\x12 \n\ttimeStamp\x18\x01 \x02(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x1b\n\tagentGUID\x18\x02 \x02(\tB\x08\x82\xb5\x18\x04uuid\x12\x0c\n\x04Name\x18\x03 \x03(\t\x12\x10\n\x08\x61piLevel\x18\x04 \x03(\t\x12\x10\n\x08sqlLevel\x18\x05 \x03(\t\x12\x15\n\rDriverODBCVer\x18\x06 \x03(\t\x12\x13\n\x0bPoolTimeout\x18\x07 \x03(\t\x12\x11\n\tImagePath\x18\x08 \x03(\t\x12\x0e\n\x06siteId\x18\t \x01(\tB8\n\"com.ziften.server.protocol.messageB\x12ODBCDriversMessage')




_ODBCDRIVERS = _descriptor.Descriptor(
  name='ODBCDrivers',
  full_name='ODBCDrivers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='ODBCDrivers.timeStamp', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='agentGUID', full_name='ODBCDrivers.agentGUID', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='Name', full_name='ODBCDrivers.Name', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='apiLevel', full_name='ODBCDrivers.apiLevel', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sqlLevel', full_name='ODBCDrivers.sqlLevel', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DriverODBCVer', full_name='ODBCDrivers.DriverODBCVer', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PoolTimeout', full_name='ODBCDrivers.PoolTimeout', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ImagePath', full_name='ODBCDrivers.ImagePath', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='siteId', full_name='ODBCDrivers.siteId', index=8,
      number=9, type=9, cpp_type=9, label=1,
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
  serialized_start=42,
  serialized_end=247,
)

DESCRIPTOR.message_types_by_name['ODBCDrivers'] = _ODBCDRIVERS

class ODBCDrivers(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ODBCDRIVERS

  # @@protoc_insertion_point(class_scope:ODBCDrivers)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\"com.ziften.server.protocol.messageB\022ODBCDriversMessage')
_ODBCDRIVERS.fields_by_name['timeStamp'].has_options = True
_ODBCDRIVERS.fields_by_name['timeStamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_ODBCDRIVERS.fields_by_name['agentGUID'].has_options = True
_ODBCDRIVERS.fields_by_name['agentGUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
# @@protoc_insertion_point(module_scope)
