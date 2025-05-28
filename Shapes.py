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

