from datetime import date, datetime


class Transaccion:

    VENTA = "V"
    ABASTECIMIENTO = "A"
    
    def __init__(self,tipo, cantidad):
        self.tipo = tipo
        self.cantidad = cantidad
        self.fecha = datetime.now()


class Libro:

    def __init__(self, isbn, titulo, precio_venta, precio_compra, cantidad_actual):
        self._isbn = isbn
        self._titulo = titulo
        self.precio_venta = precio_venta
        self.precio_compra = precio_compra
        self._cantidad_actual = cantidad_actual
        self.transacciones = [] # --> Lista

    @property
    def isbn(self):
        return self._isbn

    @property
    def cantidad_actual(self):
        return self._cantidad_actual
    
    @cantidad_actual.setter
    def cantidad_actual(self, nuevo_valor):
        self._cantidad_actual = nuevo_valor


class Tienda:
    
    def __init__(self):
        self.dinero_en_caja = 1000000
        self.catalogo = {} # --> Diccionario 

    def registrar_libro_catalogo(self, isbn, titulo, precio_compra, precio_venta, cantidad_actual):
        if isbn not in self.catalogo.keys():
            libro = Libro(isbn, titulo, precio_compra, precio_venta, cantidad_actual)
            self.catalogo[isbn] = libro 
        else:
            raise Exception("El libro ya se encuentra en el catalogo")
            