import unittest

from pen import Pen
from lsystem import LSystem, LTree


class TestLSystem(unittest.TestCase):
    # This function is run before every test
    def setUp(self):
        self.iterations = 2 
        self.lsystem = LSystem()

    def test_replacement_rules1(self):
        # define rules and axiom for testing
        rules = {"a": "b", "b": "a"}
        state = "aba"
        self.lsystem.set_rules(rules)

        for _ in range(self.iterations):
            state = self.lsystem.generate_next_state(state)

        # Check if final answer is what we would expect
        self.assertEqual(state, "aba")


class TestPen(unittest.TestCase):
    def setUp(self):
        self.pen = Pen(
            image_dimensions=(1000, 1000),
            pen_pos=(500, 1000),
            width=3
        )
        self.pen.set_heading(-90)

    def test_position(self):
        new_positions = [
            (x, y) 
            for x in range(0, 1000, 100)
            for y in range(0, 1000, 100)
        ]

        for pos in new_positions:
            self.pen.set_pos(pos)
            self.assertEqual(pos, self.pen.pos)
    
    def test_move_up(self):
        distance = 50
        self.pen.forward(distance)
        self.assertEqual(self.pen.pos, (500, 950))
        
    def test_move_left(self):
        distance = 50
        self.pen.left(90)
        self.pen.forward(distance)
        self.assertEqual(self.pen.pos, (450, 1000))

if __name__ == "__main__":
    unittest.main()

