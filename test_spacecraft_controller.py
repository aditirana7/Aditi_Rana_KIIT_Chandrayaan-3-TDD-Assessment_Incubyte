import unittest
from spacecraft_controller import Spacecraft

class TestSpacecraftController(unittest.TestCase):

    def test_movement_forward(self):
        spacecraft = Spacecraft((0, 0, 0), 'N')
        spacecraft.execute_command('f')
        self.assertEqual(spacecraft.position, (0, 1, 0))

    def test_movement_backward(self):
        spacecraft = Spacecraft((0, 0, 0), 'N')
        spacecraft.execute_command('b')
        self.assertEqual(spacecraft.position, (0, -1, 0))

    def test_turn_right(self):
        spacecraft = Spacecraft((0, 0, 0), 'N')
        spacecraft.execute_command('r')
        self.assertEqual(spacecraft.direction, 'E')

    def test_turn_left(self):
        spacecraft = Spacecraft((0, 0, 0), 'N')
        spacecraft.execute_command('l')
        self.assertEqual(spacecraft.direction, 'W')

    def test_turn_up(self):
        spacecraft = Spacecraft((0, 0, 0), 'Up')  
        spacecraft.execute_command('u')
        self.assertEqual(spacecraft.direction, 'Up')

    def test_turn_down(self):
        spacecraft = Spacecraft((0, 0, 0), 'Down') 
        spacecraft.execute_command('d')
        self.assertEqual(spacecraft.direction, 'Down')

if __name__ == '__main__':
    unittest.main()
