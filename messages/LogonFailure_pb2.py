# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: LogonFailure.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import PostgresType_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='LogonFailure.proto',
  package='',
  serialized_pb='\n\x12LogonFailure.proto\x1a\x12PostgresType.proto\"\x82\x08\n\x0cLogonFailure\x12 \n\ttimeStamp\x18\x01 \x02(\x03\x42\r\x82\xb5\x18\ttimestamp\x12\x1b\n\tagentGUID\x18\x02 \x02(\tB\x08\x82\xb5\x18\x04uuid\x12\x0e\n\x06siteId\x18\x03 \x01(\t\x12\x16\n\x04uuid\x18\x04 \x01(\tB\x08\x82\xb5\x18\x04uuid\x12+\n\nnLogonType\x18\x05 \x02(\x0e\x32\x17.LogonFailure.LogonType\x12/\n\x0cnFailureType\x18\x06 \x02(\x0e\x32\x19.LogonFailure.FailureType\x12\x12\n\nStatusCode\x18\x07 \x01(\t\x12\x15\n\rSubstatusCode\x18\x08 \x01(\t\x12\x13\n\x0b\x41\x63\x63ountName\x18\t \x02(\t\x12\x12\n\nDomainName\x18\n \x02(\t\x12\x11\n\tisConsole\x18\x0b \x02(\x08\x12\x17\n\x0fworkstationName\x18\x0c \x02(\t\x12\x1d\n\x0bprocessUUID\x18\r \x02(\tB\x08\x82\xb5\x18\x04uuid\x12\x11\n\tIPAddress\x18\x0e \x01(\t\x12\x0e\n\x06IPPort\x18\x0f \x01(\t\"\xd2\x01\n\tLogonType\x12\x14\n\x10LogonInteractive\x10\x02\x12\x10\n\x0cLogonNetwork\x10\x03\x12\x0e\n\nLogonBatch\x10\x04\x12\x10\n\x0cLogonService\x10\x05\x12\x0f\n\x0bLogonUnlock\x10\x07\x12\x19\n\x15LogonNetworkCleartext\x10\x08\x12\x17\n\x13LogonNewCredentials\x10\t\x12\x1a\n\x16LogonRemoteInteractive\x10\n\x12\x1a\n\x16LogonCachedInteractive\x10\x0b\"\x95\x03\n\x0b\x46\x61ilureType\x12\x12\n\x0e\x46\x61ilureUnknown\x10\x00\x12\x1f\n\x1b\x46\x61ilureUserNameDoesNotExist\x10\x01\x12\x1c\n\x18\x46\x61ilurePasswordIncorrect\x10\x02\x12\x18\n\x14\x46\x61ilureUserLockedOut\x10\x03\x12!\n\x1d\x46\x61ilureAccountCurrentlyLocked\x10\x04\x12&\n\"FailureUserOutsideTimeRestrictions\x10\x05\x12!\n\x1d\x46\x61ilureWorkstationRestriction\x10\x06\x12\x1c\n\x18\x46\x61ilureAccountExpiration\x10\x07\x12\x1d\n\x19\x46\x61ilurePasswordExpiration\x10\x08\x12\x1a\n\x16\x46\x61ilureClocksOutOfSync\x10\t\x12%\n!FailureUserRequiredChangePassword\x10\n\x12+\n\'FailureUserNotGrantedRequestedLogonType\x10\x0b\x42\x39\n\"com.ziften.server.protocol.messageB\x13LogonFailureMessage')



_LOGONFAILURE_LOGONTYPE = _descriptor.EnumDescriptor(
  name='LogonType',
  full_name='LogonFailure.LogonType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LogonInteractive', index=0, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LogonNetwork', index=1, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LogonBatch', index=2, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LogonService', index=3, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LogonUnlock', index=4, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LogonNetworkCleartext', index=5, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LogonNewCredentials', index=6, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LogonRemoteInteractive', index=7, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LogonCachedInteractive', index=8, number=11,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=451,
  serialized_end=661,
)

_LOGONFAILURE_FAILURETYPE = _descriptor.EnumDescriptor(
  name='FailureType',
  full_name='LogonFailure.FailureType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FailureUnknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FailureUserNameDoesNotExist', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FailurePasswordIncorrect', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FailureUserLockedOut', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FailureAccountCurrentlyLocked', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FailureUserOutsideTimeRestrictions', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FailureWorkstationRestriction', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FailureAccountExpiration', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FailurePasswordExpiration', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FailureClocksOutOfSync', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FailureUserRequiredChangePassword', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FailureUserNotGrantedRequestedLogonType', index=11, number=11,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=664,
  serialized_end=1069,
)


_LOGONFAILURE = _descriptor.Descriptor(
  name='LogonFailure',
  full_name='LogonFailure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='LogonFailure.timeStamp', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')),
    _descriptor.FieldDescriptor(
      name='agentGUID', full_name='LogonFailure.agentGUID', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='siteId', full_name='LogonFailure.siteId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='LogonFailure.uuid', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='nLogonType', full_name='LogonFailure.nLogonType', index=4,
      number=5, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nFailureType', full_name='LogonFailure.nFailureType', index=5,
      number=6, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StatusCode', full_name='LogonFailure.StatusCode', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SubstatusCode', full_name='LogonFailure.SubstatusCode', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AccountName', full_name='LogonFailure.AccountName', index=8,
      number=9, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DomainName', full_name='LogonFailure.DomainName', index=9,
      number=10, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isConsole', full_name='LogonFailure.isConsole', index=10,
      number=11, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='workstationName', full_name='LogonFailure.workstationName', index=11,
      number=12, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='processUUID', full_name='LogonFailure.processUUID', index=12,
      number=13, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')),
    _descriptor.FieldDescriptor(
      name='IPAddress', full_name='LogonFailure.IPAddress', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='IPPort', full_name='LogonFailure.IPPort', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LOGONFAILURE_LOGONTYPE,
    _LOGONFAILURE_FAILURETYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=43,
  serialized_end=1069,
)

_LOGONFAILURE.fields_by_name['nLogonType'].enum_type = _LOGONFAILURE_LOGONTYPE
_LOGONFAILURE.fields_by_name['nFailureType'].enum_type = _LOGONFAILURE_FAILURETYPE
_LOGONFAILURE_LOGONTYPE.containing_type = _LOGONFAILURE;
_LOGONFAILURE_FAILURETYPE.containing_type = _LOGONFAILURE;
DESCRIPTOR.message_types_by_name['LogonFailure'] = _LOGONFAILURE

class LogonFailure(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOGONFAILURE

  # @@protoc_insertion_point(class_scope:LogonFailure)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\"com.ziften.server.protocol.messageB\023LogonFailureMessage')
_LOGONFAILURE.fields_by_name['timeStamp'].has_options = True
_LOGONFAILURE.fields_by_name['timeStamp']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\ttimestamp')
_LOGONFAILURE.fields_by_name['agentGUID'].has_options = True
_LOGONFAILURE.fields_by_name['agentGUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_LOGONFAILURE.fields_by_name['uuid'].has_options = True
_LOGONFAILURE.fields_by_name['uuid']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
_LOGONFAILURE.fields_by_name['processUUID'].has_options = True
_LOGONFAILURE.fields_by_name['processUUID']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\202\265\030\004uuid')
# @@protoc_insertion_point(module_scope)