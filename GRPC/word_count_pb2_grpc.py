# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import word_count_pb2 as word__count__pb2


class WordCountStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CountWords = channel.unary_unary(
                '/word_count.WordCount/CountWords',
                request_serializer=word__count__pb2.WordsRequest.SerializeToString,
                response_deserializer=word__count__pb2.WordsResponse.FromString,
                )


class WordCountServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CountWords(self, request, context):
        """Unary
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WordCountServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CountWords': grpc.unary_unary_rpc_method_handler(
                    servicer.CountWords,
                    request_deserializer=word__count__pb2.WordsRequest.FromString,
                    response_serializer=word__count__pb2.WordsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'word_count.WordCount', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WordCount(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CountWords(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/word_count.WordCount/CountWords',
            word__count__pb2.WordsRequest.SerializeToString,
            word__count__pb2.WordsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)