# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: session.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='session.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rsession.proto\"R\n\tLNInvoice\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x01\x12\x0f\n\x07invoice\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x05\"7\n\x07Receipt\x12\x1b\n\x07invoice\x18\x01 \x01(\x0b\x32\n.LNInvoice\x12\x0f\n\x07receipt\x18\x02 \x01(\t\"4\n\x05Image\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"\xe4\x01\n\x05Video\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x13\n\x0bmerkle_root\x18\x02 \x01(\t\x12\x11\n\tfile_path\x18\x03 \x01(\t\x12\x11\n\tfile_size\x18\x04 \x01(\x05\x12\x10\n\x08\x64uration\x18\x05 \x01(\x02\x12\r\n\x05width\x18\x06 \x01(\x05\x12\x0e\n\x06height\x18\x07 \x01(\x05\x12\x0b\n\x03\x66ps\x18\x08 \x01(\x05\x12\x10\n\x08n_frames\x18\t \x01(\x05\x12\x14\n\x0ctotal_chunks\x18\n \x01(\x05\x12\x12\n\nchunk_size\x18\x0b \x01(\x05\x12\x13\n\x0b\x63hunk_price\x18\x0c \x01(\x05\"h\n\x05Swarm\x12\x15\n\x05video\x18\x01 \x01(\x0b\x32\x06.Video\x12\x16\n\x06poster\x18\x02 \x01(\x0b\x32\x06.Image\x12\x13\n\x0btotal_price\x18\x03 \x01(\x05\x12\x1b\n\x07invoice\x18\x04 \x01(\x0b\x32\n.LNInvoice\"N\n\x05\x43hunk\x12\x10\n\x08\x63hunk_id\x18\x01 \x01(\t\x12\x11\n\tchunk_seq\x18\x02 \x01(\x05\x12\x12\n\nchunk_data\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\"\x16\n\x08Macaroon\x12\n\n\x02id\x18\x01 \x01(\t\"N\n\x04Peer\x12\x0f\n\x07peer_id\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\x12\x1b\n\x08macaroon\x18\x04 \x01(\x0b\x32\t.Macaroon\".\n\x10HandshakeRequest\x12\x1a\n\x0b\x63lient_peer\x18\x01 \x01(\x0b\x32\x05.Peer\"I\n\x11HandshakeResponse\x12\x1a\n\x0bserver_peer\x18\x01 \x01(\x0b\x32\x05.Peer\x12\x18\n\x10handshake_status\x18\x02 \x01(\t\"*\n\x0cMediaRequest\x12\x1a\n\x0b\x63lient_peer\x18\x01 \x01(\x0b\x32\x05.Peer\"b\n\x0cMediaRespose\x12\x1a\n\x0bserver_peer\x18\x01 \x01(\x0b\x32\x05.Peer\x12\x1e\n\x06status\x18\x02 \x01(\x0e\x32\x0e.RequestStatus\x12\x16\n\x06swarms\x18\x03 \x03(\x0b\x32\x06.Swarm\"S\n\x08\x41skSwarm\x12\x1a\n\x0b\x63lient_peer\x18\x01 \x01(\x0b\x32\x05.Peer\x12\x10\n\x08swarm_id\x18\x02 \x01(\t\x12\x19\n\x07receipt\x18\x03 \x01(\x0b\x32\x08.Receipt\"\x88\x01\n\rChunkResponse\x12\x1a\n\x0bserver_peer\x18\x01 \x01(\x0b\x32\x05.Peer\x12\x10\n\x08swarm_id\x18\x02 \x01(\t\x12\x15\n\x05\x63hunk\x18\x03 \x01(\x0b\x32\x06.Chunk\x12\x1b\n\x07invoice\x18\x04 \x01(\x0b\x32\n.LNInvoice\x12\x15\n\rnext_chunk_id\x18\x05 \x01(\t\"l\n\x0f\x41skChunkPayment\x12\x1a\n\x0b\x63lient_peer\x18\x01 \x01(\x0b\x32\x05.Peer\x12\x10\n\x08\x63hunk_id\x18\x02 \x01(\t\x12\x10\n\x08swarm_id\x18\x03 \x01(\t\x12\x19\n\x07receipt\x18\x04 \x01(\x0b\x32\x08.Receipt*\"\n\rRequestStatus\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x32\xff\x01\n\x08Streamer\x12\x34\n\thandshake\x12\x11.HandshakeRequest\x1a\x12.HandshakeResponse\"\x00\x12)\n\x07looking\x12\r.MediaRequest\x1a\r.MediaRespose\"\x00\x12+\n\x0cstart_stream\x12\t.AskSwarm\x1a\x0e.ChunkResponse\"\x00\x12\x30\n\x06stream\x12\x10.AskChunkPayment\x1a\x0e.ChunkResponse\"\x00(\x01\x30\x01\x12\x33\n\tpay_chunk\x12\x0e.ChunkResponse\x1a\x10.AskChunkPayment\"\x00(\x01\x30\x01\x62\x06proto3'
)

