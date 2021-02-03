#servidor
import socket
import sys
###Modulos propios
import models as coneccion ###Conecciona  la base
import encriptar as encripts ##Encritprar y descrinptar
########
print(len(sys.argv))
print("Ip de coneccion: ", sys.argv[1])
recvIP = sys.argv[1]
puerto = int(sys.argv[2])
ss = socket.socket()
##Con el metodo bind se le indica qu epuerto se quiere escuchar
ss.bind((recvIP,puerto))
ss.listen(1)
conn, addr = ss.accept()
print("Cliente conectado desde: ", addr[0], ": ", addr[1])
clave = 0
cont = 0
while True:
    #try:
    if cont == 0:
        recibido = conn.recv(5000).decode()
        cont = cont + 1
    else:
        ###Recibes el mensaje
        recibido = conn.recv(5000)
        recibido = str(encripts.des2(recibido, llave_privada).decode())
    print("Cliente dice: ", recibido)
    ########################################################################
    if int(recibido[0:2]) < 9 and int(recibido[0:2]) > 0:
        print(type(recibido))
        d = coneccion.cliente_id(int(recibido[0:2]))
        m = "Clave Banco: "+str(d[0][0])+"\nNombre Cliente: "+str(d[0][1])+"\nEdad: "+str(d[0][2]) +"\nSexo: "+str(d[0][3])+"\nSaldo: "+str(d[0][4])+"\nNum Cambios: "+str(d[0][5])
        clave = int(d[0][0])
        c = coneccion.obtener_llaves(int(clave))
        llave_privada = c[0][0]
        llavepublica = c[0][1]
        m = encripts.enc2(bytes(m, 'utf8'), llavepublica)
        conn.send(m)
    ########################################################################
    ########################################################################
    ###Consultar Saldo
    if int(recibido[0:2]) ==15:
        saldo = coneccion.consultar_saldo_id(clave)
        cadena  = "Tu saldo actual es: "+ str(saldo)
        ###Encriptamos
        cadena = encripts.enc2(bytes(cadena, 'utf8'), llavepublica)
        conn.send(cadena)
    ########################################################################
    ########################################################################
    ##Depositar
    if int(recibido[0:2]) ==20:
        try:
            saldo = coneccion.deposito(clave, int(recibido[3:]))
            cadena ="Tu nuevo saldo al corte es: "+str(saldo)
            ###Encriptamos
            cadena = encripts.enc2(bytes(cadena, 'utf8'), llavepublica)
            conn.send(cadena)
        except:
            cadena ="Lo sentimos hubo un error y no se pudo actualizar"
            cadena = encripts.enc2(bytes(cadena, 'utf8'), llavepublica)
            conn.send(cadena)
    ########################################################################
    ########################################################################
    ##Retirar
    if int(recibido[0:2]) ==30:            
        try:
            print(int(recibido[3:5]))
            saldo = coneccion.retirar(clave, int(recibido[3:]))
            cadena ="Tu nuevo saldo al corte es: "+str(saldo)
            ###Encriptamos
            cadena = encripts.enc2(bytes(cadena, 'utf8'), llavepublica)
            conn.send(cadena)
        except:
            cadena ="Lo sentimos hubo un error y no se pudo actualizar"
            cadena = encripts.enc2(bytes(cadena, 'utf8'), llavepublica)
            conn.send(cadena)
    ########################################################################
    if int(recibido[0:2]) == -1:
        print("Se ha terminado la conexion")
        m="SALIR"
        ###Encriptamos
        m = encripts.enc2(bytes(m, 'utf8'), llavepublica)        
        conn.send(m)
        ss.close()#
        break
        #if type(recibido)!= int:
        #    print("Mensaje>>", recibido)
        #    print("Se ha terminado la conexion")
        #    ss.close()#
        #    break
    #except:
    #    print("Error")
    #    print("Se ha terminado la conexion")
    #    ss.close()#
    #    break