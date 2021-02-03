# Proyecto Final

## Descripción del Código

En ésta sección se explicará como esta conformados los módulos que hace funcionar al código, se explicará la estrctura que se utiliza.

#### Models

Éste archivo contiene los modulos necesarios para la manipulación de datos permanentes, esto se logra gracias al modulo *sqlite*, éste módulo, permite la manipulación de una base de datos sencilla, la cual se aloja en el mismo lugar donde se ejecuta el códgio, cabe mencionar, que no se recomienda usar ésta base para entornos reales, ya que no acepta la concurrencia de varias transacciones a la vez

En éste archivo se contiene las siguientes operaciones DML

* **Select * from Cliente:** Seleccionar todos los clientes registrados
* **Select * from cliente where cliente_id=?:** El cual nos trae los clientes con el id solicitado
* **Select llave_privada, llave_publica from cliente where cliente_id=?:** El cual nos trae la llave privada y publica alojada en el servidor del cliente
* **SELECT saldo from cliente where cliente_id=?:** El cual nos trae el saldo del cliente solicitado
* **UPDATE cliente SET saldo =? where cliente_id=?:** La cual nos permite actualizar el saldo del cliente solicitado

Con todas las operaciones DML anteriormente mencionadas, se puede simular la creación de un sistema bancario, con las operaciones de *Consulta*, *Retiro*, *Abono*

```python
import sqlite3
import rsagenerate as crear

def all_client():
    con = sqlite3.connect('BaseACS.db')
    cursor = con.cursor()
    cursor.execute("SELECT * from cliente;")
    datos = cursor.fetchall()
    con.commit()
    cursor.close()
    con.close()
    return datos
def cliente_id(ids):
    con = sqlite3.connect('BaseACS.db')
    cursor = con.cursor()
    cursor.execute("SELECT * from cliente where cliente_id=?",(ids,))
    datos = cursor.fetchall()
    con.commit()
    cursor.close()
    con.close()
    return datos
###Obtener llaves
def obtener_llaves(ids):
    con = sqlite3.connect('BaseACS.db')
    cursor = con.cursor()
    cursor.execute("SELECT llave_privada, llave_publica from cliente where cliente_id=?",(ids,))
    datos = cursor.fetchall()
    con.commit()
    cursor.close()
    con.close()
    return datos   
##Operacion de consulta
def consultar_saldo_id(ids):
    con = sqlite3.connect('BaseACS.db')
    cursor = con.cursor()
    cursor.execute("SELECT saldo from cliente where cliente_id=?",(ids,))
    datos = cursor.fetchall()
    con.commit()
    cursor.close()
    con.close()
    return datos[0][0]
###Operacion de Retiro
def retirar(ids, retiro):
    con = sqlite3.connect('BaseACS.db')
    cursor = con.cursor()
    ###Oebtener el ultimo saldo
    cursor.execute("SELECT saldo from cliente where cliente_id=?",(ids,))
    datos = cursor.fetchall()
    d = datos[0][0]
    d =d-retiro
    #####Actualizacion
    cursor.execute("UPDATE cliente SET saldo =? where cliente_id=?",(d,ids))
    datos = cursor.fetchall()
    ###Oebtener Devolver el saldo
    cursor.execute("SELECT saldo from cliente where cliente_id=?",(ids,))
    datos = cursor.fetchall()
    con.commit()
    cursor.close()
    con.close()
    return datos[0][0]
####Operacion de Creacion de nuevos clientes
###Operacion de Deposito
def deposito(ids, retiro):
    con = sqlite3.connect('BaseACS.db')
    cursor = con.cursor()
    ###Oebtener el ultimo saldo
    cursor.execute("SELECT saldo from cliente where cliente_id=?",(ids,))
    datos = cursor.fetchall()
    d = datos[0][0]
    d =d+retiro
    #####Actualizacion
    cursor.execute("UPDATE cliente SET saldo =? where cliente_id=?",(d,ids))
    datos = cursor.fetchall()
    ###Oebtener Devolver el saldo
    cursor.execute("SELECT saldo from cliente where cliente_id=?",(ids,))
    datos = cursor.fetchall()
    con.commit()
    cursor.close()
    con.close()
    return datos[0][0]

def crea_cliente(cliente_id, nombre_cliente, edad,sexo,saldo,num_movimientos):
    ###Generacion dee llaves
    g = crear.NewKey()
    publica = g.generatePublicKey()
    privada = g.generatePrivateKey()
    ####
    con = sqlite3.connect('BaseACS.db')
    cursor = con.cursor()
    cursor.execute("INSERT INTO cliente(cliente_id, nombre_cliente, edad,sexo,saldo,num_movimientos, llave_privada, llave_publica) VALUES(?,?,?,?,?,?,?,?);",(cliente_id, nombre_cliente, edad,sexo,saldo,num_movimientos, llave_privada, llave_publica))
    datos = cursor.fetchall()
    con.commit()
    cursor.close()
    con.close()
    print("Cliente: "+str(cliente_id)+ " Registrado")
```

