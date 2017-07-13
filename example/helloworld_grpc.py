# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: example/helloworld.proto
# plugin: grpclib.plugin.main
from abc import ABCMeta, abstractmethod

import grpclib.server
import grpclib.client

import example.helloworld_pb2


class Greeter(metaclass=ABCMeta):

    @abstractmethod
    async def SayHello(self, request, context):
        pass

    def __mapping__(self):
        return {
            '/helloworld.Greeter/SayHello': grpclib.server.Method(
                self.SayHello,
                example.helloworld_pb2.HelloRequest,
                example.helloworld_pb2.HelloReply,
            ),
        }


class GreeterStub:

    def __init__(self, channel):
        self.channel = channel

    SayHello = grpclib.client.UnaryUnaryCall(grpclib.client.Method(
        '/helloworld.Greeter/SayHello',
        example.helloworld_pb2.HelloRequest,
        example.helloworld_pb2.HelloReply,
    ))