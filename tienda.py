from datetime import datetime
from functools import reduce


class Transaccion:

    VENTA = 1
    ABASTECIMIENTO = 2

    def __init__(self, tipo: int, cantidad: int):
        self._tipo: int = tipo
        self._cantidad: int = cantidad
        self._fecha = datetime.now()
    
    @property
    def tipo(self):
        return self._tipo
    
    @property
    def cantidad(self):
        return self._cantidad
    
    @property
    def fecha(self):
        return self._fecha    


class Libro:
    def __init__(self, isbn, titulo, precio_compra, precio_venta, cantidad_actual) -> None:
        self.isbn = isbn
        self.titulo = titulo
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self._cantidad_actual =  cantidad_actual
        self.transacciones = list()
    
    @property
    def cantidad_actual(self):
        return self._cantidad_actual
    
    @cantidad_actual.setter
    def cantidad_actual(self, nueva_cantidad):
        if nueva_cantidad < 0:
            raise Exception("La cantidad de unidades de un libro no puede ser negativa")
        
        self._cantidad_actual = nueva_cantidad
    
    def vender(self, cantidad) -> bool:
        """
        Vende una cantidad dada de ejemplares del libro. Si no hay esa cantidad, no se
        realiza la venta y el método retorna False. Si la venta se realiza, el método
        retorna True
        """
        if self.cantidad_actual >= cantidad:
            self.cantidad_actual -= cantidad
            transaccion = Transaccion(Transaccion.VENTA, cantidad)
            self.transacciones.append(transaccion)
            return True
        else:
            return False
    
    def abastecer(self, cantidad):
        self.cantidad_actual += cantidad
        transaccion = Transaccion(Transaccion.ABASTECIMIENTO, cantidad)
        self.transacciones.append(transaccion)
    
    def informar_ejemplares_vendidos(self) -> int:
        if len(self.transacciones) > 0:
            # cantidades = [t.cantidad for t in self.transacciones if t.tipo == Transaccion.VENTA]
            # total_ejemplares = reduce(lambda x, y: x + y, cantidades)
            # return total_ejemplares
            cantidad_ejemplares = 0
            for trans in self.transacciones:
                if trans.tipo == Transaccion.VENTA:
                    cantidad_ejemplares += trans.cantidad
            return cantidad_ejemplares
        else:
            return 0

    def __str__(self) -> str:
        return f"ISBN: {self.isbn}\nTítulo: {self.titulo}"   



class Tienda:
    def __init__(self) -> None:
        self.diner_en_caja = 1000000
        self.catalogo =  dict()
    
    def registrar_libro_en_catalogo(self, titulo, isbn, precio_venta, precio_compra, cantidad_actual):
        if isbn not in self.catalogo.keys():
            libro = Libro(isbn, titulo, precio_compra, precio_venta, cantidad_actual)
            self.catalogo[isbn] = libro
        else:
            raise Exception(f"Ya existe un libro con el ISBN {isbn}")
    
    def eliminar_libro_de_catalogo(self, isbn):
        if isbn in self.catalogo.keys():
            del self.catalogo[isbn]
        else:
            raise Exception(f"No existe un libro con el ISBN {isbn}")


libro = Libro("1234", "El principito", 50000, 60000, 10)
print(libro)