_REQUESTSTATUS = _descriptor.EnumDescriptor(
  name='RequestStatus',
  full_name='RequestStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1334,
  serialized_end=1368,
)
_sym_db.RegisterEnumDescriptor(_REQUESTSTATUS)

RequestStatus = enum_type_wrapper.EnumTypeWrapper(_REQUESTSTATUS)
OK = 0
ERROR = 1



_LNINVOICE = _descriptor.Descriptor(
  name='LNInvoice',
  full_name='LNInvoice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='LNInvoice.client_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='LNInvoice.timestamp', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='invoice', full_name='LNInvoice.invoice', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='LNInvoice.amount', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=17,
  serialized_end=99,
)


_RECEIPT = _descriptor.Descriptor(
  name='Receipt',
  full_name='Receipt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='invoice', full_name='Receipt.invoice', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receipt', full_name='Receipt.receipt', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=101,
  serialized_end=156,
)


_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='Image.width', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='Image.height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='Image.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=158,
  serialized_end=210,
)


_VIDEO = _descriptor.Descriptor(
  name='Video',
  full_name='Video',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_name', full_name='Video.file_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='merkle_root', full_name='Video.merkle_root', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_path', full_name='Video.file_path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_size', full_name='Video.file_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='duration', full_name='Video.duration', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='Video.width', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='Video.height', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fps', full_name='Video.fps', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='n_frames', full_name='Video.n_frames', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_chunks', full_name='Video.total_chunks', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chunk_size', full_name='Video.chunk_size', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chunk_price', full_name='Video.chunk_price', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=213,
  serialized_end=441,
)


_SWARM = _descriptor.Descriptor(
  name='Swarm',
  full_name='Swarm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='video', full_name='Swarm.video', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='poster', full_name='Swarm.poster', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_price', full_name='Swarm.total_price', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='invoice', full_name='Swarm.invoice', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=443,
  serialized_end=547,
)


_CHUNK = _descriptor.Descriptor(
  name='Chunk',
  full_name='Chunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunk_id', full_name='Chunk.chunk_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chunk_seq', full_name='Chunk.chunk_seq', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chunk_data', full_name='Chunk.chunk_data', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='Chunk.data', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=549,
  serialized_end=627,
)


_MACAROON = _descriptor.Descriptor(
  name='Macaroon',
  full_name='Macaroon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Macaroon.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=629,
  serialized_end=651,
)


_PEER = _descriptor.Descriptor(
  name='Peer',
  full_name='Peer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='peer_id', full_name='Peer.peer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ip', full_name='Peer.ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='Peer.port', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='macaroon', full_name='Peer.macaroon', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=653,
  serialized_end=731,
)


_HANDSHAKEREQUEST = _descriptor.Descriptor(
  name='HandshakeRequest',
  full_name='HandshakeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_peer', full_name='HandshakeRequest.client_peer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=733,
  serialized_end=779,
)


_HANDSHAKERESPONSE = _descriptor.Descriptor(
  name='HandshakeResponse',
  full_name='HandshakeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_peer', full_name='HandshakeResponse.server_peer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='handshake_status', full_name='HandshakeResponse.handshake_status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=781,
  serialized_end=854,
)


_MEDIAREQUEST = _descriptor.Descriptor(
  name='MediaRequest',
  full_name='MediaRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_peer', full_name='MediaRequest.client_peer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=856,
  serialized_end=898,
)


_MEDIARESPOSE = _descriptor.Descriptor(
  name='MediaRespose',
  full_name='MediaRespose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_peer', full_name='MediaRespose.server_peer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='MediaRespose.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='swarms', full_name='MediaRespose.swarms', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=900,
  serialized_end=998,
)


