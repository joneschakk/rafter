#!/usr/bin/python

#socket server using threads

import socket, sys, threading
from thread import *
import sys
import pickle
from random import uniform

time_out_flag=0
nodes_up=[]
lock = threading.Lock()
time_out = 12.0 + uniform(0, 4)

def voter(campainger_detail):
    if not time_out_flag:
        voteGranted=True
        votedFor=addr
        currTerm+=1;
        conn = campainger_detail[0][0]
        data = 
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
                else:
                    logs=logs+message.log
    #came out of loop
    conn.close()

def time_out_thread():
    global time_out_flag
    global time_out
    global status
    if status == 1:
        while True:
            if not time_out_flag:
                time.sleep(time_out)
                message.log = "A"
                sender(0,message,)
    else:
        begin_time=float(time.time())
        while time_out_flag:
            seconds_passed=float(time.time())-begin_time
            if not time_out_flag<=seconds_passed:
                sender()
                

        
        
    
    time_out = 12.0 + uniform(0, 4)




                
def listener(arg):

    HOST = 'localhost'
    listnerPORT = int(arg)
    global all_nodes 
    ihear = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
    try:
        while 1:
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
            
    ihear.close()
           



def sender(voteGranted=0,message,voter_detail):
    global all_nodes
    conn = campainger_detail[0][0]
    if voteGranted:
        data=True
        conn.send(data)
    elif not voteGranted and message.log
        for x in all_nodes:
            data = pickle.dumps(message.log)
            x[0].send(data)

    
    
if __name__ == '__main__':
    listnerPORT=sys.argv[1]
    num_nodes=int(sys.argv[2])
    for x in range (3,num_nodes+1):
        nodes_up.append(sys.argv[x].split(':'))

    start_new_thread(listener,sys.argv[1])
    start_new_thread(sender,nodes_up)




    
        

            
        
    


   



            

