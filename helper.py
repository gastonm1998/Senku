from os import system, name

class Helper():
    
    @staticmethod
    def limpiarPantalla():
        #Comando para windows
        if name == 'nt':
            system('cls')
      
        #Comando para unix
        else:
            system('clear')
    
    @staticmethod
    def pulsarTecla():
        input("Pulse una tecla para continuar...")
    
    @staticmethod
    def leerFilaColumna(dimension):
        fila = 0
        columna = 0
        while True:
            try:
                fila = int(input("Fila o 0 para salir: "))   
                             
                while (fila < 0 or fila > dimension):
                    fila = int(input("El número debe ser de 1 a " + str(dimension) + " : "))
                
                if fila == 0:
                    break
                    
                columna = int(input("Columna: "))
                
                while (columna < 1 or columna > dimension):
                    columna = int(input("El número debe ser de 1 a " + str(dimension) +  " : "))
                
                break

            except ValueError:
                print("No ha ingresado un número...")
                
        return fila, columna

    @staticmethod
    def leerDireccion():
        direccion = 0
        while True:
            try:
                direccion = int(input("Dirección: "))  
                
                while (direccion < 0 or direccion > 4):
                    direccion = int(input("El número debe ser de 1 a 4: "))                 
                break
                
            except ValueError:
                print("No ha ingresado un número...")
        
        return direccion
    
    @staticmethod
    def leerSiONo(mensaje):
        while True:
            opcion = input(mensaje)
            if opcion in 'Ss':
                return 'S'
            elif opcion in 'Nn':
                return 'N'
            else:
                print("Opcion inválida")

