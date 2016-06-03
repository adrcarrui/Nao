#!/usr/bin/env python

import socket
#def main():
#	funcion = 1
#	if funcion == 1:
#		def funcionenvia ():
	
#s = socket.socket()
#s.connect(("localhost",9998)) 

#while True:
try:
	s = socket.socket()
	s.connect(("localhost", 9998))
	mensaje = raw_input("Mensaje a enviar ")
	#if mensaje == "FIN":
	#	break
	#s.send(mensaje)
	mensaje = "ID " + mensaje + " FIN"
	s.sendall(mensaje)	
	s.proto	
	print mensaje
	print "Conexion terminada"
	s.close()
except socket.error, ex:
	print ex
#s.close()


#s.close()
#			funcion = 0
	
#	if funcion == 0:
#		def funcionescucha():
#			soc = socket.socket()         # Create a socket object
#			host = "localhost" # Get local machine name
#			port = 9999                # Reserve a port for your service.
#			soc.bind((host, port))       # Bind to the port
#			soc.listen(1)                 # Now wait for client connection.
#			while True:
#			    conn, addr = soc.accept()     # Establish connection with client.
#			    print ("Got connection from",addr)
#			    msg = conn.recv(1024)
#			    mensajeCorregido = msg[2:len(msg)]
#			    print mensajeCorregido
    #print (msg)


#if __name__ == "__main__":
#	main()
