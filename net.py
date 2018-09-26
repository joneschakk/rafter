#!/usr/bin/python

#socket server using threads

import socket, sys ,threading
from threading import *
from thread import *
import sys
import pickle
from random import uniform
import os
import time
import logging
import pprint

import inspect
#   
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
loglis =logging.getLogger('listener')
logsen =logging.getLogger('sender')
logtim =logging.getLogger('time_out')
class messages:
    def __init__ (self, log="",currTerm=0,voteGranted=False,appended=False):
        self.log=log
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
isend_list=[]
status=0
logs=""

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

def clientthread(conn,addr=0):
    
    loglis.info("client")
    campainger_detail=(conn,addr)
    global logs
    while True:
        #receiving data from client
        data = conn.recv(512)
        # file = open('abcd','w')
        # file.write(pickle.dumps(data))
        # file.close()
        # file2 = open('abcd','r')
        # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        # data2=pickle.loads(file2.read())
       
        
        #pprint.pprint(data2)
        print '\n'
        with lock:
            if data:
                message=pickle.loads(data)
                print(message)
                
                
                
                loglis.info("pickled")
                if not message.log:
                    if not message.currTerm<=currTerm:
                        print "not message.currTerm<=currTerm:", campainger_detail
                        voter(campainger_detail)
                    elif message.currTerm==currTerm:
                        print "message.currTerm==currTerm:"
                        state=0
                    elif message.voteGranted:
                        voteReceived+=1
                        print "voteReceived+=1"
                        if voteReceived>len(all_nodes):
                            status=1
                            time_out_flag=1
                            print "voteReceived>len(all_nodes):"
                            
                else:
                    logs=logs+message.log
                    loglis.info(logs)
                    loglis.info("logspacehere")
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
            seconds_passed=14.0
            begin_time=float(time.time())
            while not time_out_flag and not time_out<=seconds_passed:
                seconds_passed=float(time.time())-begin_time
            time_out=0
            if status == 0: #if status didnt change its because of the timer
                status =3
        
        elif status == 3:
            begin_time=float(time.time())
            start_new_thread(sender,(my,0,0)) #campaign mode   
            while not time_out_flag and not time_out<=seconds_passed:
                seconds_passed=float(time.time())-begin_time
            status=5
        
        elif status == 1:
            my.log="A"
            start_new_thread(sender,(my,0,0))
            logtim.info( "start_new_thread(sender,(my,0,0))")
            logtim.info("started")
            while True:
                time.sleep(time_out-0.1)
                time_out_flag=1
                time.sleep(0.1)
                time_out_flag=0





        
            
        

    

    time_out = 12.0 + uniform(0, 4)
            
                

        
        
    




                
def listener(arg):

    loglis.info("Listner")
    HOST = 'localhost'
    listnerPORT = int(arg)
    global all_nodes 
    #ihear = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    loglis.info ("Socket created1")
    
    #bind socket to local host and port
    try:
        ihear.bind((HOST, listnerPORT))
    except socket.error as msg:
        print ("Bind failed. Error code: " + str(msg[0]) + ' Message ' + msg[1])
        sys.exit(0)
        
    loglis.info ("Socket bind complete")
    ihear.listen(5)
    

    
    loglis.info ("Socket now listening")
    #keep talking with the client
    while 1:
        try:
            
            #wait to accept a connection - blocking call
            conn, addr = ihear.accept()
            
            with lock:
                all_nodes.append((conn,addr))
            loglis.info ("Connected with " + addr[0] + ":" + str(addr[1]))
            #start new thread takes 1st argument as a function name to be run, second
            #is the tuple of arguments to the function
            
            start_new_thread(clientthread ,(conn,addr))
        except KeyboardInterrupt : 
            loglis.warn("Force Kill", all_nodes[0][1])
            sys.exit(0)   
    ihear.close()
           



def sender(my,voter_detail,nodes_up=0):
    global all_nodes
    global status
    print status
    
        

    if not nodes_up and not my and not voter_detail and not status:
        logsen.info( "pass")
        status=1
    elif nodes_up:
        #isend = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        i=0
        for x in nodes_up:
            print x
            isend = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            isend_list.append(isend)
            start_new_thread(clientthread,(isend,))
            isend_list[i].connect(x)
            i=i+1
            
    else:
        #try:
            # conn = campainger_detail[0][0]
            print "printer all_nodes ", all_nodes
            if status==1:
                while True:
                    if time_out_flag:
                        for x in all_nodes:
                            my.log="C"
                            print "my.log='C'"
                            data = pickle.dumps(my)
                            # print x[0]
                            x[0].send(data)
                            print "hello"
            elif status == 3:
                for x in all_nodes:
                    my.log=""
                    my.currTerm +=1
                    data = pickle.dumps(my.log)
                    x[0].send(data)
        #except:
            #print "broke"
            #pass


def killall():
    while True:
        try:
            pass
        except KeyboardInterrupt:
            ihear.close()
            isend.close()
            print "Terminated by killall"

        
    

    
    
if __name__ == '__main__':
    #global status
    listnerPORT=sys.argv[1]
    num_nodes=int(sys.argv[2])
    if num_nodes:
        for x in range (3,num_nodes+3):
            nodes_up.append(('localhost',int(sys.argv[x])))
    ihear = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # isend = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status=0
    
    try:
        Thread(target=listener,args=(sys.argv[1],)).start()
    except :
        print "killed"
        os.system("./killall.sh")
        
        
        
    try:
        Thread(target=sender,args=(0,0,nodes_up)).start()
    except :
        print "killed"
        os.system("./killall.sh")
    
    time.sleep(.5)
    try:
        Thread(target=time_out_thread,args=()).start()
    except :
        print "killed"
        os.system("./killall.sh")
    
        


    
        

            
        
    


   



            

