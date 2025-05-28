# Reto4_POO
>1.Include the class exercise in the repo.
```python
import math
class Point:
  definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."
  def __init__(self, x: float=0, y: float=0):
    self.x = x
    self.y = y
  def move(self, new_x: float, new_y: float):
    self.x = new_x
    self.y = new_y
  def compute_distance(self, other: "Point") -> float:
    return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

class Line:
    def __init__(self, longitud:float, pendiente: float, punto_inicio:Point, punto_final:Point):
        self.longitud= longitud
        self.pendiente = pendiente
        self.punto_inicio = punto_inicio
        self.punto_final = punto_final
    #Metodos de la clase Line
    def calcular_longitud(self):
       distancia = math.sqrt((self.punto_final.x - self.punto_inicio.x)**2 + (self.punto_final.y - self.punto_inicio.y)**2) 
       return distancia
    def calcular_pendiente(self):
       opuesto = self.punto_final.y - self.punto_inicio.y
       adjacente = self.punto_final.x - self.punto_inicio.x
       angulo = (180/math.pi)*(math.atan(opuesto / adjacente))
       #Calculamos el angulo en grados
       if opuesto > 0 and adjacente > 0:
          return angulo
       if opuesto > 0 and adjacente < 0:
          return 180 - angulo
       if opuesto < 0 and adjacente < 0:
          return 180 + angulo
       if opuesto < 0 and adjacente > 0:
          return 360 - angulo

class Shapes:
    def __init__(self, vertices: list[Point], lados: list[Line], angulos: list[float]):
        self.vertices = vertices
        self.lados = lados
        self.angulos = angulos
    def calcular_area(self):
        pass
    def calcular_perimetro(self):
        perimetro = 0
        for lado in self.lados:
            perimetro += lado.calcular_longitud()
        return perimetro
    def calcular_angulos(self):

        return 180* (len(self.lados) - 2)
    
    def es_regular(self):
        for lado in self.lados:
            if lado.calcular_longitud() != self.lados[0].calcular_longitud():
                return False
        return True
    
class Rectangulo(Shapes):
    def __init__(self, vertices, lados, angulos):
        super().__init__(vertices, lados, angulos)

    def calcular_area(self):
        base = self.lados[0].calcular_longitud()
        altura = self.lados[1].calcular_longitud()
        return base * altura
            
class Cuadrado(Rectangulo):
    def __init__(self, vertices, lados, angulos):
        super().__init__(vertices, lados, angulos)
    

class Triangulo(Shapes):
    def __init__(self, vertices, lados, angulos):
        super().__init__(vertices, lados, angulos)
    
    def calcular_area(self):
        a = self.lados[0].calcular_longitud()
        b = self.lados[1].calcular_longitud()
        c = self.lados[2].calcular_longitud()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
``` 
>2.The restaurant revisted
Add setters and getters to all subclasses for menu item
Override calculate_total_price() according to the order composition (e.g if the order includes a main course apply some disccount on beverages)
Add the class Payment() following the class example
```python
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
```
