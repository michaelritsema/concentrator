# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TestProtobufV2.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='TestProtobufV2.proto',
  package='',
  serialized_pb='\n\x14TestProtobufV2.proto\"N\n\x0eTestProtobufV2\x12\x0c\n\x04num1\x18\x01 \x02(\x03\x12\x0c\n\x04str1\x18\x02 \x02(\t\x12\x0f\n\x07newStr2\x18\x03 \x01(\t\x12\x0f\n\x07newNum2\x18\x04 \x01(\x03\x42;\n\"com.ziften.server.protocol.messageB\x15TestProtobufV2Message')




_TESTPROTOBUFV2 = _descriptor.Descriptor(
  name='TestProtobufV2',
  full_name='TestProtobufV2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num1', full_name='TestProtobufV2.num1', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='str1', full_name='TestProtobufV2.str1', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='newStr2', full_name='TestProtobufV2.newStr2', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='newNum2', full_name='TestProtobufV2.newNum2', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=24,
  serialized_end=102,
)

DESCRIPTOR.message_types_by_name['TestProtobufV2'] = _TESTPROTOBUFV2

class TestProtobufV2(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TESTPROTOBUFV2

  # @@protoc_insertion_point(class_scope:TestProtobufV2)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\"com.ziften.server.protocol.messageB\025TestProtobufV2Message')
# @@protoc_insertion_point(module_scope)
