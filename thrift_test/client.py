# -*- coding: UTF-8 -*-
"""
# WANGZHE12
"""
from HelloService import HelloService
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from HelloService.ttypes import MyMessage


try:
    # 连接Socket
    transport = TSocket.TSocket('localhost', 9090)
    # 获取Transport
    transport = TTransport.TBufferedTransport(transport)
    # 获取TBinaryProtocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    # 创建一个Client
    client = HelloService.Client(protocol)
    # 连接通道transport
    transport.open()
    # 调用某个没有返回值的函数
    client.sayHello()
    # 调用某个有返回值的函数
    print(client.getData("client access"))

    print(client.getInfo(MyMessage(name="abc", age=567)))
    # 关闭通道transport
    transport.close()
except :
    print('error')


