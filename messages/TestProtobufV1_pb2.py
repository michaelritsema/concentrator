# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TestProtobufV1.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='TestProtobufV1.proto',
  package='',
  serialized_pb='\n\x14TestProtobufV1.proto\",\n\x0eTestProtobufV1\x12\x0c\n\x04num1\x18\x01 \x02(\x03\x12\x0c\n\x04str1\x18\x02 \x02(\tB;\n\"com.ziften.server.protocol.messageB\x15TestProtobufV1Message')




_TESTPROTOBUFV1 = _descriptor.Descriptor(
  name='TestProtobufV1',
  full_name='TestProtobufV1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num1', full_name='TestProtobufV1.num1', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='str1', full_name='TestProtobufV1.str1', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  serialized_start=24,
  serialized_end=68,
)

DESCRIPTOR.message_types_by_name['TestProtobufV1'] = _TESTPROTOBUFV1

class TestProtobufV1(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TESTPROTOBUFV1

  # @@protoc_insertion_point(class_scope:TestProtobufV1)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\"com.ziften.server.protocol.messageB\025TestProtobufV1Message')
# @@protoc_insertion_point(module_scope)
