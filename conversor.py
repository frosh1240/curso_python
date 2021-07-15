def convertir(tipo_pesos, dolar):
    pesos = input("¿Cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print ("Tienes $" + dolares + " dólares")


menu = """
    Bienvenido al conversor de monedas 
    
    1 - Pesos Colombianos
    2 - Pesos Argentinos
    3 - Pesos Mexicanos

    Elige una opción: 
"""

opcion = int(input(menu))
if opcion == 1:
    convertir("colombianos", 3875)
elif opcion ==2:
    convertir("argentinos", 65)
elif opcion == 3:    
    convertir("mexicanos", 24)
else:
    print("Ingrese una opción correcto")
