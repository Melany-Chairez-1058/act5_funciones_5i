print("Funciones creadas por el usuario ")
def Mi_lista():
    amigos=["Homero","Paty","Lety"]
    for nava in amigos:
        print(nava)
def Mi_tupla():
    peliculas=("el libro de la vida","luna de miel en familia","son como niños")
    for peli in peliculas:
        print(peli)   
def Mi_conjunto():
    libros={"Harry Potter","Crepusculo","Los juegos del Hambre"}
    for libro in libros:
        print(libro)     
def Mi_diccionario():
    personas={"Harry":"Gryffindor","Draco":"Slytherin","Luna":"Ravenclaw"}
    for casas in personas:
        print(casas)                
#llamadas a funciones
print(" \n lista")
Mi_lista() 
print("\n Tupla")
Mi_tupla()  
print("\n Conjunto")
Mi_conjunto()  
print("\n Diccionario")  
Mi_diccionario()