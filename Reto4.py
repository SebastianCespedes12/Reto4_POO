class MenuItem:
    def __init__(self, name:str, price:float):
        self._name = name
        self._price = price
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    def get_price(self):
        return self._price
    
    def set_price(self, price):
        self._price = price
    
    def calcuar_precio_total(self, items):
        total = 0
        for i in items:
            total += i.get_price()
        return total
    
class Beverage(MenuItem):
    def __init__(self, name, price, size:str):
        super().__init__(name, price)
        self._size = size
        if size == "small":
            self._price = 1500
        elif size == "medium":
            self._price = 2000
        else:
            self._price = 3000
    
    def get_size(self):
        return self._size
    
    def set_size(self, size):
        self._size = size
        if size == "small":
            self._price = 1500
        elif size == "medium":
            self._price = 2000
        else:
            self._price = 3000

class MainCourse(MenuItem):
    def __init__(self, name , price, rice:bool, salad:bool):
        super().__init__(name, price)
        self._rice = rice
        self._salad = salad
        if rice == True:
            self._price += 2000
        if salad == True:
            self._price += 1500
    
    def get_rice(self):
        return self._rice
    
    def set_rice(self, rice):
        self._rice = rice
    
    def get_salad(self):
        return self._salad
    
    def set_salad(self, salad):
        self._salad = salad

class Apetizer(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)

class Dessert(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)

class Order:
    def __init__(self):
        self._orden = []
    
    def get_orden(self):
        return self._orden
    
    def set_orden(self, orden):
        self._orden = orden
    
    def anadir_orden(self, item: "MenuItem"):
        self._orden.append(item)
    
    def calcular_precio_total(self):
        total = 0
        tiene_plato_principal = False
        total_bebidas = 0
        
        for i in self._orden:
            if isinstance(i, MainCourse):
                tiene_plato_principal = True
            if isinstance(i, Beverage):
                total_bebidas += i.get_price()
            else:
                total += i.get_price()
        
        if tiene_plato_principal:
            total_bebidas *= 0.9
        
        total += total_bebidas
        return total
    
    def mostrar_orden(self):
        for i in self._orden:
            print(f"{i.get_name()} - {i.get_price()}")
        print(f"Total: {self.calcular_precio_total()}")

class Payment:
    def __init__(self, order: Order):
        self._order = order
    
    def get_order(self):
        return self._order
    
    def set_order(self, order):
        self._order = order
    
    def pago_en_efectivo(self, dinero_entregado):
        total = self._order.calcular_precio_total()
        if dinero_entregado >= total:
            cambio = dinero_entregado - total
            print(f"Pago en efectivo. Total a pagar: {total}")
            print(f"Dinero entregado: {dinero_entregado}")
            print(f"Cambio: {cambio}")
        else:
            print(f"Dinero insuficiente. Total: {total}, Entregado: {dinero_entregado}")
        
    def pago_con_tarjeta(self, saldo_cuenta):
        total = self._order.calcular_precio_total()
        if saldo_cuenta >= total:
            nuevo_saldo = saldo_cuenta - total
            print(f"Pago con tarjeta. Total a pagar: {total}")
            print(f"Saldo restante: {nuevo_saldo}")
        else:
            print(f"Saldo insuficiente. Total: {total}, Saldo disponible: {saldo_cuenta}")