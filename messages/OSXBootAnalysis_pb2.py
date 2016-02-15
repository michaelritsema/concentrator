# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OSXBootAnalysis.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = _descriptor.FileDescriptor(
  name='OSXBootAnalysis.proto',
  package='',
  serialized_pb='\n\x15OSXBootAnalysis.proto\x1a\x12PostgresType.proto\"\xd7\x02\n\x0fOSXBootAnalysis\x12 \n\ttimeStamp\x18\x01 \x02(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x1b\n\tagentGUID\x18\x02 \x02(\tB\x08\x82\xb5\x18\x04uuid\x12\x1e\n\x0c\x61nalysisGUID\x18\x03 \x02(\tB\x08\x82\xb5\x18\x04uuid\x12%\n\x0e\x65ventTimeStamp\x18\x04 \x03(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x11\n\teventType\x18\x05 \x03(\x05\x12\x11\n\tprocessId\x18\x06 \x03(\x05\x12\x17\n\x0fparentProcessId\x18\x07 \x03(\x05\x12\x15\n\rimageFileName\x18\x08 \x03(\t\x12\x13\n\x0b\x63ommandLine\x18\t \x03(\t\x12\x15\n\rimageFilepath\x18\n \x03(\t\x12\x14\n\x0cimageFileMD5\x18\x0b \x03(\t\x12\x0e\n\x06siteId\x18\x0c \x01(\t\x12\x16\n\x04uuid\x18\r \x01(\tB\x08\x82\xb5\x18\x04uuidB<\n\"com.ziften.server.protocol.messageB\x16OSXBootAnalysisMessage')




_OSXBOOTANALYSIS = _descriptor.Descriptor(
  name='OSXBootAnalysis',
  full_name='OSXBootAnalysis',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='OSXBootAnalysis.timeStamp', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='agentGUID', full_name='OSXBootAnalysis.agentGUID', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='analysisGUID', full_name='OSXBootAnalysis.analysisGUID', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='eventTimeStamp', full_name='OSXBootAnalysis.eventTimeStamp', index=3,
      number=4, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='eventType', full_name='OSXBootAnalysis.eventType', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='processId', full_name='OSXBootAnalysis.processId', index=5,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parentProcessId', full_name='OSXBootAnalysis.parentProcessId', index=6,
      number=7, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imageFileName', full_name='OSXBootAnalysis.imageFileName', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='commandLine', full_name='OSXBootAnalysis.commandLine', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imageFilepath', full_name='OSXBootAnalysis.imageFilepath', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imageFileMD5', full_name='OSXBootAnalysis.imageFileMD5', index=10,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='siteId', full_name='OSXBootAnalysis.siteId', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='OSXBootAnalysis.uuid', index=12,
      number=13, type=9, cpp_type=9, label=1,
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
  serialized_end=389,
)

DESCRIPTOR.message_types_by_name['OSXBootAnalysis'] = _OSXBOOTANALYSIS

class OSXBootAnalysis(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OSXBOOTANALYSIS

  # @@protoc_insertion_point(class_scope:OSXBootAnalysis)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\"com.ziften.server.protocol.messageB\026OSXBootAnalysisMessage')
_OSXBOOTANALYSIS.fields_by_name['timeStamp'].has_options = True
_OSXBOOTANALYSIS.fields_by_name['timeStamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_OSXBOOTANALYSIS.fields_by_name['agentGUID'].has_options = True
_OSXBOOTANALYSIS.fields_by_name['agentGUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_OSXBOOTANALYSIS.fields_by_name['analysisGUID'].has_options = True
_OSXBOOTANALYSIS.fields_by_name['analysisGUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_OSXBOOTANALYSIS.fields_by_name['eventTimeStamp'].has_options = True
_OSXBOOTANALYSIS.fields_by_name['eventTimeStamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_OSXBOOTANALYSIS.fields_by_name['uuid'].has_options = True
_OSXBOOTANALYSIS.fields_by_name['uuid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
# @@protoc_insertion_point(module_scope)
