from naoqi import ALProxy
robot_ip = "127.0.0.1"
puerto = 54013
aas = ALProxy("ALAnimatedSpeech", robot_ip, puerto)
tts = ALProxy("ALTextToSpeech", robot_ip, puerto)

f = open("Speech.txt","r")
cad = f.read()
#cad = f.read()
f.close()

lista = cad.splitlines()
longitud = len(lista)
indice = lista.index("Buenos dias, esperamos que su compra sea satisfactoria")
newList = lista[indice:longitud]
#aux = cad.split()
#longitud = len(aux)
#indice = aux.index("FINCOMENTARIO")
#cad2 = aux[indice + 1: longitud]
longitud2 = len(newList)
#for i in range(0,longitud2):
#    print newList[i]
aas.say(str(newList[0]))
aas.say(str(newList[1]))
aas.say(str(newList[2]))
aas.say(str(newList[3]) + ".^start(animations/Stand/Gestures/Hey_1)")
##Nombre="Javi"
##aas.say(Nombre + "^start(animations/Stand/Gestures/Hey_1)")

diccio = {"primeraFrase": newList[0], "segundaFrase": newList[1], "terceraFrase": newList[2]}
