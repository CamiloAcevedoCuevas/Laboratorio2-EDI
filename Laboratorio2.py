# Laboratorio 2
# Desarrollado por Camilo Acevedo Cuevas

#    ▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄   
#    █▒▒░░░░░░░░░▒▒█   
#     █░░█░░░░░█░░█    
#  ▄▄  █░░░▀█▀░░░█  ▄▄ 
# █░░█ ▀▄░░░░░░░▄▀ █░░█
# █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
# █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
# █░░║║║╠─║─║─║║║║║╠─░░█
# █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
# █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
class Llamada:
    """Clase que representa una llamada

    Args:
        id (int): Identificador de la llamada
        nombre (str): Nombre del cliente
        prioridad (str): Prioridad de la llamada
        estado (str): Estado de la llamada
        next (Llamada): Referencia a la siguiente llamada
    """

    def __init__(self, id, nombre, prioridad, estado):
        self.id = id
        self.nombre = nombre
        self.prioridad = prioridad
        self.estado = estado
        self.next = None
    
class ListaEnlazadaSimple:
    """Clase que representa una lista enlazada simple

    Args:
        head (Llamada): Referencia a la primera llamada de la lista

    Methods:
        add_llamada: Agrega una llamada a la lista
        del_llamada: Elimina la primera llamada de la lista
        get_llamadas: Muestra las llamadas de la lista
        get_llamada(id): Busca una llamada por su id
    """
    def __init__(self):
        self.head = None

    def add_llamada(self, id, nombre, prioridad, estado):
        new_llamada = Llamada(id, nombre, prioridad, estado)
        if self.head == None:
            self.head = new_llamada
        else:
            if (prioridad == "regular"):
                last = self.head
                while last.next != None:
                    last = last.next
                last.next = new_llamada
            else:
                new_llamada.next = self.head
                self.head = new_llamada

    def del_llamada(self, id):
        actual = self.head
        anterior = None
        while actual:
            if actual.id == id:
                if anterior:
                    anterior.next = actual.next
                else:
                    self.head = actual.next
                    print(f"\nLlamada {id} eliminada exitosamente.\n____________________________________________________________________")
                return
            anterior = actual
            actual = actual.next

    def get_llamadas(self):
        if self.head != None:
            actual = self.head
            while actual != None:
                print(f"\nID: {actual.id}, Nombre: {actual.nombre}, Prioridad: {actual.prioridad}, Estado: {actual.estado}")
                actual = actual.next

    def get_llamada(self, id):
        if self.head != None:
            actual = self.head
            while actual != None:
                if actual.id == id:
                    return actual
                actual = actual.next
        return None
    
class LlamadaPremium:
    """Clase que representa una llamada premium

    Args:
        id (int): Identificador de la llamada premium
        nombre (str): Nombre del cliente premium
        estado (str): Estado de la llamada premium
        next (LlamadaPremium): Referencia a la siguiente llamada premium
    """
    
    def __init__(self, id, nombre, prioridad, estado):
        self.id = id
        self.nombre = nombre
        self.prioridad = prioridad
        self.estado = estado
        self.next = None

class ListaEnlazadaCircular:
    """Clase que representa una lista enlazada circular

    Args:
        head (LlamadaPremium): Referencia a la primera llamada premium de la lista

    Methods:
        add_llamada_premium: Agrega una llamada premium a la lista
        del_llamada_premium: Elimina la primera llamada premium de la lista
        get_llamadas_premium: Muestra las llamadas premium de la lista
        get_llamada_premium(id): Busca una llamada premium por su id
    """
    def __init__(self):
        self.head = None

    def add_llamada_premium(self, id, nombre, prioridad, estado):
        new_llamada = LlamadaPremium(id, nombre, prioridad, estado)
        if self.head == None:
            self.head = new_llamada
            self.head.next = self.head
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = new_llamada
            new_llamada.next = self.head

    def del_llamada_premium(self):
        if self.head != None:
            if self.head.next == self.head:
                self.head = None
            else:
                actual = self.head
                while actual.next != self.head:
                    actual = actual.next
                actual.next = self.head.next
                self.head = self.head.next

    def get_llamadas_premium(self):
        if self.head != None:
            actual = self.head
            while actual.next != self.head:
                print(f"\nID: {actual.id}, Nombre: {actual.nombre}, Prioridad: {actual.prioridad}, Estado: {actual.estado}")
                actual = actual.next
            print(f"\nID: {actual.id}, Nombre: {actual.nombre}, Prioridad: {actual.prioridad}, Estado: {actual.estado}")

    def get_llamada_premium(self, id):
        if self.head != None:
            actual = self.head
            while actual != None:
                if actual.id == id:
                    return actual
                actual = actual.next
        return None
    