_ASKSWARM = _descriptor.Descriptor(
  name='AskSwarm',
  full_name='AskSwarm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_peer', full_name='AskSwarm.client_peer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='swarm_id', full_name='AskSwarm.swarm_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receipt', full_name='AskSwarm.receipt', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1000,
  serialized_end=1083,
)


_CHUNKRESPONSE = _descriptor.Descriptor(
  name='ChunkResponse',
  full_name='ChunkResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_peer', full_name='ChunkResponse.server_peer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='swarm_id', full_name='ChunkResponse.swarm_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chunk', full_name='ChunkResponse.chunk', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='invoice', full_name='ChunkResponse.invoice', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_chunk_id', full_name='ChunkResponse.next_chunk_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1086,
  serialized_end=1222,
)


_ASKCHUNKPAYMENT = _descriptor.Descriptor(
  name='AskChunkPayment',
  full_name='AskChunkPayment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_peer', full_name='AskChunkPayment.client_peer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chunk_id', full_name='AskChunkPayment.chunk_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='swarm_id', full_name='AskChunkPayment.swarm_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receipt', full_name='AskChunkPayment.receipt', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1224,
  serialized_end=1332,
)

_RECEIPT.fields_by_name['invoice'].message_type = _LNINVOICE
_SWARM.fields_by_name['video'].message_type = _VIDEO
_SWARM.fields_by_name['poster'].message_type = _IMAGE
_SWARM.fields_by_name['invoice'].message_type = _LNINVOICE
_PEER.fields_by_name['macaroon'].message_type = _MACAROON
_HANDSHAKEREQUEST.fields_by_name['client_peer'].message_type = _PEER
_HANDSHAKERESPONSE.fields_by_name['server_peer'].message_type = _PEER
_MEDIAREQUEST.fields_by_name['client_peer'].message_type = _PEER
_MEDIARESPOSE.fields_by_name['server_peer'].message_type = _PEER
_MEDIARESPOSE.fields_by_name['status'].enum_type = _REQUESTSTATUS
_MEDIARESPOSE.fields_by_name['swarms'].message_type = _SWARM
_ASKSWARM.fields_by_name['client_peer'].message_type = _PEER
_ASKSWARM.fields_by_name['receipt'].message_type = _RECEIPT
_CHUNKRESPONSE.fields_by_name['server_peer'].message_type = _PEER
_CHUNKRESPONSE.fields_by_name['chunk'].message_type = _CHUNK
_CHUNKRESPONSE.fields_by_name['invoice'].message_type = _LNINVOICE
_ASKCHUNKPAYMENT.fields_by_name['client_peer'].message_type = _PEER
_ASKCHUNKPAYMENT.fields_by_name['receipt'].message_type = _RECEIPT
DESCRIPTOR.message_types_by_name['LNInvoice'] = _LNINVOICE
DESCRIPTOR.message_types_by_name['Receipt'] = _RECEIPT
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['Video'] = _VIDEO
DESCRIPTOR.message_types_by_name['Swarm'] = _SWARM
DESCRIPTOR.message_types_by_name['Chunk'] = _CHUNK
DESCRIPTOR.message_types_by_name['Macaroon'] = _MACAROON
DESCRIPTOR.message_types_by_name['Peer'] = _PEER
DESCRIPTOR.message_types_by_name['HandshakeRequest'] = _HANDSHAKEREQUEST
DESCRIPTOR.message_types_by_name['HandshakeResponse'] = _HANDSHAKERESPONSE
DESCRIPTOR.message_types_by_name['MediaRequest'] = _MEDIAREQUEST
DESCRIPTOR.message_types_by_name['MediaRespose'] = _MEDIARESPOSE
DESCRIPTOR.message_types_by_name['AskSwarm'] = _ASKSWARM
DESCRIPTOR.message_types_by_name['ChunkResponse'] = _CHUNKRESPONSE
DESCRIPTOR.message_types_by_name['AskChunkPayment'] = _ASKCHUNKPAYMENT
DESCRIPTOR.enum_types_by_name['RequestStatus'] = _REQUESTSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LNInvoice = _reflection.GeneratedProtocolMessageType('LNInvoice', (_message.Message,), {
  'DESCRIPTOR' : _LNINVOICE,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:LNInvoice)
  })
_sym_db.RegisterMessage(LNInvoice)

Receipt = _reflection.GeneratedProtocolMessageType('Receipt', (_message.Message,), {
  'DESCRIPTOR' : _RECEIPT,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:Receipt)
  })
