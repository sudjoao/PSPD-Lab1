# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: word_count.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10word_count.proto\x12\nword_count\"4\n\x0cWordsRequest\x12\r\n\x05words\x18\x01 \x01(\t\x12\x15\n\rsearched_word\x18\x02 \x01(\t\"1\n\rWordsResponse\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\x12\x11\n\tocurrency\x18\x02 \x01(\x05\x32N\n\tWordCount\x12\x41\n\nCountWords\x12\x18.word_count.WordsRequest\x1a\x19.word_count.WordsResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'word_count_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WORDSREQUEST._serialized_start=32
  _WORDSREQUEST._serialized_end=84
  _WORDSRESPONSE._serialized_start=86
  _WORDSRESPONSE._serialized_end=135
  _WORDCOUNT._serialized_start=137
  _WORDCOUNT._serialized_end=215
# @@protoc_insertion_point(module_scope)