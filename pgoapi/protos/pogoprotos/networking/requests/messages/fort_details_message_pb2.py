# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/fort_details_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/fort_details_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_pb=_b('\nBpogoprotos/networking/requests/messages/fort_details_message.proto\x12\'pogoprotos.networking.requests.messages\"J\n\x12\x46ortDetailsMessage\x12\x0f\n\x07\x66ort_id\x18\x01 \x01(\t\x12\x10\n\x08latitude\x18\x02 \x01(\x01\x12\x11\n\tlongitude\x18\x03 \x01(\x01\x62\x06proto3')
)




_FORTDETAILSMESSAGE = _descriptor.Descriptor(
  name='FortDetailsMessage',
  full_name='pogoprotos.networking.requests.messages.FortDetailsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='pogoprotos.networking.requests.messages.FortDetailsMessage.fort_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='pogoprotos.networking.requests.messages.FortDetailsMessage.latitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='pogoprotos.networking.requests.messages.FortDetailsMessage.longitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=185,
)

DESCRIPTOR.message_types_by_name['FortDetailsMessage'] = _FORTDETAILSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FortDetailsMessage = _reflection.GeneratedProtocolMessageType('FortDetailsMessage', (_message.Message,), dict(
  DESCRIPTOR = _FORTDETAILSMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.fort_details_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.FortDetailsMessage)
  ))
_sym_db.RegisterMessage(FortDetailsMessage)


# @@protoc_insertion_point(module_scope)
