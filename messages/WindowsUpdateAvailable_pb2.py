# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WindowsUpdateAvailable.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import PostgresType_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WindowsUpdateAvailable.proto',
  package='',
  serialized_pb='\n\x1cWindowsUpdateAvailable.proto\x1a\x12PostgresType.proto\"\xa0\x04\n\x16WindowsUpdateAvailable\x12 \n\ttimeStamp\x18\x01 \x02(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x1b\n\tagentGUID\x18\x02 \x02(\tB\x08\x82\xb5\x18\x04uuid\x12\x13\n\x0b\x64\x65scription\x18\x03 \x03(\t\x12\x10\n\x08updateID\x18\x04 \x03(\t\x12\x10\n\x08revision\x18\x05 \x03(\x05\x12\x14\n\x0cisDownloaded\x18\x06 \x03(\x08\x12\x10\n\x08isHidden\x18\x07 \x03(\x08\x12\x13\n\x0bisInstalled\x18\x08 \x03(\x08\x12\x13\n\x0bisMandatory\x18\t \x03(\x08\x12\x17\n\x0fisUninstallable\x18\n \x03(\x08\x12\x10\n\x08\x65ulaText\x18\x0b \x03(\t\x12\x10\n\x08severity\x18\x0c \x03(\t\x12\x14\n\x0creleaseNotes\x18\r \x03(\t\x12\x1a\n\x12securityBulletinID\x18\x0e \x03(\t\x12\x1b\n\x13supersededUpdateIDs\x18\x0f \x03(\t\x12\x12\n\nsupportUrl\x18\x10 \x03(\t\x12\r\n\x05title\x18\x11 \x03(\t\x12\x13\n\x0bkbArticleID\x18\x12 \x03(\x05\x12\x1b\n\x13uninstallationNotes\x18\x13 \x03(\t\x12\x14\n\x0csizeOfUpdate\x18\x15 \x03(\x03\x12\x0e\n\x06siteId\x18\x14 \x01(\t\x12\x16\n\x04uuid\x18\x16 \x01(\tB\x08\x82\xb5\x18\x04uuid\x12\x1d\n\x0bwuaScanUUID\x18\x17 \x01(\tB\x08\x82\xb5\x18\x04uuidBC\n\"com.ziften.server.protocol.messageB\x1dWindowsUpdateAvailableMessage')




_WINDOWSUPDATEAVAILABLE = _descriptor.Descriptor(
  name='WindowsUpdateAvailable',
  full_name='WindowsUpdateAvailable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='WindowsUpdateAvailable.timeStamp', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='agentGUID', full_name='WindowsUpdateAvailable.agentGUID', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='description', full_name='WindowsUpdateAvailable.description', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updateID', full_name='WindowsUpdateAvailable.updateID', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='revision', full_name='WindowsUpdateAvailable.revision', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isDownloaded', full_name='WindowsUpdateAvailable.isDownloaded', index=5,
      number=6, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isHidden', full_name='WindowsUpdateAvailable.isHidden', index=6,
      number=7, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isInstalled', full_name='WindowsUpdateAvailable.isInstalled', index=7,
      number=8, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isMandatory', full_name='WindowsUpdateAvailable.isMandatory', index=8,
      number=9, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isUninstallable', full_name='WindowsUpdateAvailable.isUninstallable', index=9,
      number=10, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eulaText', full_name='WindowsUpdateAvailable.eulaText', index=10,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='severity', full_name='WindowsUpdateAvailable.severity', index=11,
      number=12, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='releaseNotes', full_name='WindowsUpdateAvailable.releaseNotes', index=12,
      number=13, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='securityBulletinID', full_name='WindowsUpdateAvailable.securityBulletinID', index=13,
      number=14, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='supersededUpdateIDs', full_name='WindowsUpdateAvailable.supersededUpdateIDs', index=14,
      number=15, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='supportUrl', full_name='WindowsUpdateAvailable.supportUrl', index=15,
      number=16, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='WindowsUpdateAvailable.title', index=16,
      number=17, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kbArticleID', full_name='WindowsUpdateAvailable.kbArticleID', index=17,
      number=18, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uninstallationNotes', full_name='WindowsUpdateAvailable.uninstallationNotes', index=18,
      number=19, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sizeOfUpdate', full_name='WindowsUpdateAvailable.sizeOfUpdate', index=19,
      number=21, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='siteId', full_name='WindowsUpdateAvailable.siteId', index=20,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='WindowsUpdateAvailable.uuid', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='wuaScanUUID', full_name='WindowsUpdateAvailable.wuaScanUUID', index=22,
      number=23, type=9, cpp_type=9, label=1,
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
  serialized_start=53,
  serialized_end=597,
)

DESCRIPTOR.message_types_by_name['WindowsUpdateAvailable'] = _WINDOWSUPDATEAVAILABLE

class WindowsUpdateAvailable(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WINDOWSUPDATEAVAILABLE

  # @@protoc_insertion_point(class_scope:WindowsUpdateAvailable)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\"com.ziften.server.protocol.messageB\035WindowsUpdateAvailableMessage')
_WINDOWSUPDATEAVAILABLE.fields_by_name['timeStamp'].has_options = True
_WINDOWSUPDATEAVAILABLE.fields_by_name['timeStamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_WINDOWSUPDATEAVAILABLE.fields_by_name['agentGUID'].has_options = True
_WINDOWSUPDATEAVAILABLE.fields_by_name['agentGUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_WINDOWSUPDATEAVAILABLE.fields_by_name['uuid'].has_options = True
_WINDOWSUPDATEAVAILABLE.fields_by_name['uuid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_WINDOWSUPDATEAVAILABLE.fields_by_name['wuaScanUUID'].has_options = True
_WINDOWSUPDATEAVAILABLE.fields_by_name['wuaScanUUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
# @@protoc_insertion_point(module_scope)
