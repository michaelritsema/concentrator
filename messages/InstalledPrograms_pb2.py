# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: InstalledPrograms.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import PostgresType_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='InstalledPrograms.proto',
  package='',
  serialized_pb='\n\x17InstalledPrograms.proto\x1a\x12PostgresType.proto\"\x9f\x02\n\x11InstalledPrograms\x12 \n\ttimeStamp\x18\x01 \x02(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x1b\n\tagentGUID\x18\x02 \x02(\tB\x08\x82\xb5\x18\x04uuid\x12\x17\n\x0finstallLocation\x18\x03 \x03(\t\x12\x0c\n\x04name\x18\x04 \x03(\t\x12\x11\n\tpublisher\x18\x05 \x03(\t\x12\x10\n\x08noRepair\x18\x06 \x03(\x05\x12\x10\n\x08noModify\x18\x07 \x03(\x05\x12\x13\n\x0bnoUninstall\x18\x08 \x03(\x05\x12\x0c\n\x04size\x18\t \x03(\x05\x12\x11\n\tuninstall\x18\n \x03(\t\x12\x0f\n\x07version\x18\x0b \x03(\t\x12\x0e\n\x06siteId\x18\x0c \x01(\t\x12\x16\n\x04uuid\x18\r \x01(\tB\x08\x82\xb5\x18\x04uuidB>\n\"com.ziften.server.protocol.messageB\x18InstalledProgramsMessage')




_INSTALLEDPROGRAMS = _descriptor.Descriptor(
  name='InstalledPrograms',
  full_name='InstalledPrograms',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='InstalledPrograms.timeStamp', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='agentGUID', full_name='InstalledPrograms.agentGUID', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='installLocation', full_name='InstalledPrograms.installLocation', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='InstalledPrograms.name', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='publisher', full_name='InstalledPrograms.publisher', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='noRepair', full_name='InstalledPrograms.noRepair', index=5,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='noModify', full_name='InstalledPrograms.noModify', index=6,
      number=7, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='noUninstall', full_name='InstalledPrograms.noUninstall', index=7,
      number=8, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='InstalledPrograms.size', index=8,
      number=9, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uninstall', full_name='InstalledPrograms.uninstall', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='InstalledPrograms.version', index=10,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='siteId', full_name='InstalledPrograms.siteId', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='InstalledPrograms.uuid', index=12,
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
  serialized_start=48,
  serialized_end=335,
)

DESCRIPTOR.message_types_by_name['InstalledPrograms'] = _INSTALLEDPROGRAMS

class InstalledPrograms(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INSTALLEDPROGRAMS

  # @@protoc_insertion_point(class_scope:InstalledPrograms)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\"com.ziften.server.protocol.messageB\030InstalledProgramsMessage')
_INSTALLEDPROGRAMS.fields_by_name['timeStamp'].has_options = True
_INSTALLEDPROGRAMS.fields_by_name['timeStamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_INSTALLEDPROGRAMS.fields_by_name['agentGUID'].has_options = True
_INSTALLEDPROGRAMS.fields_by_name['agentGUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_INSTALLEDPROGRAMS.fields_by_name['uuid'].has_options = True
_INSTALLEDPROGRAMS.fields_by_name['uuid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
# @@protoc_insertion_point(module_scope)