**Importante: Para que funciones éste módulo se debe hacer uso del módulo SQlite3**

#### RsaGenerate

Módulo encargado de generar nuevas llaves públicas y privadas, con ayuda del módulo *from Cryptodome.PublicKey import RSA*.

```python
from Cryptodome.PublicKey import RSA

class NewKey():
    def __init__(self):
        self.llave = RSA.generate(2048) #1025, 2048 
        
    def generatePrivateKey(self):
        #f = open('llaveprivada.pem', 'wb')
        #f.write(self.llave.exportKey('PEM'))
        return self.llave.exportKey('PEM')
        #f.close()
        
    def generatePublicKey(self):
        #g = open('llavepublica2.pem', 'wb')
        #g.write(self.llave.publickey().exportKey('PEM'))
        #g.close()
        return self.llave.publickey().exportKey('PEM')
    ##Generar Llave Privada en formato .txt
    def generatePrivateKey_txt(self):
        f = open('llave.pem', 'wb')
        f.write(self.llave.exportKey('PEM'))
        f.close()
    ##Generar Llave Publica en formato .txt    
    def generatePublicKey_txt(self):
        g = open('llave.pem', 'wb')
        g.write(self.llave.publickey().exportKey('PEM'))
        g.close()        

```

**Importante: Èste Módulo sólo funciona en ambientes basados en UNIX**

#### Encriptar

Èste módulo hace uso de las operaciones de Encriptar (Con ayuda de la llave Pública) y Desencriptar (Con la ayuda de la llave Privada)

```python
from Cryptodome.PublicKey import RSA

class NewKey():
    def __init__(self):
        self.llave = RSA.generate(2048) #1025, 2048 
        
    def generatePrivateKey(self):
        #f = open('llaveprivada.pem', 'wb')
        #f.write(self.llave.exportKey('PEM'))
        return self.llave.exportKey('PEM')
        #f.close()
        
    def generatePublicKey(self):
        #g = open('llavepublica2.pem', 'wb')
        #g.write(self.llave.publickey().exportKey('PEM'))
        #g.close()
        return self.llave.publickey().exportKey('PEM')
    ##Generar Llave Privada en formato .txt
    def generatePrivateKey_txt(self):
        f = open('llave.pem', 'wb')
        f.write(self.llave.exportKey('PEM'))
        f.close()
    ##Generar Llave Publica en formato .txt    
    def generatePublicKey_txt(self):
        g = open('llave.pem', 'wb')
        g.write(self.llave.publickey().exportKey('PEM'))
        g.close()        

```

**Importante: Al igual que el módulo anterior, se necesita importar el módulo *Cryptodome.Cipher* y *Cryptodome.PublicKey**

#### Cliente

En este código se muestra el código que hace funcionar al cliente, el cual se conectar a un puerto y una dirección IP, los cuales se pasan como parametro en la línea de comandos.

Para que éste código se necesita importar los módulos anteriores

```python
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
```



#### Servidor

En éste código se recibe las peticiones del cliente y realiza la conexión a la base.

```python
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
```

## Repositorio

Link del Repositorio: [LINK](https://github.com/galigaribaldi/ACS/tree/main/ProyectoFinal)

