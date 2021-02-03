from Cryptodome.Cipher import PKCS1_OAEP ##Llaves publicas con RSA
from Cryptodome.PublicKey import RSA
####
def encriptar():
    mensaje = b"Nuevo mensaje secreto"
    key = RSA.importKey(open("llavepublica.pem", "rb").read())
    cifrado = PKCS1_OAEP.new(key)
    cifrarmensaje = cifrado.encrypt(mensaje)
    f = open("textoCifrado.txt", "wb")
    f.write(cifrarmensaje)
    f.close()
    
def desencriptar():
    f = open("textoCifrado.txt", "rb")
    mensaje = f.read()
    key = RSA.importKey(open("llaveprivada2.pem", "rb").read())
    cifrado = PKCS1_OAEP.new(key)
    decifrarmensaje = cifrado.decrypt(mensaje)
    print(decifrarmensaje)

def enc2(mensaje,llavepublica):
    mensaje = mensaje
    key = RSA.importKey(llavepublica)
    cifrado = PKCS1_OAEP.new(key)
    cifrarmensaje = cifrado.encrypt(mensaje)
    #f = open("textoCifrado.txt", "wb")
    #f.write(cifrarmensaje)
    #f.close()
    return cifrarmensaje
    
def des2(arg, llaveprivada):
    f = arg
    mensaje = f
    key = RSA.importKey(llaveprivada)
    cifrado = PKCS1_OAEP.new(key)
    decifrarmensaje = cifrado.decrypt(mensaje)
    return decifrarmensaje
#encriptar()
#desencriptar()