from typing import Dict, List
from pen import Pen

class LSystem:
    rules: Dict[str, str]

    def set_rules(self, rules: Dict[str, str]):
        self.rules = rules

    def generate_next_state(self, current_state: str):
        new_state = ""
        for character in current_state:
            if character in self.rules.keys():
                new_state = new_state + self.rules[character]
            else:
                new_state = new_state + character
        return new_state
    

class LTree(LSystem):
    length: int
    thickness: int
    colour: str
    angle: int
    pen: Pen
    drawing_stack: List[Dict]
    state_history: List[str]

    def __init__(
        self,
        axiom: str,
        rules: Dict[str, str],
        length: int,
        thickness: int,
        colour: str,
        angle: int
    ):
        LSystem.__init__(self)
        self.length = length
        self.thickness = thickness
        self.colour = colour
        self.angle = angle
        self.rules = rules
        self.state_history = [axiom]
        self.drawing_stack = []
        self.pen = Pen(
            image_dimensions=(1000, 1000),
            pen_pos=(500, 1000),
            width=3
        )
        self.pen.set_heading(-90)


    def generate(self, iterations: int):
        for _ in range(iterations):
            current_state = self.state_history[-1]
            new_state = self.generate_next_state(current_state)
            self.state_history.append(new_state)

    def draw(self, command: str):
        if command == "L" or command == "I":
            self.pen.forward(self.length)
        elif command == "[":
            pen_state = {
                "position": self.pen.get_pos(),
                "heading": self.pen.get_heading()
            }
            self.drawing_stack.append(pen_state)
            self.pen.left(self.angle)
        elif command == "]":
            pen_state = self.drawing_stack.pop()
            self.pen.up()
            self.pen.set_pos(pen_state["position"])
            self.pen.set_heading(pen_state["heading"])
            self.pen.right(self.angle)
            self.pen.down()

    def create_image(self):
        state = self.state_history[-1]
        self.pen.down()
        for command in state:
            self.draw(command)
        self.pen.up()

    def save(self, filename: str):
        self.pen.save(filename)


if __name__ == "__main__":
    rules = {"L": "I[L]L", "I": "II"}
    axiom = "L"
    ltree = LTree(
        axiom=axiom,
        rules=rules,
        length=5,
        thickness=3,
        angle=35,
        colour="#4C4C4C"
    )
    ltree.generate(6)
    ltree.create_image()
    ltree.save("binary_tree.png")