_sym_db.RegisterMessage(Receipt)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {
  'DESCRIPTOR' : _IMAGE,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:Image)
  })
_sym_db.RegisterMessage(Image)

Video = _reflection.GeneratedProtocolMessageType('Video', (_message.Message,), {
  'DESCRIPTOR' : _VIDEO,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:Video)
  })
_sym_db.RegisterMessage(Video)

Swarm = _reflection.GeneratedProtocolMessageType('Swarm', (_message.Message,), {
  'DESCRIPTOR' : _SWARM,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:Swarm)
  })
_sym_db.RegisterMessage(Swarm)

Chunk = _reflection.GeneratedProtocolMessageType('Chunk', (_message.Message,), {
  'DESCRIPTOR' : _CHUNK,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:Chunk)
  })
_sym_db.RegisterMessage(Chunk)

Macaroon = _reflection.GeneratedProtocolMessageType('Macaroon', (_message.Message,), {
  'DESCRIPTOR' : _MACAROON,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:Macaroon)
  })
_sym_db.RegisterMessage(Macaroon)

Peer = _reflection.GeneratedProtocolMessageType('Peer', (_message.Message,), {
  'DESCRIPTOR' : _PEER,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:Peer)
  })
_sym_db.RegisterMessage(Peer)

HandshakeRequest = _reflection.GeneratedProtocolMessageType('HandshakeRequest', (_message.Message,), {
  'DESCRIPTOR' : _HANDSHAKEREQUEST,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:HandshakeRequest)
  })
_sym_db.RegisterMessage(HandshakeRequest)

HandshakeResponse = _reflection.GeneratedProtocolMessageType('HandshakeResponse', (_message.Message,), {
  'DESCRIPTOR' : _HANDSHAKERESPONSE,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:HandshakeResponse)
  })
_sym_db.RegisterMessage(HandshakeResponse)

MediaRequest = _reflection.GeneratedProtocolMessageType('MediaRequest', (_message.Message,), {
  'DESCRIPTOR' : _MEDIAREQUEST,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:MediaRequest)
  })
_sym_db.RegisterMessage(MediaRequest)

MediaResponse = _reflection.GeneratedProtocolMessageType('MediaRespose', (_message.Message,), {
  'DESCRIPTOR' : _MEDIARESPOSE,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:MediaRespose)
  })
_sym_db.RegisterMessage(MediaResponse)

AskSwarm = _reflection.GeneratedProtocolMessageType('AskSwarm', (_message.Message,), {
  'DESCRIPTOR' : _ASKSWARM,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:AskSwarm)
  })
_sym_db.RegisterMessage(AskSwarm)

ChunkResponse = _reflection.GeneratedProtocolMessageType('ChunkResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHUNKRESPONSE,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:ChunkResponse)
  })
_sym_db.RegisterMessage(ChunkResponse)

AskChunkPayment = _reflection.GeneratedProtocolMessageType('AskChunkPayment', (_message.Message,), {
  'DESCRIPTOR' : _ASKCHUNKPAYMENT,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:AskChunkPayment)
  })
_sym_db.RegisterMessage(AskChunkPayment)



_STREAMER = _descriptor.ServiceDescriptor(
  name='Streamer',
  full_name='Streamer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1371,
  serialized_end=1626,
  methods=[
  _descriptor.MethodDescriptor(
    name='handshake',
    full_name='Streamer.handshake',
    index=0,
    containing_service=None,
    input_type=_HANDSHAKEREQUEST,
    output_type=_HANDSHAKERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='looking',
    full_name='Streamer.looking',
    index=1,
    containing_service=None,
    input_type=_MEDIAREQUEST,
    output_type=_MEDIARESPOSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='start_stream',
    full_name='Streamer.start_stream',
    index=2,
    containing_service=None,
    input_type=_ASKSWARM,
    output_type=_CHUNKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='stream',
    full_name='Streamer.stream',
    index=3,
    containing_service=None,
    input_type=_ASKCHUNKPAYMENT,
    output_type=_CHUNKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='pay_chunk',
    full_name='Streamer.pay_chunk',
    index=4,
    containing_service=None,
    input_type=_CHUNKRESPONSE,
    output_type=_ASKCHUNKPAYMENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STREAMER)

DESCRIPTOR.services_by_name['Streamer'] = _STREAMER

# @@protoc_insertion_point(module_scope)
