#!/usr/bin/env python
#import socket  
      
#s = socket.socket()   
#s.bind(("localhost", 9999))  
#s.listen(1)  
      
#sc, addr = s.accept()  
      
#while True:  
#	recibido = sc.recv(1024)  
#        if recibido == "quit":  
#           break        
#        print "Recibido:", recibido  
#        sc.send(recibido)  
      
#print "adios"  
      
#sc.close()  
#s.close()  

import socket               # Import socket module

soc = socket.socket()         # Create a socket object
host = "localhost" # Get local machine name
port = 9999                # Reserve a port for your service.
soc.bind((host, port))       # Bind to the port
soc.listen(1)                 # Now wait for client connection.
while True:
    conn, addr = soc.accept()     # Establish connection with client.
    print ("Got connection from",addr)
    msg = conn.recv(1024)
    mensajeCorregido = msg[2:len(msg)]
    print mensajeCorregido
    #print (msg)
    #print type(msg)
    #print len(msg)
    #print msg[0]
    #print msg[1]
    #print msg[2]
    #print msg[3]
    #print msg[4]
    #print msg[5]
    #if ( msg == "Hola" ):
    	#print("Hii everyone")
    #else:
    	#print("Go away")
	#break

#sc.close()  
#s.close()
