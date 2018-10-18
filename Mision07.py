#Autor: Damián Iván García Ravelo
#Matrícula: A01376354
#Programa que divide sin usar el símbolo de dividir y encuentra el número mayor introducido por el usuario.

def dividir(dividendo,divisor): #Función que depende de los valores dados por el usuario

    resta=dividendo #Se asigna al valor inicial de la resta, el valor inicial del dividendo
    contador=0 #El numero de veces restadas comienza en 0

    #Si la resta es más grande al divisor, seguirá restando, y las veces irán aumentando
    while resta>=divisor:
        resta = resta-divisor
        contador+=1

    print(dividendo,"/",divisor,"=",contador,", sobra",resta) #Imprime el resultado


def encontrarMayor(): #Función que encuentra el valor más grande dentro de los número ingresador por el usuario

    mayor=0 #Consideramos que 0 es el máximo valor inicial

    #Interacción con el usuario dando las instrucciones a seguir
    print("Teclea una serie de números para encontrar el mayor.")
    numero=int(input("Teclea un número [-1 para salir]: "))

    #Comenzamos el ciclo que será deteriorado si recibe el valor de -1
    while numero != -1:
        #Si el numero ingresado es mayor al máximo valor, el máximo valor guardará este como uno nuevo
        if numero>mayor:
            mayor=numero
        numero = int(input("Teclea un número [-1 para salir]: ")) #Seguirá preguntando datos al usuario

    if mayor == -1 : #Si el mayor es asignado con -1, significa no hay ningun valor máximo
        print("No hay valor mayor")
    else: print("El mayor es: " ,mayor) #De lo contrario, imprime el valor más grande

def leerOpcionMenu(): #Función que crea un menú para que el usuario seleccione que programa correr
    print("Mision 07: Ciclos while")
    print("Autor: Damián Iván García Ravelo")
    print("Matrícula: A01376354")
    print("1. Calcular divisiones")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcion = int(input("Teclea tu opción: ")) #Está en función del número de opción que eliga el usuario
    return opcion


def main():
    opcion=leerOpcionMenu() #Corre la opcion del menu dependiendo del valor recibido
    while opcion!=3: #Mientras que la opción salir no sea seleccionada:
        if opcion==1: #Correrá y preguntara las variables que necesita el primer programa para correr
            dividendo=int(input("Ingresa el valor del dividendo:"))
            divisor=int(input("Ingresa el valor del divisor: "))
            dividir(dividendo,divisor) #Llama a la función
        if opcion==2: #Correra el segundo programa
            encontrarMayor()
        if opcion<1 or opcion>3: #Si el número ingresado no es entre 1-3, solicitará un valor dentro de se rango
            print("Ingrese un valor en el rango permitido")
        opcion = leerOpcionMenu()
    print()#Si se selecciona salir, imprime la despedida
    print("Gracias por usar este programa, vuelve pronto.")




main() #Llama a la función principal