def main():
    lista = ListaEnlazadaSimple()
    lista_premium = ListaEnlazadaCircular()
    while True:
        print("\nMenu\n\n1. Agregar llamada\n2. Eliminar llamada\n3. Mostrar llamadas\n4. Buscar llamada\n5. Salir")
        while True:
            try:
                opc = int(input("\nIngrese una opción: "))
                if int(opc) >= 1 and int(opc) <= 5:
                    break
                else:
                    print("\nError: Ingrese una opción válida.")
            except ValueError:
                print("\nError: Ingrese un número.")
        if opc == 1:
            print("____________________________________________________________________\n\nAgregar llamada")
            while True:
                try:
                    id = int(input("\nIngrese el ID de la llamada: "))
                    if int(id) >= 0:
                        llamada = lista.get_llamada(id)
                        if llamada == None:
                            break
                        else:
                            print("\nError: El ID ya existe.")
                    else:
                        print("\nError: Ingrese un número positivo.")
                except ValueError:
                    print("\nError: Ingrese un número.")
            while True:
                nombre = input("\nIngrese el nombre del cliente: ")
                if nombre.isalpha():
                    break
                else:
                    print("\nError: Ingrese un texto.")
            while True:
                try:
                    prioridad = int(input("\nIngrese la prioridad de la llamada (1: Regular, 2: VIP, 3: Premium): "))
                    if int(prioridad) == 1 or int(prioridad) == 2 or int(prioridad) == 3:
                        break
                    else:
                        print("\nError: Ingrese una opción válida.")
                except ValueError:
                    print("\nError: Ingrese un número.")
            while True:
                try:
                    estado = int(input("\nIngrese el estado de la llamada (1: Pendiente, 2: En proceso, 3: Finalizada): "))
                    if int(estado) == 1 or int(estado) == 2 or int(estado) == 3:
                        break
                    else:
                        print("\nError: Ingrese una opción válida.")
                except ValueError:
                    print("\nError: Ingrese un número.")
            if prioridad == 1:
                prioridad = "Regular"
            elif prioridad == 2:
                prioridad = "VIP"
            else:
                prioridad = "Premium"
            if estado == 1:
                estado = "Pendiente"
            elif estado == 2:
                estado = "En proceso"
            else:
                estado = "Finalizada"
            if prioridad == "Premium":
                lista_premium.add_llamada_premium(id, nombre, prioridad, estado)
            else:
                lista.add_llamada(id, nombre, prioridad, estado)
            print("\nLlamada agregada exitosamente.\n____________________________________________________________________")
        elif opc == 2:
            print("____________________________________________________________________\n\nEliminar llamada")
            while True:
                try:
                    id = int(input("\nIngrese el ID de la llamada: "))
                    if int(id) >= 0:
                        if lista.get_llamada(id) != None:
                            lista.del_llamada(id)
                            break
                        elif lista_premium.get_llamada_premium(id) != None:
                            lista_premium.del_llamada_premium
                            print(f"\nLlamada {id} eliminada exitosamente.\n____________________________________________________________________")
                            break
                        else:
                            print("\nError: Llamada no encontrada.\n____________________________________________________________________")
                            break
                    else:
                        print("\nError: Ingrese un número positivo.")
                except ValueError:
                    print("\nError: Ingrese un número.")
        elif opc == 3:
            print("____________________________________________________________________\n\nMostrar llamadas:")
            lista.get_llamadas()
            lista_premium.get_llamadas_premium()
            print("\n____________________________________________________________________")
        elif opc == 4:
            print("____________________________________________________________________\n\nBuscar llamada")
            while True:
                try:
                    id = int(input("\nIngrese el ID de la llamada: "))
                    if int(id) >= 0:
                        llamada = lista.get_llamada(id)
                        if llamada == None:
                            llamada = lista_premium.get_llamada_premium(id)
                        if llamada == None:
                            print("\nError: Llamada no encontrada.\n____________________________________________________________________")
                            break
                        else:
                            print(f"\nID: {llamada.id}, Nombre: {llamada.nombre}, Prioridad: {llamada.prioridad}, Estado: {llamada.estado}\n____________________________________________________________________")
                            break
                    else:
                        print("\nError: Ingrese un número positivo.")
                except ValueError:
                    print("\nError: Ingrese un número.")
        elif opc == 5:
            break

if __name__ == "__main__":
    main()