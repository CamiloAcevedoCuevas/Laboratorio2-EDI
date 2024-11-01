class Llamada:
    """Clase que representa una llamada."""
    def __init__(self, id, nombre, prioridad, estado):
        self.id = id
        self.nombre = nombre
        self.prioridad = prioridad
        self.estado = estado
        self.next = None
    
class ListaEnlazadaSimple:
    """Clase que representa una lista enlazada simple."""
    def __init__(self):
        self.head = None

    def add_llamada(self, id, nombre, prioridad, estado):
        """Agrega una llamada a la lista

        Args:
            id (int): Identificador del cliente.
            nombre (str): Nombre del cliente.
            prioridad (int): Prioridad de la llamada.
            estado (int): Estado de la llamada.
        """
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
        """Elimina una llamada por su id.

        Args:
            id (int): Identificador del cliente.
        """
        actual = self.head
        anterior = None
        while actual:
            if actual.id == id:
                if anterior:
                    anterior.next = actual.next
                else:
                    self.head = actual.next
                return
            anterior = actual
            actual = actual.next

    def get_llamadas(self):
        """Muestra las llamadas de la lista."""
        if self.head != None:
            actual = self.head
            while actual != None:
                print(f"---- ID del cliente: {actual.id}, Nombre del cliente: {actual.nombre}, Prioridad de la llamada: {actual.prioridad}, Estado de la llamada: {actual.estado}")
                actual = actual.next

    def get_llamada(self, id):
        """Busca una llamada por su id.

        Args:
            id (int): Identificador del cliente.

        Returns:
            actual: Llamada encontrada.
        """
        if self.head != None:
            actual = self.head
            while actual != None:
                if actual.id == id:
                    return actual
                actual = actual.next
        return None
    
class LlamadaPremium:
    """Clase que representa una llamada premium."""
    def __init__(self, id, nombre, prioridad, estado):
        self.id = id
        self.nombre = nombre
        self.prioridad = prioridad
        self.estado = estado
        self.next = None

class ListaEnlazadaCircular:
    """Clase que representa una lista enlazada circular."""
    def __init__(self):
        self.head = None

    def add_llamada_premium(self, id, nombre, prioridad, estado):
        """Agrega una llamada premium a la lista.

        Args:
            id (int): Identificador del cliente.
            nombre (str): Nombre del cliente.
            prioridad (int): Prioridad de la llamada.
            estado (int): Estado de la llamada.
        """
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

    def del_llamada_premium(self, id):
        """Elimina una llamada premium por su id.

        Args:
            id (int): Identificador del cliente.
        """
        actual = self.head
        anterior = None
        while actual:
            if actual.id == id:
                if anterior:
                    anterior.next = actual.next
                else:
                    self.head = actual.next
                return
            anterior = actual
            actual = actual.next

    def get_llamadas_premium(self):
        """Muestra las llamadas premium de la lista."""
        if self.head != None:
            actual = self.head
            while actual.next != self.head:
                print(f"---- ID del cliente: {actual.id}, Nombre del cliente: {actual.nombre}, Prioridad de la llamada: {actual.prioridad}, Estado de la llamada: {actual.estado}")
                actual = actual.next
            print(f"---- ID del cliente: {actual.id}, Nombre del cliente: {actual.nombre}, Prioridad de la llamada: {actual.prioridad}, Estado de la llamada: {actual.estado}")

    def get_llamada_premium(self, id):
        """Busca una llamada premium por su id.

        Args:
            id (int): Identificador del cliente.

        Returns:
            actual: Llamada premium encontrada.
        """
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
    print("\nMenú\n")
    while True:
        print("1. Agregar llamada\n2. Eliminar llamada\n3. Mostrar llamadas\n4. Buscar llamada\n5. Salir")
        while True:
            try:
                opc = int(input("\nIngrese una opción: "))
                if int(opc) >= 1 and int(opc) <= 5:
                    break
                else:
                    print("Error: Ingrese una opción válida.")
            except ValueError:
                print("Error: Ingrese un número.")
        print()
        if opc == 1:
            while True:
                try:
                    id = int(input("Ingrese el ID del cliente: "))
                    if int(id) >= 0:
                        llamada = lista.get_llamada(id)
                        if llamada == None:
                            break
                        else:
                            print("Error: El ID ya existe.")
                    else:
                        print("Error: Ingrese un número positivo.")
                except ValueError:
                    print("Error: Ingrese un número.")
            while True:
                nombre = input("Ingrese el nombre del cliente: ")
                if nombre.isalpha():
                    break
                else:
                    print("Error: Ingrese un texto.")
            while True:
                try:
                    prioridad = int(input("Ingrese la prioridad de la llamada (1. Regular, 2. VIP, 3. Premium): "))
                    if int(prioridad) == 1 or int(prioridad) == 2 or int(prioridad) == 3:
                        break
                    else:
                        print("Error: Ingrese una opción válida.")
                except ValueError:
                    print("Error: Ingrese un número.")
            while True:
                try:
                    estado = int(input("Ingrese el estado de la llamada (1.Pendiente, 2.En proceso, 3.Finalizada): "))
                    if int(estado) == 1 or int(estado) == 2 or int(estado) == 3:
                        break
                    else:
                        print("Error: Ingrese una opción válida.")
                except ValueError:
                    print("Error: Ingrese un número.")
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
            print()
        elif opc == 2:
            while True:
                try:
                    id = int(input("Ingrese el ID del cliente: "))
                    if int(id) >= 0:
                        if lista.get_llamada(id) != None:
                            lista.del_llamada(id)
                            print("\nLlamada eliminada.")
                            break
                        elif lista_premium.get_llamada_premium(id) != None:
                            lista_premium.del_llamada_premium(id)
                            print("\nLlamada eliminada.")
                            break
                        else:
                            print("Error: Llamada no encontrada.")
                            break
                    else:
                        print("Error: Ingrese un número positivo.")
                except ValueError:
                    print("Error: Ingrese un número.")
            print()
        elif opc == 3:
            lista.get_llamadas()
            lista_premium.get_llamadas_premium()
            print()
        elif opc == 4:
            while True:
                try:
                    id = int(input("Ingrese el ID del cliente: "))
                    if int(id) >= 0:
                        llamada = lista.get_llamada(id)
                        if llamada == None:
                            llamada = lista_premium.get_llamada_premium(id)
                        if llamada == None:
                            print("Error: Llamada no encontrada.")
                            break
                        else:
                            print(f"\n---- Nombre del cliente: {llamada.nombre}, Prioridad de la llamada: {llamada.prioridad}, Estado de llamada: {llamada.estado}")
                            break
                    else:
                        print("Error: Ingrese un número positivo.")
                except ValueError:
                    print("Error: Ingrese un número.")
            print()
        elif opc == 5:
            break

if __name__ == "__main__":
    main()