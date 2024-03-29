# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: IpfixEncapsulation.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import PostgresType_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='IpfixEncapsulation.proto',
  package='',
  serialized_pb='\n\x18IpfixEncapsulation.proto\x1a\x12PostgresType.proto\"\xa5\x01\n\x12IpfixEncapsulation\x12 \n\ttimeStamp\x18\x01 \x02(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x1b\n\tagentGUID\x18\x02 \x02(\tB\x08\x82\xb5\x18\x04uuid\x12(\n\x0cipfixMessage\x18\x03 \x03(\x0c\x42\x12\x82\xb5\x18\x0elong varbinary\x12\x0e\n\x06siteId\x18\x04 \x01(\t\x12\x16\n\x04uuid\x18\x05 \x01(\tB\x08\x82\xb5\x18\x04uuidB?\n\"com.ziften.server.protocol.messageB\x19IpfixEncapsulationMessage')




_IPFIXENCAPSULATION = _descriptor.Descriptor(
  name='IpfixEncapsulation',
  full_name='IpfixEncapsulation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='IpfixEncapsulation.timeStamp', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='agentGUID', full_name='IpfixEncapsulation.agentGUID', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='ipfixMessage', full_name='IpfixEncapsulation.ipfixMessage', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\016long varbinary')),
    _descriptor.FieldDescriptor(
      name='siteId', full_name='IpfixEncapsulation.siteId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='IpfixEncapsulation.uuid', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_end=214,
)

DESCRIPTOR.message_types_by_name['IpfixEncapsulation'] = _IPFIXENCAPSULATION

class IpfixEncapsulation(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _IPFIXENCAPSULATION

  # @@protoc_insertion_point(class_scope:IpfixEncapsulation)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\"com.ziften.server.protocol.messageB\031IpfixEncapsulationMessage')
_IPFIXENCAPSULATION.fields_by_name['timeStamp'].has_options = True
_IPFIXENCAPSULATION.fields_by_name['timeStamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_IPFIXENCAPSULATION.fields_by_name['agentGUID'].has_options = True
_IPFIXENCAPSULATION.fields_by_name['agentGUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_IPFIXENCAPSULATION.fields_by_name['ipfixMessage'].has_options = True
_IPFIXENCAPSULATION.fields_by_name['ipfixMessage']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\016long varbinary')
_IPFIXENCAPSULATION.fields_by_name['uuid'].has_options = True
_IPFIXENCAPSULATION.fields_by_name['uuid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
# @@protoc_insertion_point(module_scope)
