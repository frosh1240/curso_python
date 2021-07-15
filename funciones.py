#def imprimir_mensaje():
#    print('Mensaje especial: ')
#    print('¡Estoy aprendiendo funciones')

#imprimir_mensaje()
#imprimir_mensaje()
#imprimir_mensaje()

def imprimir(opcion):
    mensaje = str(opcion)
    print('Hola')
    print("Elegiste la opcion " + mensaje)

opcion = int(input("Elige una opción (1,2,3): "))
if opcion == 1:
    imprimir(opcion)
elif opcion == 2:
    imprimir(opcion)
elif opcion == 3:
    imprimir(opcion)
else:
    input("error")