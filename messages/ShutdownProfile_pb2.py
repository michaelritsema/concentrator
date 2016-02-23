# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ShutdownProfile.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import PostgresType_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ShutdownProfile.proto',
  package='',
  serialized_pb='\n\x15ShutdownProfile.proto\x1a\x12PostgresType.proto\"\x91\x01\n\x0fShutdownProfile\x12 \n\ttimeStamp\x18\x01 \x02(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x1b\n\tagentGUID\x18\x02 \x02(\tB\x08\x82\xb5\x18\x04uuid\x12\x17\n\x0f\x62ootSpanInTicks\x18\x03 \x02(\x03\x12\x0e\n\x06siteId\x18\x04 \x01(\t\x12\x16\n\x04uuid\x18\x05 \x01(\tB\x08\x82\xb5\x18\x04uuidB<\n\"com.ziften.server.protocol.messageB\x16ShutdownProfileMessage')




_SHUTDOWNPROFILE = _descriptor.Descriptor(
  name='ShutdownProfile',
  full_name='ShutdownProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='ShutdownProfile.timeStamp', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='agentGUID', full_name='ShutdownProfile.agentGUID', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='bootSpanInTicks', full_name='ShutdownProfile.bootSpanInTicks', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='siteId', full_name='ShutdownProfile.siteId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='ShutdownProfile.uuid', index=4,
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
  serialized_start=46,
  serialized_end=191,
)

DESCRIPTOR.message_types_by_name['ShutdownProfile'] = _SHUTDOWNPROFILE

class ShutdownProfile(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SHUTDOWNPROFILE

  # @@protoc_insertion_point(class_scope:ShutdownProfile)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\"com.ziften.server.protocol.messageB\026ShutdownProfileMessage')
_SHUTDOWNPROFILE.fields_by_name['timeStamp'].has_options = True
_SHUTDOWNPROFILE.fields_by_name['timeStamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_SHUTDOWNPROFILE.fields_by_name['agentGUID'].has_options = True
_SHUTDOWNPROFILE.fields_by_name['agentGUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_SHUTDOWNPROFILE.fields_by_name['uuid'].has_options = True
_SHUTDOWNPROFILE.fields_by_name['uuid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
# @@protoc_insertion_point(module_scope)
