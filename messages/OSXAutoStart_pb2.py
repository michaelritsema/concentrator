# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OSXAutoStart.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = _descriptor.FileDescriptor(
  name='OSXAutoStart.proto',
  package='',
  serialized_pb='\n\x12OSXAutoStart.proto\x1a\x12PostgresType.proto\"\xb8\x02\n\x0cOSXAutoStart\x12 \n\ttimeStamp\x18\x01 \x02(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x1b\n\tagentGUID\x18\x02 \x02(\tB\x08\x82\xb5\x18\x04uuid\x12\r\n\x05label\x18\x03 \x02(\t\x12\x19\n\x11\x61utostartlocation\x18\x04 \x02(\t\x12\x10\n\x08\x64isabled\x18\x05 \x02(\t\x12\x10\n\x08procuser\x18\x06 \x02(\t\x12\x11\n\tprocgroup\x18\x07 \x02(\t\x12\x11\n\trunatload\x18\x08 \x02(\t\x12\x10\n\x08ondemand\x18\t \x02(\t\x12\x18\n\x10throttleinterval\x18\n \x02(\t\x12\x0c\n\x04path\x18\x0b \x02(\t\x12\x13\n\x0b\x63ommandline\x18\x0c \x02(\t\x12\x0e\n\x06siteId\x18\r \x01(\t\x12\x16\n\x04uuid\x18\x0e \x01(\tB\x08\x82\xb5\x18\x04uuidB9\n\"com.ziften.server.protocol.messageB\x13OSXAutoStartMessage')




_OSXAUTOSTART = _descriptor.Descriptor(
  name='OSXAutoStart',
  full_name='OSXAutoStart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='OSXAutoStart.timeStamp', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='agentGUID', full_name='OSXAutoStart.agentGUID', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='label', full_name='OSXAutoStart.label', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='autostartlocation', full_name='OSXAutoStart.autostartlocation', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='disabled', full_name='OSXAutoStart.disabled', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='procuser', full_name='OSXAutoStart.procuser', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='procgroup', full_name='OSXAutoStart.procgroup', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='runatload', full_name='OSXAutoStart.runatload', index=7,
      number=8, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ondemand', full_name='OSXAutoStart.ondemand', index=8,
      number=9, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='throttleinterval', full_name='OSXAutoStart.throttleinterval', index=9,
      number=10, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='OSXAutoStart.path', index=10,
      number=11, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='commandline', full_name='OSXAutoStart.commandline', index=11,
      number=12, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='siteId', full_name='OSXAutoStart.siteId', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='OSXAutoStart.uuid', index=13,
      number=14, type=9, cpp_type=9, label=1,
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
  serialized_start=43,
  serialized_end=355,
)

DESCRIPTOR.message_types_by_name['OSXAutoStart'] = _OSXAUTOSTART

class OSXAutoStart(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OSXAUTOSTART

  # @@protoc_insertion_point(class_scope:OSXAutoStart)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\"com.ziften.server.protocol.messageB\023OSXAutoStartMessage')
_OSXAUTOSTART.fields_by_name['timeStamp'].has_options = True
_OSXAUTOSTART.fields_by_name['timeStamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_OSXAUTOSTART.fields_by_name['agentGUID'].has_options = True
_OSXAUTOSTART.fields_by_name['agentGUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_OSXAUTOSTART.fields_by_name['uuid'].has_options = True
_OSXAUTOSTART.fields_by_name['uuid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
# @@protoc_insertion_point(module_scope)
