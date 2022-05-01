import unittest
import main

class positionInput(unittest.TestCase):
    def testConstructor(self):
        testRover = main.Rover(5, 5, 5, 5, 'N')
        self.assertEqual(testRover.x, 5)
        self.assertEqual(testRover.y, 5)

class borderInput(unittest.TestCase):
    def testConstructor(self):
        testRover = main.Rover(5, 5, 5, 5, 'N')
        self.assertEqual(testRover.borderX, 5)
        self.assertEqual(testRover.borderY, 5)

class directionInput(unittest.TestCase):
    def testConstructor(self):
        testRover = main.Rover(5, 5, 5, 5, 'N')
        self.assertEqual(testRover.direction, 'N')

class turnLeft(unittest.TestCase):
    def testConstructor(self):
        testRover = main.Rover(5, 5, 5, 5, 'N')
        testRover.turnLeft()
        self.assertEqual(testRover.direction, 'W')

class turnRight(unittest.TestCase):
    def testConstructor(self):
        testRover= main.Rover(5, 5, 5, 5, 'W')
        testRover.turnRight()
        self.assertEqual(testRover.direction, 'N')

class moveForward(unittest.TestCase):
    def testConstructor(self):
        testRover= main.Rover(0, 0, 5, 5, 'N')
        testRover.moveForward()
        self.assertEqual(testRover.x, 0)
        self.assertEqual(testRover.y, 1)

class northBorder(unittest.TestCase):
    def testConstructor(self):
        testRover= main.Rover(5, 5, 5, 5, 'N')
        testRover.moveForward()
        self.assertEqual(testRover.x, 5)
        self.assertEqual(testRover.y, 5)

class eastBorder(unittest.TestCase):
    def testConstructor(self):
        testRover= main.Rover(5, 5, 5, 5, 'E')
        testRover.moveForward()
        self.assertEqual(testRover.x, 5)
        self.assertEqual(testRover.y, 5)

class southBorder(unittest.TestCase):
    def testConstructor(self):
        testRover= main.Rover(0, 0, 5, 5, 'S')
        testRover.moveForward()
        self.assertEqual(testRover.x, 0)
        self.assertEqual(testRover.y, 0)

class westBorder(unittest.TestCase):
    def testConstructor(self):
        testRover= main.Rover(0, 0, 5, 5, 'W')
        testRover.moveForward()
        self.assertEqual(testRover.x, 0)
        self.assertEqual(testRover.y, 0)

if __name__ == '__main__':
    unittest.main()

