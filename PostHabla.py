#!/usr/bin/env python

from naoqi import *
import socket
import time

ip = "169.254.87.118"
port = 9559


aux1 = ''	
BaseDatos = ['']
		
memory = ALProxy("ALMemory", ip, port)
tts = ALProxy("ALTextToSpeech", ip, port)
leds = ALProxy("ALLeds", ip, port)

def iniciaLista():
	return []
def devuelveLista(lista):
	return lista
def printLista(cad):
	print cad
def addLista(lista, cad):
	lista.append(cad)

class myEventHandler(ALModule):

    def myCallback(self, key, value, msg):
	
	#print (key, value, msg)
	if(value):
		memory.post.insertData("cadena", value)
		aux1 = devuelveLista(BaseDatos)
		#long = len(aux1)
		#aux1 = aux1[-1]
		cad = str(value)
		print cad
		
    		aux = cad.split("'",3)
		aux = aux[1]
		print aux
		
		#print aux1
		palabraAnt = aux1[-1]
		#print aux1
		#printLista(BaseDatos)
		while(aux!=palabraAnt):
			#memory.post.insertData("nombre", cad)
			palabraAnt = aux
			id = leds.post.rasta(2)	
			leds.wait(id, 0)		
			tts.say("Le doy la bienvenida a la demostracion "+ aux)
			#leds.rasta(1)			
			aux1 = addLista(BaseDatos, aux)
			NaoSocket = misocket()
			NaoSocket.conecta("localhost", 9998)
			NaoSocket.envia(aux)
			NaoSocket.cierra()
			#printLista(BaseDatos)
			
			#memory.post.subscribe("BarcodeReader/BarcodeDetected", "handlerModule", "myCallback")
				

#i = 0
			#for i in range(0,100):
			#	print i
			#	i = i + 1
	
		else:
			memory.post.insertData("nombre", "")
	else:
		memory.post.insertData("nombre", "")
			  	
	#self.nombre = aux[1]
		#nombre = aux[1]
	#	var = aux[1]
	#	print var
	#	memory.insertData("var", var)
	#else:
	#	memory.insertData("var", "")

def habla(msg, ip, port):
	tts = ALProxy("ALTextToSpeech", ip, port)
	id = tts.post.say(msg)
	return id

def compruebaCabeza(ip, port):
	motion = ALProxy("ALMotion", ip, port)
	names = "Head"
	useSensors = False
	commandAngles = motion.getAngles(names, useSensors)
	print "Command angles: "
	print str(commandAngles)
	print ""
	return commandAngles

def mueveCabeza(ip, port, objetive):
	motion = ALProxy("ALMotion", ip, port)
	motion.setStiffnesses("Head", 1.0)
	names = "HeadYaw"
        angles = objetive[0]
   	fractionMaxSpeed = 0.1
   	motion.setAngles(names,angles,fractionMaxSpeed)
    	names = "HeadPitch"
    	angles = objetive[1]
    	fractionMaxSpeed = 0.1
    	motion.setAngles(names,angles,fractionMaxSpeed)

def manejaEstimulos(ip, port, cad):
	basicawareness = ALProxy("ALBasicAwareness", ip, port)
	basicawareness.setStimulusDetectionEnabled("People", cad)
	basicawareness.setStimulusDetectionEnabled("Movement", cad)
	basicawareness.setStimulusDetectionEnabled("Touch", cad)
	basicawareness.setStimulusDetectionEnabled("Sound", cad)

class misocket:

    def __init__(self):
	self.sock = socket.socket()

    def conecta(self, host, port):
        self.sock.connect((host, port))
	
    def escucha(self, host, port):
	self.sock.bind((host, port))
	self.sock.listen(10)
	print "Ahora escucha"

    def envia(self,msg):
	msg ="ID: " + msg + " FIN"
	self.sock.sendall(msg)
	
    def recibe(self):
	conn, addr = self.sock.accept()
	print ("Conexion establecido con ", addr)
	self.msg = conn.recv(1024)
	return True

    def dameMensaje(self):
	return self.msg

    def cierra(self):
	print "Cerrando conexion..."
	self.sock.close()
