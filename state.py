


STATE_FOLLOWER = 'follower'
STATE_CANDIDATE = 'follower'
STATE_LEADER = 'follower'
from threading import Event

ELECTION_TIMEOUT_MILLIS = 500

class Server(object):
    def __init__(self, id=0, peers=0):
        self.state = STATE_FOLLOWER
        self.peers = peers
        self.log_idx=0
        self.term=0
        self.node_list=[('127.0.0.1',8120,True)]

    def run(self):
        while True:
            pass

    def add_node(self, server_addr):
        for node in self.node_list:
            if node==server_addr and node[2]==False:  #node_list=[ip_addr,port,actv/de-actv]
                node[2]=True
        
# def when_timeout():
#     pass


    
