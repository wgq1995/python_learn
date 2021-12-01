# -*- coding: UTF-8 -*-
"""
# WANGZHE12
"""
from HelloService import HelloService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class HelloServiceHandler:
    """
    # HelloServiceHandler是中定义的方法用于实现在thrift文件中定义的接口
    """
    def __init__(self):
        self.log = {}
    def sayHello(self):
        # sayHello接口的实现
        print('sayHello')
    def getData(self, input):
        # getData接口的实现
        return input+' from server 1024'
    def getInfo(self, myMessage):
        res = "name=%s, age=%s" % (myMessage.name, myMessage.age)
        print(res)
        return res

# 实例化Handler
handler = HelloServiceHandler()
# 根据handler创建一个processor
processor = HelloService.Processor(handler)
# 指定端口启动transport
transport = TSocket.TServerSocket(port=9090)
# 创建tfactory, pfactory
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
# 创建Server
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
print('Starting the server...')
# 启动server
server.serve()
print('done.')
