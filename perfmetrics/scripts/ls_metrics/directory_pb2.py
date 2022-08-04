# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: directory.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='directory.proto',
  package='perfmetrics',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x64irectory.proto\x12\x0bperfmetrics\"\x97\x01\n\tDirectory\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tnum_files\x18\x02 \x01(\x05\x12\x18\n\x10\x66ile_name_prefix\x18\x03 \x01(\t\x12\x11\n\tfile_size\x18\x04 \x01(\t\x12\x13\n\x0bnum_folders\x18\x05 \x01(\x05\x12\'\n\x07\x66olders\x18\x06 \x03(\x0b\x32\x16.perfmetrics.Directoryb\x06proto3'
)




_DIRECTORY = _descriptor.Descriptor(
  name='Directory',
  full_name='perfmetrics.Directory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='perfmetrics.Directory.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_files', full_name='perfmetrics.Directory.num_files', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_name_prefix', full_name='perfmetrics.Directory.file_name_prefix', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_size', full_name='perfmetrics.Directory.file_size', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_folders', full_name='perfmetrics.Directory.num_folders', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='folders', full_name='perfmetrics.Directory.folders', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=184,
)

_DIRECTORY.fields_by_name['folders'].message_type = _DIRECTORY
DESCRIPTOR.message_types_by_name['Directory'] = _DIRECTORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Directory = _reflection.GeneratedProtocolMessageType('Directory', (_message.Message,), {
  'DESCRIPTOR' : _DIRECTORY,
  '__module__' : 'directory_pb2'
  # @@protoc_insertion_point(class_scope:perfmetrics.Directory)
  })
_sym_db.RegisterMessage(Directory)


# @@protoc_insertion_point(module_scope)