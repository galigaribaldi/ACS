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
