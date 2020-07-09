import sys
import math
archivo = sys.argv[1] # Archivo que contiene la gramatica
cadena =  sys.argv[2] # Cadena a verificar dada por el usuario.

#Clase que ayuda a guardar la gramaticay sea mas facil acceder a
#sus elementos.
class Produccion(object):
    def __init__(self,simbolo,derivacion):
        self.derivacion = derivacion
        self.simbolo=simbolo

#Se lee del archivo de la gramatica dada guardandolo en una lista de
#producciones, tomando en cuenta como se especifico en la practica.
def gramatica(archivo):
    lista =[] #lista de produccione
    g = open(archivo)
    with g:
        linea= g.readline()
        while linea:
            linea.strip()
            produccion = ""
            for c in linea:
                if c != "-" and c != " " and c != ">" and c != "\n":
                    produccion += c
            #Separamos las cadenas sabes que la primera es el simbolo
            #y lo que resta la derivacion
            produccion = Produccion(produccion[0],produccion[1:])
            lista.append(produccion)
            linea = g.readline()
    return lista
    g.close()


#Funcion auxiliar que une dos subcadenas
def union(c1,c2):
    l = []
    for i in c1:
        for j in c2:
            l.append(i+j)
    return l


#Algoritmo CYK dinamico
def cyk(cadena):
    #Generamos la matriz
    m = [["-"]*len(cadena) for i in range(len(cadena))]
    #Cargamos la gramatica
    g = gramatica(archivo)
    #Vamos a meter a la matriz los simbolos de la forma A -> a
    for i in range(len(cadena)):
        f= ""
        for simbolo in g:
            if(cadena[i] == simbolo.derivacion):
                a =simbolo.simbolo
                f+= simbolo.simbolo
        #Aqui se mete correctamente a la matriz
        m[i][i] = f
    #Vamos a verificar si la cadena contiene simbolos de la forma
    #A -> AB
    c = len(cadena)-1
    acc =1
    for i in range(len(cadena)-1):
        n = acc
        for j in range(c):
            #Matematicamente Verificando la subcadena [j][acc]
            #Matriz Python   Verificando la subcadena [acc][j]
            #Sabremos que poner en m[acc][j]
            #Inicio de cadena
            ini = j
            f= ""
            for k in range (j,acc):
                # Verificando vecinos (A -> "A"  "B")
                sc1= str(m[ini][j])
                sc2= str(m[acc][ini+1])
                lsc = union(sc1,sc2)
                #lista de cadenas que se encuentran en la matriz
                for l in  lsc:
                    for s in g:
                        #Verificamos si se encuentra alguna coincidencia
                        #en la gramatica. Y la guardamos en la matriz
                        if(l == s.derivacion):
                            f+= s.simbolo
                            m[acc][j] = f
                        #else:
                        #debug,print(l + " != "+ s.derivacion)
                ini +=1
            acc +=1
        acc = n +1
        c-=1
    a = "Cadena rechazada"
    for i in m[len(cadena)-1][0]:
        if(i == "S"):
            a ="Cadena aceptada"
    print(a)

#Ejecucion del algoritmo.
cyk(cadena)
