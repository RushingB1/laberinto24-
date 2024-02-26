import unittest
from laberinto import Juego, Maze, Habitacion, Puerta

class TestMazeGame(unittest.TestCase):

    def test_create_maze(self):
        game = Juego()
        maze = game.createMaze2HabFM()
        
        self.assertIsInstance(maze, Maze)
        
        rooms = maze.habitaciones
        self.assertEqual(len(rooms), 2)
        
        room1, room2 = rooms
        
        self.assertIsInstance(room1, Habitacion)
        self.assertIsInstance(room2, Habitacion)
        
        # Verificar paredes y puertas
        self.assertIsNotNone(room1.north) 
        self.assertIsNotNone(room1.south)
        self.assertIsNotNone(room1.east)
        self.assertIsNotNone(room1.west)
        
        self.assertIsNotNone(room2.north)
        self.assertIsNotNone(room2.south)
        self.assertIsNotNone(room2.east)
        self.assertIsNotNone(room2.west)  
        
        # Verificar que las paredes sean distintas instancias
        self.assertIsNot(room1.north, room2.north)
        self.assertIsNot(room1.south, room2.south)
        
        #verifica que al sur de room1 hay un objeto de tipo puerta
        self.assertIsInstance(room1.south, Puerta)


if __name__ == '__main__':
    unittest.main()