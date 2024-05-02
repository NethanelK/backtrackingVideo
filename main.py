# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from manim import *


class One(Scene):

    def construct(self):
        intro_text = Text("Grid Backtracking Exploration", font_size=36, color=WHITE)
        intro_text.to_edge(UP)
        self.play(Write(intro_text))
        # Define the starting position and create the main node
        start_pos = np.array([0, 2, 0])  # Start at the center top
        start_dot = Dot(start_pos, color=RED)
        start_label = Text("(0,0)", font_size=24, color=BLUE).next_to(start_dot, UP, buff=SMALL_BUFF)
        self.play(Write(start_label))
        all_scene = VGroup()
        all_scene.add(intro_text)
        all_scene.add(start_label)
        # Generate the tree vertically downwards
        self.generate_tree(start_dot, (0, 0), 2, 0, start_label, all_scene)
        self.wait(2)
        self.play(FadeOut(all_scene))

    def generate_tree(self, start_dot, start_coords, depth, in_level, start_label, all_scene):
        if depth == 0:
            return
        print("starting: ", start_coords)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        level_distance = 1  # Vertical spacing between levels
        nodes = VGroup(start_dot)
        new_nodes = VGroup()
        labels = []

        # Calculate positions for the next level
        for idx, (dx, dy) in enumerate(directions):
            end_coords = (start_coords[0] + dx, start_coords[1] + dy)
            print("adding", end_coords)
            color = LIGHT_PINK
            if end_coords == (0, 0):
                color = RED
            elif end_coords[0] < 0 or end_coords[1] < 0:
                color = YELLOW_C
            new_label = Text(f"({end_coords[0]}, {end_coords[1]})", font_size=18, color=color)

            new_dot = Dot(color=BLUE)

            if idx == 0:
                new_dot.next_to(nodes, DOWN, buff=level_distance)
                if in_level == 0:
                    if depth == 2:
                        new_dot.shift(LEFT * 5)
                    else:
                        new_dot.shift(LEFT * 1)
                else:
                    new_dot.shift(LEFT * 1)
            else:
                if depth == 2:
                    new_dot.next_to(new_nodes, RIGHT, buff=3)
                else:
                    new_dot.next_to(new_nodes, RIGHT, buff=0.6)

            new_label.next_to(new_dot, DOWN)
            new_label.shift(UP*0.2)
            new_nodes.add(new_dot)
            self.play(Write(new_label), run_time=0.3)

            # Connect the new dot to the previous level
            arrow = Arrow(start_label.get_bottom(), new_label.get_top(), buff=0.1, color=color)
            self.play(GrowArrow(arrow), run_time=0.5)
            labels.append(new_label)
            all_scene.add(new_label)
            all_scene.add(arrow)
            i = 0
            self.generate_tree(new_dot, (end_coords[0], end_coords[1]), depth - 1, i, new_label,
                                   all_scene)


def print_hi(name):
    One().construct()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
