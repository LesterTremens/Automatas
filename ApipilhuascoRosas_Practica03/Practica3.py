import sys
import math

#Entrada
entrada =sys.argv[1]
#Estructura que organiza las reglas.
class Reglas:
    """docstring forTuringMachine."""
    def __init__(self,q,c1,p,c2,m):
        self.q  = q
        self.c1 = c1
        self.p=p
        self.c2  = c2
        self.m  = m
#Guarda la entrada en una lista
def guardaEntrada(etrada):
    lista=[]
    e=open(entrada)
    with e:
        linea=e.readline()
        while linea:
            lista.append(linea.strip())
            linea=e.readline()
    e.close()
    return lista
#Crea una lista con las funciones de transicion.
def listaReglas(lista):
    lis=[]
    for r in lista[3:]:
          reglas=Reglas(r[0],r[2],r[4],r[6],r[8])
          lis.append(reglas)
    return(lis)
#Simula la cinta
def cinta(lista):
    lis=["B"]*100
    i=1
    for c in lista[2]:
        lis[i]=c
        i+=1
    return lis
#Simula una MT
def turing():
    reglas=guardaEntrada(entrada)
    #Estados
    actual=reglas[0]
    final=reglas[1]
    cadena=reglas[2]
    cint=cinta(reglas)
    contador=1
    lr   =  listaReglas(reglas)
    print("Estado inicial: "+ actual+" Estado final: "+ final+" Cadena a revisar:"+cadena)
    b=True
    #Simulacion
    while b==True:
        for r in lr:
            if(cint[contador]==r.c1  and actual==r.q):
                print(r.q,r.c1)
                print(r.p,r.c2,r.m)
                cint[contador]=r.c2
                actual=r.p
                print(cint[:10])
                if(r.m=="R"):
                    contador+=1
                if(r.m=="L"):
                    contador-=1
        else:
            if(actual==final):
                print("Cadena aceptada")
                b=False
#Ejecucion.
turing()
