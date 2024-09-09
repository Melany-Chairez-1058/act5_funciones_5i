print("manejo de funciones V1")
def hola_mundo():
    print("Hola aqui estoy dentro de la funcion ")
def   mensa(msg):
    print(msg)
def escribeNC(nombre,apellido):    
    print(nombre,apellido)
    print( f" Tu nombre completo es: {nombre} {apellido}")
def suma2numeros(n1,n2):
    s=n1+n2    
    return f" La suma de {n1} + {n2} es:",s
    # Llamando a la funcion 
hola_mundo()
mensa("hola") #llama a mensa con 1 parametro
mensa("el profe me sorprendio enviando mensajes")#llama a mensa con 
escribeNC("Melany","chairez")
print(" \n Funciones que regresan valores")
print(suma2numeros(7,3))
print(suma2numeros(15,45))