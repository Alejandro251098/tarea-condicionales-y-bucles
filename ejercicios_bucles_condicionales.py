# CONDICIONALES

# ejercicio 1 : VERIFICACION DE NUMERO PAR O IMPAR

# numero = int(input('Ingrese un numero entero'))

# if (numero % 2) == 0: 
#     print('Es par')
# else:
#     print('Es impar')
 


    
    
#  ejercicio 2 : Clasificacion de edades


# edad = int(input("ingrese sus edad"))

# if edad  < 18 :
#       print("eres menor de edad")
        
# elif edad >= 18 and edad <= 65 :
#          print("eres un adulto")
        
# else:  
#   print("eres un adulto mayor")  



# Ejercicio 3 :Calculadora de descuento

#precio = int(input("ingrese el valor del producto"))
# edad = int(input("ingrese su edad"))


# if edad < 18  :
#     print(precio*0.9)
 
# elif edad >= 65:
#     print(precio * 0.85)
    
# if edad >=18 and edad < 65 :
#     print(precio)  



# Ejercicio 4 : Clasificacion de notas 


# nota = int(input("ingrese un numero"))
 
# if nota >= 90 and nota <= 100 : 
#     print ("A : sobrealiente")

# elif nota >= 80 and nota <= 89 :   
#     print ("B: bueno")
# elif nota >=70 and nota <= 79 :
#     print ("C: satisfactorio")
# elif nota >= 60 and nota <= 69 :
#     print("D: necesita mejorar")

# else :
#    print("F: reprobado")


# Ejercicio 5 : calculo impuesto sobre la renta


# salario = int ( input("ingrese el valor de su salario anual"))

# if salario <= 10000  :
#    print  ("no se aplica impuesto")
# elif salario > 10000 and salario <= 50000 :
#    print ( salario * 0.1)
# elif salario > 50000 and salario <= 100000 :
#     print (salario * 0.2)

# else :
#     print ( salario * 0.3) 
   
   

# EJERCICIO BUCLES "while"


# Ejercicio 1 :Contador ascendente y descendente 

# ascendente = 0
# descendente = 11
# while ascendente < 10 :
#    ascendente += 1
#    descendente -= 1
#    print(ascendente , "/" , descendente) 


# Ejercicio 2 : Adivina el numero

# import random

# aleatoreo = random.randint( 1,100)
# adivina = 0

# while adivina != aleatoreo :
#     if adivina == 0 :
#         print ( "inicia el juego")
#     elif adivina < aleatoreo :
#         print ( "demasiado bajo")
        
#     else :
#         print ("demasaido alto")
#     adivina = int(input("ingresa el numero"))           
#  print("haz ganado")


# BUCLES "for "

# Ejercicio 1 : Tblas de multiplicar 

numeros = int(input('Ingrese un numero'))

# for multipos in range(1, 11):
#       resultado = numeros * multipos
#       print(numeros, '*', multipos, '=', resultado) 



# Ejercicio 2 : Suma de numeros pares

numero = int (input("ingrese un numero"))

for numeros_pares in range (2, numero  ) :
   numeros_pares =(numero % 2)  
   print( numeros_pares , numero )
    



