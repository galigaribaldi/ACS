
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
#c = obtener_llaves(1)
#print(c[0][0])
#print(c[0][1])
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

###############
#c = all_client()
#print(c)