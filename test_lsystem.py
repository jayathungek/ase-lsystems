import unittest

from lsystem import LSystem


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

if __name__ == "__main__":
    unittest.main()

