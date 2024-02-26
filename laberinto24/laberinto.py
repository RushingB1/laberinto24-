class Juego:
    def __init__(self):
        self.maze = None

    def crearPared(self):
        return Pared()
    
    def crearPuerta(self,lado1,lado2):
        puerta=Puerta(lado1,lado2)
        return puerta  
    
    def crearHabitacion(self, id):
        habitacion=Habitacion(id)
        habitacion.norte=self.crearPared()
        habitacion.este=self.crearPared()
        habitacion.sur=self.crearPared()
        habitacion.oeste=self.crearPared()
        return habitacion

    def crearMaze(self):
        return Maze()
    
    def crea2HabMazeFM(self):
        self.maze = self.crearMaze()
        habitacion1 = self.crearHabitacion(1)
        habitacion2 = self.crearHabitacion(2)
        puerta = self.crearPuerta(habitacion1,habitacion2)
        habitacion1.sur=puerta
        habitacion2.norte=puerta
        self.maze.añadirHabitacion(habitacion1)
        self.maze.añadirHabitacion(habitacion2)
        return self.maze
    
    def crea2HabsMaze(self):
        self.maze = Maze()
        habitacion1 = Habitacion(1)
        habitacion2 = Habitacion(2)
        self.maze.añadirHabitacion(habitacion1)
        self.maze.añadirHabitacion(habitacion2)

        puerta=Puerta(habitacion1,habitacion2)
        habitacion1.sur = puerta
        habitacion2.norte = puerta
        return self.maze

class JuegoBomba(Juego):
    def crear_pared(self):
        return ParedBomba()

class ElementoMapa:
    def __init__(self):
        pass
    def entrar(self):
        pass

class Contenedor(ElementoMapa):
    def __init__(self):
        self.hijos=[]
        
    def agregarHijo(self, hijo):
        self.hijos.append(hijo)
        
    def eliminarHijo(self, hijo):
        self.hijos.remove(hijo)


class Hoja(ElementoMapa):
    def accept(self, visitor):
        visitor.visitHoja(self)

class Decorador(Hoja):
    def __init__(self, componente):
        self.componente = componente

class Maze(Contenedor):
    def __init__(self):
        self.habitaciones = []
    
    def añadirHabitacion(self, habitacion):
        self.habitaciones.append(habitacion)
    
    def entrar(self):
        self.habitaciones[0].entrar()  

class Habitacion(Contenedor):
    def __init__(self,id):
        self.norte = None
        self.este = None
        self.oeste = None
        self.sur = None
        self.id = id
    
    def entrar(self):
        print("Entraste a la habitacion ", self.id)

class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
        self.abierta = False
    def entrar(self):
        if self.abierta:
            self.lado2.entrar()
        else:
            print("La puerta esta cerrada")
    
class Pared(ElementoMapa):
    def __init__(self):
        pass # Walls don't need additional attributes
    def entrar(self):
        print("No puedes entrar en una pared")

class ParedBomba(Pared):
    def __init__(self):
        self.activa = False   
    def entrar(self):
        if self.activa:
            print("La bomba ha explotado")
        else:
            return super().entrar()


juego = Juego()
juego.crea2HabsMaze()
juego.maze.entrar()

juego = Juego()
juego.crea2HabMazeFM()

juego=JuegoBomba()
juego.crea2HabMazeFM()
juego.maze.entrar() 



