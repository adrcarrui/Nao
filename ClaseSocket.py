#!/usr/bin/env python

from naoqi import *
import time
import socket

ROBOT_IP="169.254.87.118"

barcode=ALProxy("ALBarcodeReader", ROBOT_IP, 9559)
memory=ALProxy("ALMemory", ROBOT_IP, 9559)
broker = ALBroker("pythonBroker","0.0.0.0", 0, ROBOT_IP, 9559)
aas = ALProxy("ALAnimatedSpeech", ROBOT_IP, 9559)


class misocket:

    def __init__(self):
	self.sock = socket.socket()

    def conecta(self, host, port):
        self.sock.connect((host, port))
	
    def escucha(self, host, port):
	self.sock.bind((host, port))
	self.sock.listen(1)
	print "Ahora escucha"

    def envia(self,msg):        
	#msg = raw_input("Mensaje a enviar: ")
	msg ="ID: " + msg + " FIN"
	#print(len (msg))
	self.sock.sendall(msg)

    def recibe(self):
	conn, addr = self.sock.accept()
	print ("Conexion establecido con ", addr)
	self.msg = conn.recv(1024)
	#print msg
	
    def dameMensaje(self):
	return self.msg

    def cierra(self):
	print "Cerrando conexion..."
	self.sock.close()

class myEventHandler(ALModule):

    def myCallback(self, key, value, msg):
    	aux = str(value)
    	aux = aux.split(";",10)
    	self.nombre = aux[1]

    def dameNombre(self):
        return self.nombre

while True:
	####   LEO QR   ####
	handlerModule = myEventHandler("handlerModule")
	memory.subscribeToEvent("BarcodeReader/BarcodeDetected", "handlerModule", "myCallback")
	time.sleep(5) 
	variable = handlerModule.dameNombre()
	memory.unsubscribeToEvent("BarcodeReader/BarcodeDetected", "handlerModule")
	flag_nao = true
	####################
	if(flag_nao == true):
		NaoSocket = misocket()
		NaoSocketServer = misocket()
		####   ENVIO ID  ####
		NaoSocket.conecta("localhost", 9998)
		NaoSocket.envia(variable)
		NaoSocket.cierra()
		flag_nao = false
	#####################
	if(flag_nao == false):
		####   RECIBO FRASES   ####
		NaoSocketServer.escucha("localhost", 9999)
		NaoSocketServer.recibe()
		frases = NaoSocketServer.dameMensaje()
		#NaoSocketServer.cierra()
		frases = frases[2:len(frases)]
		print frases
		frases = frases.split("/")
		print frases
		iteracion = 0
		for iteracion in range(0,len(frases)):
			aas.say(str(frases[iteracion]) + ".^start(animations/Stand/Gestures/Hey_1)")
			iteracion = iteracion + 1

		aas.say("Espero haberle servido de ayuda en su compra, vuelva pronto" + ".^start(animations/Stand/Gestures/Explain_5)")
	###########################
