#!/usr/bin/env python

from naoqi import *
from PostHabla import *
from PostHabla import misocket
from PostHabla import myEventHandler
import time
import socket

ip = "169.254.87.118"
port = 9559

broker = ALBroker("pythonBroker","0.0.0.0", 0, ip, port)
motion = ALProxy("ALMotion", ip, port)
memory = ALProxy("ALMemory", ip, port)
basicawareness = ALProxy("ALBasicAwareness", ip, port)
barcode = ALProxy("ALBarcodeReader", ip, port)
tts = ALProxy("ALTextToSpeech", ip, port)
aas = ALProxy("ALAnimatedSpeech", ip, port)


if __name__ == "__main__":
	manejaEstimulos(ip, port, False)
	#objetivo = [0.0, 0.51]
	objetivo = [-0.0031099319458007812, 0.09199810028076172]
	mueveCabeza(ip, port, objetivo)
	time.sleep(2)
	calculado = compruebaCabeza(ip, port)
	error = [objetivo[0] - calculado[0], objetivo[1] - calculado[1]]
	
	print 'Errores: '
	print str(error)
	print ''

	NaoSocketServer = misocket()
	#NaoSocket = misocket()
	NaoSocketServer.escucha("localhost", 9999)
	handlerModule = myEventHandler("handlerModule")
	while True:
		id = memory.post.subscribeToEvent("BarcodeReader/BarcodeDetected", "handlerModule", "myCallback")
		bol = NaoSocketServer.recibe()
		if(bol == True):
			memory.stop(id)
			#nombre = memory.getData("cadena")
			#print nombre
			#nombre = str(nombre)
			#if(nombre != ''):
			#	print nombre
			#	nombre = nombre.split("'",3)
			#	nombre = nombre[1]
				#NaoSocket = misocket()
				#NaoSocket.conecta("localhost", 9998)
				#NaoSocket.envia(nombre)
				#NaoSocket.cierra()			
				#tts.say('Bienvenido ' + nombre)
				
				#print nombre
			#else:
			#	nombre = ""
			#nombre = memory.getData("nombre")
			#print nombre
			#if(nombre):
			#	nombre = nombre.split("'",3)
			#	nombre = nombre[1]
			#	NaoSocket.conecta("localhost", 9998)
			#	NaoSocket.envia(nombre)
			 #	NaoSocket.cierra()
			#else:
			#	nombre = ""

			frases = NaoSocketServer.dameMensaje()
			frases = frases[2:len(frases)]
			frases = frases.split("/")
			print frases
			iteracion = 0
			for iteracion in range(0,len(frases)):
				aas.say(str(frases[iteracion]))
				#tts.say(str(frases[iteracion]))
				iteracion = iteracion + 1

			memory.post.insertData("cadena", '')
	
