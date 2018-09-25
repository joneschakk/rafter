#!/usr/bin/python

#socket server using threads

import socket, sys ,threading
from threading import *
from thread import *
import sys
import pickle
from random import uniform

class messages:
    def __init__ (self, logs="",currTerm=0,voteGranted=False,appended=False):
        self.logs=logs
        self.currTerm=currTerm
        self.voteGranted=voteGranted
        self.appended=appended

time_out_flag=0
nodes_up=[]
lock = threading.Lock()
campainger_detail=[]
time_out = 12.0 + uniform(0, 4)
my=messages()
all_nodes=[]

def voter(campainger_detail):
    global currTerm
    global voteGranted
    global votedFor
    if not time_out_flag:
        voteGranted=True
        votedFor=addr
        currTerm+=1;
        my.voteGranted=True
        my.currTerm=currTerm
        conn = campainger_detail[0][0]
        data = pickle.dumps(my)
        conn.send(data)

def clientthread(conn,addr):
    
    campainger_detail=(conn,addr)
    while True:
        #receiving data from client
        data = conn.recv(1024)
        
        with lock:
            if data:
                message=pickle.loads(data)
                if not message.log:
                    if not message.currTerm<=currTerm:
                        voter(campainger_detail)
                    elif message.currTerm==currTerm:
                        state=0
                    elif message.voteGranted:
                        voteReceived+=1
                        if voteReceived>len(all_nodes):
                            status=1
                            time_out_flag=1
                            
                else:
                    logs=logs+message.log
    #came out of loop
    conn.close()

def time_out_thread():
    global time_out_flag
    global time_out
    global status
    # if status == 1:
    #     while True:
    #         if not time_out_flag:
    #             time.sleep(time_out)
    #             message.log = "A"
    #             sender()
    while True:
        if status == 0:
            begin_time=float(time.time())
            while not time_out_flag and not time_out<=seconds_passed:
                seconds_passed=float(time.time())-begin_time
            time_out=0
            if status == 0: #if status didnt change its because of the timer
                status =3
        
        elif status == 3:
            begin_time=float(time.time())
            start_new_thread(sender) #campaign mode
            while not time_out_flag and not time_out<=seconds_passed:
                seconds_passed=float(time.time())-begin_time
        
        elif status == 1:
            start_new_thread(sender)
            while True:
                time.sleep(time_out-0.1)
                time_out_flag=1
                time.sleep(0.1)
                time_out_flag=0





        
            
        

    

    time_out = 12.0 + uniform(0, 4)
            
                

        
        
    




                
def listener(arg):

    print "Listner"
    HOST = 'localhost'
    listnerPORT = int(arg)
    global all_nodes 
    #ihear = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket created1")
    
    #bind socket to local host and port
    try:
        ihear.bind((HOST, listnerPORT))
    except socket.error as msg:
        print ("Bind failed. Error code: " + str(msg[0]) + ' Message ' + msg[1])
        sys.exit(0)
        
    print ("Socket bind complete")
    ihear.listen(5)
    

    
    print ("Socket now listening")
    #keep talking with the client
    while 1:
        try:
            
            #wait to accept a connection - blocking call
            conn, addr = ihear.accept()
            
            with lock:
                all_nodes.append((conn,addr))
            print ("Connected with " + addr[0] + ":" + str(addr[1]))
            #start new thread takes 1st argument as a function name to be run, second
            #is the tuple of arguments to the function
            
            start_new_thread(clientthread ,(conn,addr))
        except KeyboardInterrupt: 
            print "Force Kill", all_nodes[0][1]
            sys.exit(0)   
    ihear.close()
           



def sender(my,voter_detail,nodes_up=0):
    global all_nodes
    
    if not nodes_up and not my and not voter_detail:
        print "pass"
    elif nodes_up:
        #isend = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for x in nodes_up:
            print x
            isend.connect(x)
    else:
        conn = campainger_detail[0][0]
        if status==1:
            while True:
                if time_out_flag:
                    for x in all_nodes:
                        my.log='A'
                        data = pickle.dumps(my.log)
                        x[0][0].send(data)
        elif status == 3:
            for x in all_nodes:
                my.log=''
                my.currTerm +=1
                data = pickle.dumps(my.log)
                x[0][0].send(data)
def killall():
    while True:
        try:
            pass
        except KeyboardInterrupt:
            ihear.close()
            isend.close()
            print "Terminated by killall"

        
    

    
    
if __name__ == '__main__':
    listnerPORT=sys.argv[1]
    num_nodes=int(sys.argv[2])
    if num_nodes:
        for x in range (3,num_nodes+3):
            nodes_up.append(('localhost',int(sys.argv[x])))
    ihear = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    isend = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        Thread(target=listener,args=(sys.argv[1],)).start()
        Thread(target=sender,args=(0,0,nodes_up)).start()
        Thread(target=killall,args=()).start()
        
    except KeyboardInterrupt:
        print "killed"
        sys.exit(0)



    
        

            
        
    


   



            
