# Laboratorio 2
# Desarrollado por Camilo Acevedo Cuevas

class Llamada:
    """Clase que representa una llamada

    Args:
        id (int): Identificador de la llamada
        nombre (str): Nombre del cliente
        prioridad (str): Prioridad de la llamada
        estado (str): Estado de la llamada
        next (Llamada): Referencia al siguiente nodo
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
        head (Llamada): Referencia al primer nodo de la lista

    Methods:
        add_llamada: Agrega un nodo a la lista
        del_llamada: Elimina el primer nodo de la lista
        print_llamadas: Muestra los nodos de la lista
        get_llamada(id): Busca un nodo por su id
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

    def del_llamada(self):
        if self.head != None:
            self.head = self.head.next

    def print_llamadas(self):
        if self.head != None:
            actual = self.head
            while actual != None:
                print("ID: " + str(actual.id) + ", Nombre: " + actual.nombre + ", Prioridad: " + str(actual.prioridad) + ", Estado: " + actual.estado)
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
    """Clase que representa una llamada premium.

    Args:
        id (int): Identificador de la llamada
        nombre (str): Nombre del cliente
        estado (str): Estado de la llamada
        next (LlamadaPremium): Referencia al siguiente nodo
    """
    
    def __init__(self, id, nombre, estado):
        self.id = id
        self.nombre = nombre
        self.estado = estado
        self.next = None

class ListaEnlazadaCircular:
    def __init__(self, head):
        self.head = None
        self.head.next =head

    def add_llamada_premium(self, id, nombre, estado):
        new_llamada = LlamadaPremium(id, nombre, estado)
        if self.head == None:
            self.head = new_llamada
            self.head.next = self.head
        else:
            actual = self.head
            while actual.next != self.head:
                actual = actual.next
            actual.next = new_llamada
            new_llamada.next = self.head

    def eliminar(self):
        if self.head != None:
            self.head = self.head.siguiente

    def mostrar(self):
        if self.head != None:
            actual = self.head
            while actual != self.tail:
                print("ID: " + str(actual.ID) + ", Nombre: " + actual.Nombre + ", Prioridad: " + str(actual.Prioridad) + ", Estado: " + actual.Estado)
                actual = actual.siguiente
            print("ID: " + str(self.tail.ID) + ", Nombre: " + self.tail.Nombre + ", Prioridad: " + str(self.tail.Prioridad) + ", Estado: " + self.tail.Estado)

    def buscar(self, id):
        if self.head != None:
            actual = self.head
            while actual != self.tail:
                if actual.ID == id:
                    return actual
                actual = actual.siguiente
            if self.tail.ID == id:
                return self.tail
        return None
    
def main():
    lista = ListaEnlazadaSimple()
    while True:
        print("\nMenu\n\n1. Agregar llamada\n2. Eliminar llamada\n3. Mostrar llamadas\n4. Buscar llamada\n5. Salir")
        while True:
            try:
                opc = int(input("\nIngrese una opción: "))
                if int(opc) >= 1 and int(opc) <= 5:
                    break
                else:
                    print("\nError: Ingrese una opción válida.\n\nIngrese una opción: ")
            except ValueError:
                print("\nError: Ingrese un número.")
        if opc == 1:
            print("\nAgregar llamada")
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
                    prioridad = int(input("\nIngrese la prioridad de la llamada (1: regular, 2: VIP): "))
                    if int(prioridad) == 1 or int(prioridad) == 2:
                        break
                    else:
                        print("\nError: Ingrese una opción válida.")
                except ValueError:
                    print("\nError: Ingrese un número.")
            while True:
                try:
                    estado = int(input("\nIngrese el estado de la llamada (1: pendiente, 2: en proceso, 3: finalizada): "))
                    if int(estado) == 1 or int(estado) == 2 or int(estado) == 3:
                        break
                    else:
                        print("\nError: Ingrese una opción válida.")
                except ValueError:
                    print("\nError: Ingrese un número.")
            if prioridad == 1:
                prioridad = "regular"
            else:
                prioridad = "VIP"
            if estado == 1:
                estado = "pendiente"
            elif estado == 2:
                estado = "en proceso"
            else:
                estado = "finalizada"
            if prioridad == "regular" and estado == "finalizado":
                pass
            else:
                lista.add_llamada(id, nombre, prioridad, estado)
        elif opc == 2:
            print("\nEliminar llamada")
            while True:
                try:
                    id = int(input("\nIngrese el ID de la llamada: "))
                    if int(id) >= 0:
                        break
                    else:
                        print("\nError: Ingrese un número positivo.")
                except ValueError:
                    print("\nError: Ingrese un número.")
            llamada = lista.get_llamada(id)
            if llamada != None:
                if llamada.estado == "finalizado":
                    lista.del_llamada()
                else:
                    print("\nError: La llamada no ha sido finalizada.")
            else:
                print("\nLlamada no encontrada")
        elif opc == 3:
            print("Mostrar llamadas")
            lista.print_llamadas()
            lista_premium.mostrar()
        elif opc == 4:
            print("Buscar llamada")
            id = int(input("Ingrese el ID de la llamada: "))
            llamada = lista.get_llamada(id)
            if llamada != None:
                print("ID: " + str(llamada.id) + ", Nombre: " + llamada.nombre + ", Prioridad: " + str(llamada.prioridad) + ", Estado: " + llamada.estado)
            else:
                print("Llamada no encontrada")
        elif opc == 5:
            break
        else:
            print("opc no valida")
    # lista = ListaEnlazadaSimple()
    # lista.add_llamada(1, "Juan", 1, "En espera")
    # lista.add_llamada(2, "Pedro", 2, "En espera")
    # lista.add_llamada(3, "Maria", 3, "En espera")
    # lista.print_llamadas()
    # print("Eliminando llamada...")
    # lista.del_llamada()
    # lista.print_llamadas()
    # print("Buscando llamada...")
    # llamada = lista.get_llamada(2)
    # if llamada != None:
    #     print("ID: " + str(llamada.id) + ", Nombre: " + llamada.nombre + ", Prioridad: " + str(llamada.prioridad) + ", Estado: " + llamada.estado)
    # else:
    #     print("Llamada no encontrada")


if __name__ == "__main__":
    main()