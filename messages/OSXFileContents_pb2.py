# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OSXFileContents.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import PostgresType_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='OSXFileContents.proto',
  package='',
  serialized_pb='\n\x15OSXFileContents.proto\x1a\x12PostgresType.proto\"\xc0\x02\n\x0fOSXFileContents\x12 \n\ttimeStamp\x18\x01 \x02(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x1b\n\tagentGUID\x18\x02 \x02(\tB\x08\x82\xb5\x18\x04uuid\x12\x15\n\rimageFilePath\x18\x03 \x02(\t\x12\x32\n\x0c\x66ileContents\x18\x04 \x02(\x0c\x42\x1c\x82\xb5\x18\x18long varbinary(32000000)\x12\x18\n\x10\x43reatedTimeStamp\x18\x05 \x01(\x03\x12\x19\n\x11ModifiedTimeStamp\x18\x06 \x01(\x03\x12\x14\n\x0cimageFileMD5\x18\x07 \x02(\t\x12\x19\n\x11\x63ommandIdentifier\x18\x08 \x02(\x04\x12\x0e\n\x06siteId\x18\t \x01(\t\x12\x16\n\x04uuid\x18\n \x01(\tB\x08\x82\xb5\x18\x04uuid\x12\x15\n\nretryCount\x18\x0b \x01(\x05:\x01\x30\x42<\n\"com.ziften.server.protocol.messageB\x16OSXFileContentsMessage')




_OSXFILECONTENTS = _descriptor.Descriptor(
  name='OSXFileContents',
  full_name='OSXFileContents',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='OSXFileContents.timeStamp', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='agentGUID', full_name='OSXFileContents.agentGUID', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='imageFilePath', full_name='OSXFileContents.imageFilePath', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fileContents', full_name='OSXFileContents.fileContents', index=3,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\030long varbinary(32000000)')),
    _descriptor.FieldDescriptor(
      name='CreatedTimeStamp', full_name='OSXFileContents.CreatedTimeStamp', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ModifiedTimeStamp', full_name='OSXFileContents.ModifiedTimeStamp', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imageFileMD5', full_name='OSXFileContents.imageFileMD5', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='commandIdentifier', full_name='OSXFileContents.commandIdentifier', index=7,
      number=8, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='siteId', full_name='OSXFileContents.siteId', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='OSXFileContents.uuid', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='retryCount', full_name='OSXFileContents.retryCount', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
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
  serialized_start=46,
  serialized_end=366,
)

DESCRIPTOR.message_types_by_name['OSXFileContents'] = _OSXFILECONTENTS

class OSXFileContents(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OSXFILECONTENTS

  # @@protoc_insertion_point(class_scope:OSXFileContents)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\"com.ziften.server.protocol.messageB\026OSXFileContentsMessage')
_OSXFILECONTENTS.fields_by_name['timeStamp'].has_options = True
_OSXFILECONTENTS.fields_by_name['timeStamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_OSXFILECONTENTS.fields_by_name['agentGUID'].has_options = True
_OSXFILECONTENTS.fields_by_name['agentGUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_OSXFILECONTENTS.fields_by_name['fileContents'].has_options = True
_OSXFILECONTENTS.fields_by_name['fileContents']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\030long varbinary(32000000)')
_OSXFILECONTENTS.fields_by_name['uuid'].has_options = True
_OSXFILECONTENTS.fields_by_name['uuid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
# @@protoc_insertion_point(module_scope)
