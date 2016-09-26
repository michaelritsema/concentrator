# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ProcessModuleLoad.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import PostgresType_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ProcessModuleLoad.proto',
  package='',
  serialized_pb='\n\x17ProcessModuleLoad.proto\x1a\x12PostgresType.proto\"\xd4\x01\n\x11ProcessModuleLoad\x12 \n\ttimeStamp\x18\x01 \x02(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x1b\n\tagentGUID\x18\x02 \x02(\tB\x08\x82\xb5\x18\x04uuid\x12\x18\n\x10processImagePath\x18\x03 \x02(\t\x12\x12\n\nprocessMD5\x18\x04 \x02(\t\x12\x17\n\x0fmoduleImagePath\x18\x05 \x02(\t\x12\x11\n\tmoduleMD5\x18\x06 \x02(\t\x12\x0e\n\x06siteId\x18\x07 \x01(\t\x12\x16\n\x04uuid\x18\x08 \x01(\tB\x08\x82\xb5\x18\x04uuidB>\n\"com.ziften.server.protocol.messageB\x18ProcessModuleLoadMessage')




_PROCESSMODULELOAD = _descriptor.Descriptor(
  name='ProcessModuleLoad',
  full_name='ProcessModuleLoad',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='ProcessModuleLoad.timeStamp', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='agentGUID', full_name='ProcessModuleLoad.agentGUID', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='processImagePath', full_name='ProcessModuleLoad.processImagePath', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='processMD5', full_name='ProcessModuleLoad.processMD5', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='moduleImagePath', full_name='ProcessModuleLoad.moduleImagePath', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='moduleMD5', full_name='ProcessModuleLoad.moduleMD5', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='siteId', full_name='ProcessModuleLoad.siteId', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='ProcessModuleLoad.uuid', index=7,
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
  serialized_start=48,
  serialized_end=260,
)

DESCRIPTOR.message_types_by_name['ProcessModuleLoad'] = _PROCESSMODULELOAD

class ProcessModuleLoad(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PROCESSMODULELOAD

  # @@protoc_insertion_point(class_scope:ProcessModuleLoad)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\"com.ziften.server.protocol.messageB\030ProcessModuleLoadMessage')
_PROCESSMODULELOAD.fields_by_name['timeStamp'].has_options = True
_PROCESSMODULELOAD.fields_by_name['timeStamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_PROCESSMODULELOAD.fields_by_name['agentGUID'].has_options = True
_PROCESSMODULELOAD.fields_by_name['agentGUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_PROCESSMODULELOAD.fields_by_name['uuid'].has_options = True
_PROCESSMODULELOAD.fields_by_name['uuid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
# @@protoc_insertion_point(module_scope)