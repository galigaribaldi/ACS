#cliente
import socket
import sys
###Modulos propios
import models as coneccion ###Conecciona  la base
import encriptar as encripts ##Encritprar y descrinptar
####
print(len(sys.argv))
print("Ip de coneccion: ", sys.argv[1])
recvIp = sys.argv[1]
puerto = int(sys.argv[2])
s = socket.socket()

def imprimirOpciones():
    ##10
    print("Para consultar, Escriba >> CONSULTAR")
    ###20
    print("Para Depositar, presione >> DEPOSITAR (espacio) CANTIDAD_A_DEPOSITAR")
    ###30
    print("Para Retirar, presione >> RETIRAR (espacio) CANTIDAD_A_RETIRAR")
    ##Salir
    print("Para Salir, presione >> SALIR")
    opcion = input("Opciones>> ")
    ###10
    if opcion[0:9].upper() == 'CONSULTAR':
        print(opcion[0:9].upper())
        return str(15)
	##20
    if opcion[0:9].upper() == 'DEPOSITAR':
        print(opcion[0:9].upper())
        print(opcion[10:].upper())
        return str(20)+" "+str(opcion[10:])
	##30
    if opcion[0:7].upper() == 'RETIRAR':
        print(opcion[0:7].upper())
        print(opcion[8:])
        return str(30)+" "+str(opcion[8:])
	##-1
    if opcion.upper() == 'SALIR':
        return str(-1)
s.connect((recvIp, 9000))
cont = 0
mensaje =""
while True:
    if cont == 0:
        calve = input("Ingrese la clave de su banco: ")
        c = coneccion.obtener_llaves(int(calve))
        llave_privada = c[0][0]
        llavepublica = c[0][1]
        s.send(calve.encode())
        cont = cont + 1
    else:
        ###Recibes el mensaje
        respuesta = s.recv(1024)
        respuesta = str(encripts.des2(respuesta, llave_privada).decode())
        ##############
        if respuesta == "SALIR":
            print("Conexion finalizada")
            s.close()
            break
        print(">>> ", respuesta)
        mensaje = imprimirOpciones()
        ###Encriptamos el mensaje
        mens =encripts.enc2(bytes(mensaje, 'utf8'), llavepublica)
        s.send(mens)