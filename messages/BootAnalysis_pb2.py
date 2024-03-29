# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BootAnalysis.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import PostgresType_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='BootAnalysis.proto',
  package='',
  serialized_pb='\n\x12\x42ootAnalysis.proto\x1a\x12PostgresType.proto\"\xd9\x03\n\x0c\x42ootAnalysis\x12 \n\ttimeStamp\x18\x01 \x02(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x1b\n\tagentGUID\x18\x02 \x02(\tB\x08\x82\xb5\x18\x04uuid\x12\x1e\n\x0c\x61nalysisGUID\x18\x03 \x02(\tB\x08\x82\xb5\x18\x04uuid\x12%\n\x0e\x65ventTimeStamp\x18\x04 \x03(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x11\n\teventType\x18\x05 \x03(\x05\x12\x11\n\tprocessId\x18\x06 \x03(\x05\x12\x17\n\x0fparentProcessId\x18\x07 \x03(\x05\x12\x15\n\rimageFileName\x18\x08 \x03(\t\x12\x13\n\x0b\x63ommandLine\x18\t \x03(\t\x12\x15\n\rimageFilepath\x18\n \x03(\t\x12\x14\n\x0cimageFileMD5\x18\x0b \x03(\t\x12\x13\n\x0b\x61\x63\x63ountName\x18\x0c \x03(\t\x12\x12\n\ndomainName\x18\r \x03(\t\x12\x0e\n\x06siteId\x18\x0e \x01(\t\x12\x16\n\x0e\x65xecutionCount\x18\x0f \x03(\x05\x12\x16\n\x04uuid\x18\x10 \x01(\tB\x08\x82\xb5\x18\x04uuid\x12\x1d\n\x0bprocessUUID\x18\x11 \x03(\tB\x08\x82\xb5\x18\x04uuid\x12#\n\x11parentProcessUUID\x18\x12 \x03(\tB\x08\x82\xb5\x18\x04uuidB9\n\"com.ziften.server.protocol.messageB\x13\x42ootAnalysisMessage')




_BOOTANALYSIS = _descriptor.Descriptor(
  name='BootAnalysis',
  full_name='BootAnalysis',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='BootAnalysis.timeStamp', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='agentGUID', full_name='BootAnalysis.agentGUID', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='analysisGUID', full_name='BootAnalysis.analysisGUID', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='eventTimeStamp', full_name='BootAnalysis.eventTimeStamp', index=3,
      number=4, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='eventType', full_name='BootAnalysis.eventType', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='processId', full_name='BootAnalysis.processId', index=5,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parentProcessId', full_name='BootAnalysis.parentProcessId', index=6,
      number=7, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imageFileName', full_name='BootAnalysis.imageFileName', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='commandLine', full_name='BootAnalysis.commandLine', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imageFilepath', full_name='BootAnalysis.imageFilepath', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imageFileMD5', full_name='BootAnalysis.imageFileMD5', index=10,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accountName', full_name='BootAnalysis.accountName', index=11,
      number=12, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='domainName', full_name='BootAnalysis.domainName', index=12,
      number=13, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='siteId', full_name='BootAnalysis.siteId', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='executionCount', full_name='BootAnalysis.executionCount', index=14,
      number=15, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='BootAnalysis.uuid', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='processUUID', full_name='BootAnalysis.processUUID', index=16,
      number=17, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='parentProcessUUID', full_name='BootAnalysis.parentProcessUUID', index=17,
      number=18, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=43,
  serialized_end=516,
)

DESCRIPTOR.message_types_by_name['BootAnalysis'] = _BOOTANALYSIS

class BootAnalysis(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BOOTANALYSIS

  # @@protoc_insertion_point(class_scope:BootAnalysis)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\"com.ziften.server.protocol.messageB\023BootAnalysisMessage')
_BOOTANALYSIS.fields_by_name['timeStamp'].has_options = True
_BOOTANALYSIS.fields_by_name['timeStamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_BOOTANALYSIS.fields_by_name['agentGUID'].has_options = True
_BOOTANALYSIS.fields_by_name['agentGUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_BOOTANALYSIS.fields_by_name['analysisGUID'].has_options = True
_BOOTANALYSIS.fields_by_name['analysisGUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_BOOTANALYSIS.fields_by_name['eventTimeStamp'].has_options = True
_BOOTANALYSIS.fields_by_name['eventTimeStamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_BOOTANALYSIS.fields_by_name['uuid'].has_options = True
_BOOTANALYSIS.fields_by_name['uuid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_BOOTANALYSIS.fields_by_name['processUUID'].has_options = True
_BOOTANALYSIS.fields_by_name['processUUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_BOOTANALYSIS.fields_by_name['parentProcessUUID'].has_options = True
_BOOTANALYSIS.fields_by_name['parentProcessUUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
# @@protoc_insertion_point(module_scope)
