
import socket
import select
import time
from wire import *
import state
time_out=5


    


class BaseUDPTransport(object):
    max_dgarm_size_expected = 1024

    def __init__(self, address):
        self.socket = socket.socket( socket.AF_INET,
                                    socket.SOCK_DGRAM)
        addr,port = address.split(':')
        self.server_address = addr, int(port)
        self.break_flag = False
        self.write = self.socket.sendto
        self.my=state.Server()

    
    def datagram_received(self, data, addr):
        raise NotImplementedError

    def serve_forever(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)
        last_timeout = time.time()
        while not self.break_flag:
            if (time.time()-last_timeout)> time_out:
                last_timeout=time.time()
                self.call_election()    
                print "TIME"
            readable, writable, errored = select.select([self.socket], [], [],0.01)
            if readable:
                data, addr = self.socket.recvfrom(self.max_dgarm_size_expected)
                # try:
                    
                self.datagram_received(data, addr)
                    
                # except NotImplementedError:
                #     raise
                # except Exception as oops:
                #     # print(self.server_address)
                #     print("unhandled error on dg rcv:", oops)
    
    
    def close(self):
        self.break_flag = True
        self.socket.close()

