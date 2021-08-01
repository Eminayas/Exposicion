class Cadena:
    def __init__(self, cadena):
        self.lista = cadena
    
    def  recorrerCadena(self):
        for ele in self.lista:   #[::-1] / para colocarlo al reves 
            print(ele,end=" ")
        for ele in self.lista[::-1]:
            print(ele,end=" ")    
            
        print()     
        for pos,ele in enumerate(self.lista):
            print("[{}]={}  ".format(pos,ele))
        print()    
        
        for pos in range(len(self.lista)-1,0,-1):
            print("[{}]={}  ".format(pos,self.lista[pos]))     
            
            
    def  buscarCaracter(self, buscado):
        encontrado=False
        for pos,ele in enumerate(self.lista):
             if ele==buscado:
                 encontrado=True
                 break # rompe el for
                 
         
        if encontrado:   return pos
        else:            return -1 
        
        
    def  listaPosiciones(self,caracter):
        pass   
        
    def listaPalabras():
        pass
    def cadenaLista():
        pass
    def insertarDato(self,num):
        for pos in range(0,len(self.lista)-1):
            for sig in range(pos+1, len(self.lista)):
                if self.lista[pos] > self.lista[sig]:
                    aux = self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux
                auxiliar=[]
        for pos,ele in enumerate(self.lista):
            if num < ele:
                auxiliar.append(num)
                break
        
        self.lista=self.lista[0:pos]+auxiliar+self.lista[pos:]
                    
                    
    def eliminarOcurrencias(self, buscado):
        
        enc=False
        for pos,ele in enumerate(self.lista):
            if buscado == ele:  
                enc=True
                break
        if enc: self.lista=self.lista[0:pos]+self.lista[pos+1:]
        
    def retornaValor(posicion):
        pass
    def concatenarCadena(dato):
        pass
