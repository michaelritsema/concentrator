# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OSXAgentCommandResponse.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = _descriptor.FileDescriptor(
  name='OSXAgentCommandResponse.proto',
  package='',
  serialized_pb='\n\x1dOSXAgentCommandResponse.proto\x1a\x12PostgresType.proto\"\xd1\x03\n\x17OSXAgentCommandResponse\x12 \n\ttimeStamp\x18\x01 \x02(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x1b\n\tagentGUID\x18\x02 \x02(\tB\x08\x82\xb5\x18\x04uuid\x12\x19\n\x11\x63ommandIdentifier\x18\x03 \x02(\x04\x12=\n\rcommandResult\x18\x04 \x02(\x0e\x32&.OSXAgentCommandResponse.CommandResult\x12\x0e\n\x06siteId\x18\x05 \x01(\t\x12\x16\n\x04uuid\x18\x06 \x01(\tB\x08\x82\xb5\x18\x04uuid\x12\x36\n\x08\x66\x61ilCode\x18\x07 \x01(\x0e\x32$.OSXAgentCommandResponse.FailureCode\"9\n\rCommandResult\x12\x13\n\x0f\x43OMMAND_SUCCESS\x10\x00\x12\x13\n\x0f\x43OMMAND_FAILURE\x10\x01\"\x81\x01\n\x0b\x46\x61ilureCode\x12\x11\n\rFAIL_NO_ERROR\x10\x00\x12\x15\n\x11\x46\x41IL_MISSING_FILE\x10\x01\x12\x17\n\x13\x46\x41IL_FILE_TOO_LARGE\x10\x02\x12\x16\n\x12\x46\x41IL_ACCESS_DENIED\x10\x03\x12\x17\n\x13\x46\x41IL_FILE_OPERATION\x10\x04\x42\x44\n\"com.ziften.server.protocol.messageB\x1eOSXAgentCommandResponseMessage')



_OSXAGENTCOMMANDRESPONSE_COMMANDRESULT = _descriptor.EnumDescriptor(
  name='CommandResult',
  full_name='OSXAgentCommandResponse.CommandResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COMMAND_SUCCESS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMAND_FAILURE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=330,
  serialized_end=387,
)

_OSXAGENTCOMMANDRESPONSE_FAILURECODE = _descriptor.EnumDescriptor(
  name='FailureCode',
  full_name='OSXAgentCommandResponse.FailureCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FAIL_NO_ERROR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAIL_MISSING_FILE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAIL_FILE_TOO_LARGE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAIL_ACCESS_DENIED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAIL_FILE_OPERATION', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=390,
  serialized_end=519,
)


_OSXAGENTCOMMANDRESPONSE = _descriptor.Descriptor(
  name='OSXAgentCommandResponse',
  full_name='OSXAgentCommandResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='OSXAgentCommandResponse.timeStamp', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='agentGUID', full_name='OSXAgentCommandResponse.agentGUID', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='commandIdentifier', full_name='OSXAgentCommandResponse.commandIdentifier', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='commandResult', full_name='OSXAgentCommandResponse.commandResult', index=3,
      number=4, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='siteId', full_name='OSXAgentCommandResponse.siteId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='OSXAgentCommandResponse.uuid', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='failCode', full_name='OSXAgentCommandResponse.failCode', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OSXAGENTCOMMANDRESPONSE_COMMANDRESULT,
    _OSXAGENTCOMMANDRESPONSE_FAILURECODE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=54,
  serialized_end=519,
)

_OSXAGENTCOMMANDRESPONSE.fields_by_name['commandResult'].enum_type = _OSXAGENTCOMMANDRESPONSE_COMMANDRESULT
_OSXAGENTCOMMANDRESPONSE.fields_by_name['failCode'].enum_type = _OSXAGENTCOMMANDRESPONSE_FAILURECODE
_OSXAGENTCOMMANDRESPONSE_COMMANDRESULT.containing_type = _OSXAGENTCOMMANDRESPONSE;
_OSXAGENTCOMMANDRESPONSE_FAILURECODE.containing_type = _OSXAGENTCOMMANDRESPONSE;
DESCRIPTOR.message_types_by_name['OSXAgentCommandResponse'] = _OSXAGENTCOMMANDRESPONSE

class OSXAgentCommandResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OSXAGENTCOMMANDRESPONSE

  # @@protoc_insertion_point(class_scope:OSXAgentCommandResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\"com.ziften.server.protocol.messageB\036OSXAgentCommandResponseMessage')
_OSXAGENTCOMMANDRESPONSE.fields_by_name['timeStamp'].has_options = True
_OSXAGENTCOMMANDRESPONSE.fields_by_name['timeStamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_OSXAGENTCOMMANDRESPONSE.fields_by_name['agentGUID'].has_options = True
_OSXAGENTCOMMANDRESPONSE.fields_by_name['agentGUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_OSXAGENTCOMMANDRESPONSE.fields_by_name['uuid'].has_options = True
_OSXAGENTCOMMANDRESPONSE.fields_by_name['uuid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
# @@protoc_insertion_point(module_scope)
