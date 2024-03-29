# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ProcessInventory.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import PostgresType_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ProcessInventory.proto',
  package='',
  serialized_pb='\n\x16ProcessInventory.proto\x1a\x12PostgresType.proto\"\x9a\x07\n\x10ProcessInventory\x12 \n\ttimeStamp\x18\x01 \x02(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x1b\n\tagentGUID\x18\x02 \x02(\tB\x08\x82\xb5\x18\x04uuid\x12\x15\n\rimageFilepath\x18\x03 \x02(\t\x12\x13\n\x0b\x66ileVersion\x18\x04 \x02(\t\x12\x17\n\x0f\x66ileDescription\x18\x05 \x02(\t\x12\x13\n\x0b\x63ompanyName\x18\x06 \x02(\t\x12\x13\n\x0bproductName\x18\x07 \x02(\t\x12\x14\n\x0cinternalName\x18\x08 \x02(\t\x12\x16\n\x0elegalCopyright\x18\t \x02(\t\x12\x17\n\x0flegalTrademarks\x18\n \x02(\t\x12\x18\n\x10originalFilename\x18\x0b \x02(\t\x12\x16\n\x0eproductVersion\x18\x0c \x02(\t\x12\x14\n\x0cimageFileMD5\x18\r \x02(\t\x12\x17\n\x0f\x66ileTextVersion\x18\x0e \x01(\t\x12\x1a\n\x12productTextVersion\x18\x0f \x01(\t\x12\x1b\n\x13sourceModuleMessage\x18\x10 \x01(\t\x12\x0e\n\x06siteId\x18\x11 \x01(\t\x12\x19\n\nisDisabled\x18\x12 \x01(\x08:\x05\x66\x61lse\x12\x13\n\x0bserviceName\x18\x13 \x01(\t\x12\x1a\n\x12serviceDisplayName\x18\x14 \x01(\t\x12\x12\n\nfileLength\x18\x15 \x01(\x03\x12\x16\n\x04uuid\x18\x16 \x01(\tB\x08\x82\xb5\x18\x04uuid\x12\x10\n\x08IsSigned\x18\x17 \x01(\x08\x12\x16\n\x0eValidSignature\x18\x18 \x01(\x08\x12\x18\n\x10SignerIssuerName\x18\x19 \x01(\t\x12\x12\n\nThumbprint\x18\x1a \x01(\t\x12\x13\n\x0bSubjectName\x18\x1b \x01(\t\x12\x1b\n\x13TimestampIssuerName\x18\x1c \x01(\t\x12\x1b\n\x13TimestampThumbprint\x18\x1d \x01(\t\x12\x1c\n\x14TimestampSubjectName\x18\x1e \x01(\t\x12&\n\x0f\x44\x61teOfTimestamp\x18\x1f \x01(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x16\n\x0eSignatureError\x18  \x01(\x05\x12!\n\x19SignatureErrorDescription\x18! \x01(\t\x12\x17\n\x0fOperatingSystem\x18\" \x01(\t\x12\x15\n\rimageFileSHA1\x18# \x01(\t\x12\x17\n\x0fimageFileSHA256\x18$ \x01(\tB=\n\"com.ziften.server.protocol.messageB\x17ProcessInventoryMessage')




_PROCESSINVENTORY = _descriptor.Descriptor(
  name='ProcessInventory',
  full_name='ProcessInventory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='ProcessInventory.timeStamp', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='agentGUID', full_name='ProcessInventory.agentGUID', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='imageFilepath', full_name='ProcessInventory.imageFilepath', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fileVersion', full_name='ProcessInventory.fileVersion', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fileDescription', full_name='ProcessInventory.fileDescription', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='companyName', full_name='ProcessInventory.companyName', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='productName', full_name='ProcessInventory.productName', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='internalName', full_name='ProcessInventory.internalName', index=7,
      number=8, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='legalCopyright', full_name='ProcessInventory.legalCopyright', index=8,
      number=9, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='legalTrademarks', full_name='ProcessInventory.legalTrademarks', index=9,
      number=10, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='originalFilename', full_name='ProcessInventory.originalFilename', index=10,
      number=11, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='productVersion', full_name='ProcessInventory.productVersion', index=11,
      number=12, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imageFileMD5', full_name='ProcessInventory.imageFileMD5', index=12,
      number=13, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fileTextVersion', full_name='ProcessInventory.fileTextVersion', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='productTextVersion', full_name='ProcessInventory.productTextVersion', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sourceModuleMessage', full_name='ProcessInventory.sourceModuleMessage', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='siteId', full_name='ProcessInventory.siteId', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isDisabled', full_name='ProcessInventory.isDisabled', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serviceName', full_name='ProcessInventory.serviceName', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serviceDisplayName', full_name='ProcessInventory.serviceDisplayName', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fileLength', full_name='ProcessInventory.fileLength', index=20,
      number=21, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='ProcessInventory.uuid', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='IsSigned', full_name='ProcessInventory.IsSigned', index=22,
      number=23, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ValidSignature', full_name='ProcessInventory.ValidSignature', index=23,
      number=24, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SignerIssuerName', full_name='ProcessInventory.SignerIssuerName', index=24,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Thumbprint', full_name='ProcessInventory.Thumbprint', index=25,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SubjectName', full_name='ProcessInventory.SubjectName', index=26,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TimestampIssuerName', full_name='ProcessInventory.TimestampIssuerName', index=27,
      number=28, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TimestampThumbprint', full_name='ProcessInventory.TimestampThumbprint', index=28,
      number=29, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TimestampSubjectName', full_name='ProcessInventory.TimestampSubjectName', index=29,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DateOfTimestamp', full_name='ProcessInventory.DateOfTimestamp', index=30,
      number=31, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='SignatureError', full_name='ProcessInventory.SignatureError', index=31,
      number=32, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SignatureErrorDescription', full_name='ProcessInventory.SignatureErrorDescription', index=32,
      number=33, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OperatingSystem', full_name='ProcessInventory.OperatingSystem', index=33,
      number=34, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imageFileSHA1', full_name='ProcessInventory.imageFileSHA1', index=34,
      number=35, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imageFileSHA256', full_name='ProcessInventory.imageFileSHA256', index=35,
      number=36, type=9, cpp_type=9, label=1,
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
  serialized_start=47,
  serialized_end=969,
)

DESCRIPTOR.message_types_by_name['ProcessInventory'] = _PROCESSINVENTORY

class ProcessInventory(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PROCESSINVENTORY

  # @@protoc_insertion_point(class_scope:ProcessInventory)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\"com.ziften.server.protocol.messageB\027ProcessInventoryMessage')
_PROCESSINVENTORY.fields_by_name['timeStamp'].has_options = True
_PROCESSINVENTORY.fields_by_name['timeStamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_PROCESSINVENTORY.fields_by_name['agentGUID'].has_options = True
_PROCESSINVENTORY.fields_by_name['agentGUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_PROCESSINVENTORY.fields_by_name['uuid'].has_options = True
_PROCESSINVENTORY.fields_by_name['uuid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_PROCESSINVENTORY.fields_by_name['DateOfTimestamp'].has_options = True
_PROCESSINVENTORY.fields_by_name['DateOfTimestamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
# @@protoc_insertion_point(module_scope)
