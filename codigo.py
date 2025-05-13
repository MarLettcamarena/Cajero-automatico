print("Bienvenido al cajero automatico")#mensaje de bienvenida
saldo= 24000 #saldo inicial
print("Por favor ingrese su numero de usuario y NIP")#mensaje de ingreso de datos
usuario=int(input("Numero de usuario: "))
int(input("NIP: "))
while True:#usamos True para que se siga usando el ciclo hasta que este use la opcion 4 de acabar el programa
    print("Menu de opciones: \n 1.Consultar estado de cuenta \n 2.Retirar dinero \n 3.Depositar dinero \n 4.Salir")#menu de opciones
    menu=int(input("Ingrese la opcion deseada: "))#ingreso de opcion
    if menu ==1:#estado de cuenta
      print("Consultar estado de cuenta")
      print("usuario consultor:", usuario)
      print("Su saldo es de: $",saldo)#se imprime el saldo
    elif menu==2: #retirar dinero
        print(f"el usuario {usuario} esta retirando dinero")
        retiro=int(input("cantidad que desee retirar: ")) #ingresa la cantidad del retiro
        print("Se retiro la cantidad de:",retiro)
        confirmar=input("Desea confirmar el retiro? (s/n): ")#confirmacion del retiro
        if confirmar == "n":#en caso de que el usuario no quiera confirmar el retiro
            print("Modificar la cantidad a retirar:")
            retiro=int(input("Reingresar cantidad a retirar: "))#se le pide al usuario que ingrese nuevamente la cantidad a retirar
        else:
            print("Retiro exitoso.")
            saldo= saldo - retiro #se resta el saldo inicial con el retiro
    elif menu ==3:#depodito de dinero
         print("depositar dinero")#mensaje de iniciacion 
         cuenta=int(input("cuenta a depositar: ")) #ingresar valores 
         deposito=int(input("Cantidad a depositar: "))
         print(f"Se deposito la cantidad de: {deposito} en la cuenta {cuenta}.")
         confirmar=input("Desea confirmar el deposito? (s/n): ")
         if confirmar == "n":#confirmacion del deposito
            print("Modificar la cuenta o la cantidad a depositar:")#mensaje de modificacion
            cuenta=input("Reingresar cuenta: ") #usamos nuevamente el nombre de las variables para modificar el valor
            deposito=input("Reingresar deposito: ")
         else:
           print("Deposito exitoso.")#En caso de que todo saliera bien, este mensaje se imprime
           saldo= saldo + deposito #se suma el saldo inicial con el deposito

    elif menu ==4:#salir del cajero
       print("Gracias por usar el cajero automatico.")
       break #deja de trabajar el programa y se cierra
    else:
      print("opcion no valida, intente de nuevo")#mensaje de error
#fin del programa
