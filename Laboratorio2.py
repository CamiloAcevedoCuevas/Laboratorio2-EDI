# Laboratorio 2
# Desarrollado por Camilo Acevedo Cuevas

class Llamada:
    """Clase que representa una Llamada.

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
    """Clase que representa una lista enlazada simple.

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
    """Clase que representa una LlamadaPremium.

    Args:
        id (int): Identificador de la llamada
        nombre (str): Nombre del cliente
        estado (str): Estado de la llamada
        next (Llamada): Referencia al siguiente nodo
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
    pass

if __name__ == "__main__":
    main()