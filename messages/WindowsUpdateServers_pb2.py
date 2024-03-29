# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WindowsUpdateServers.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import PostgresType_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WindowsUpdateServers.proto',
  package='',
  serialized_pb='\n\x1aWindowsUpdateServers.proto\x1a\x12PostgresType.proto\"\xdb\x01\n\x14WindowsUpdateServers\x12 \n\ttimeStamp\x18\x01 \x02(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x1b\n\tagentGUID\x18\x02 \x02(\tB\x08\x82\xb5\x18\x04uuid\x12\x17\n\x0fWUA_ServersGUID\x18\x03 \x02(\t\x12\x10\n\x08serverID\x18\x04 \x03(\t\x12\x12\n\nserverName\x18\x05 \x03(\t\x12\x0e\n\x06siteId\x18\x06 \x01(\t\x12\x16\n\x04uuid\x18\x07 \x01(\tB\x08\x82\xb5\x18\x04uuid\x12\x1d\n\x0bwuaScanUUID\x18\x08 \x01(\tB\x08\x82\xb5\x18\x04uuidBA\n\"com.ziften.server.protocol.messageB\x1bWindowsUpdateServersMessage')




_WINDOWSUPDATESERVERS = _descriptor.Descriptor(
  name='WindowsUpdateServers',
  full_name='WindowsUpdateServers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='WindowsUpdateServers.timeStamp', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='agentGUID', full_name='WindowsUpdateServers.agentGUID', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='WUA_ServersGUID', full_name='WindowsUpdateServers.WUA_ServersGUID', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serverID', full_name='WindowsUpdateServers.serverID', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serverName', full_name='WindowsUpdateServers.serverName', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='siteId', full_name='WindowsUpdateServers.siteId', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='WindowsUpdateServers.uuid', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='wuaScanUUID', full_name='WindowsUpdateServers.wuaScanUUID', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=51,
  serialized_end=270,
)

DESCRIPTOR.message_types_by_name['WindowsUpdateServers'] = _WINDOWSUPDATESERVERS

class WindowsUpdateServers(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WINDOWSUPDATESERVERS

  # @@protoc_insertion_point(class_scope:WindowsUpdateServers)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\"com.ziften.server.protocol.messageB\033WindowsUpdateServersMessage')
_WINDOWSUPDATESERVERS.fields_by_name['timeStamp'].has_options = True
_WINDOWSUPDATESERVERS.fields_by_name['timeStamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_WINDOWSUPDATESERVERS.fields_by_name['agentGUID'].has_options = True
_WINDOWSUPDATESERVERS.fields_by_name['agentGUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_WINDOWSUPDATESERVERS.fields_by_name['uuid'].has_options = True
_WINDOWSUPDATESERVERS.fields_by_name['uuid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_WINDOWSUPDATESERVERS.fields_by_name['wuaScanUUID'].has_options = True
_WINDOWSUPDATESERVERS.fields_by_name['wuaScanUUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
# @@protoc_insertion_point(module_scope)
