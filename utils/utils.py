from manim import *
import json

def intro(self):
    intro_text = Text(
        "Learning How to Solve Backtracking",
        font="Comic Sans MS").scale(0.7)

    # Position the text at the top of the screen
    intro_text.to_edge(UP)
    intro_text.shift(DOWN)

    with_text = Text(
        "With",
        font="Comic Sans MS").scale(1).move_to(intro_text.get_center())

    with_text.next_to(intro_text, DOWN)

    # Create a Text object for "Nati"
    name_text = Text("Nati", font="Comic Sans MS", stroke_width=0).scale(3)
    name_text.next_to(with_text, DOWN * 2)

    # Animate the appearance of the introductory text
    self.play(FadeIn(intro_text), run_time=2)
    self.play(FadeIn(with_text), run_time=0.2)

    # Animate the writing of "Nati"
    self.play(Write(name_text), run_time=2)

    # Hold the final frame for a few seconds
    self.wait(2)

    self.play(FadeOut(intro_text), FadeOut(name_text), run_time=1)

    title = Text("Learning Backtracking", font="Arial", weight=BOLD, color=BLUE).scale(1.2)
    title.to_edge(UP, buff=0.5)
    title.shift(DOWN)

    # Part 1: Understanding the Problem
    understanding = Text(
        "1. Examples of Backtracking Questions",
        font="Arial", color=WHITE).scale(0.6)
    understanding.next_to(title, DOWN, buff=1)

    # Part 2: Example of Backtracking Questions
    examples = Text(
        "2. Understanding the Problem",
        font="Arial", color=WHITE).scale(0.6)
    examples.next_to(understanding, DOWN, buff=1)

    # Part 3: Solution Techniques
    solution = Text(
        "3. Solution Techniques",
        font="Arial", color=WHITE).scale(0.6)
    solution.next_to(examples, DOWN, buff=1)

    # Draw all parts to the screen
    self.play(Transform(with_text, title))
    self.play(FadeIn(understanding, shift=UP))
    self.play(FadeIn(examples, shift=UP))
    self.play(FadeIn(solution, shift=UP))

    # Hold the slide for a few seconds
    self.wait(2)

    self.play(FadeOut(with_text), FadeOut(solution), FadeOut(examples), FadeOut(understanding))



def generate_tree(self,start_coord, out_of_bound_nodes, visited_nodes, replace_nodes=None, show_animation=True, check_bounds=True):
    with open('nodes_position.json', 'r') as file:
        pos = json.load(file)
    pos = {int(key): value for key, value in pos.items()}
    labels = []
    arrows = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    color_good = BLUE
    color_out_of_bounds = RED
    color_visited = YELLOW

    for idx, (dx, dy) in enumerate(directions):
        out_of_bounds_or_visited = False
        end_coords = (start_coord[0] + dx, start_coord[1] + dy)
        node_color = color_good
        index1 = idx+2
        if check_bounds and index1 in out_of_bound_nodes:
            node_color = color_out_of_bounds
            out_of_bounds_or_visited = True
        if check_bounds and index1 in visited_nodes:
            node_color = color_visited
            out_of_bounds_or_visited = True

        new_label = Text(f"({end_coords[0]}, {end_coords[1]})", font_size=18, color=node_color)
        if replace_nodes:
            new_label = replace_nodes[index1]
        new_label.move_to(pos[idx + 2])
        new_label.shift(UP * 0.2)
        labels.append(new_label)

        arrow = Arrow(pos[1], new_label.get_top(), buff=0.2, color=node_color)
        arrows.append(arrow)

        if show_animation:
            self.play(Write(new_label), run_time=0.3)
            self.play(GrowArrow(arrow), run_time=0.5)

        if out_of_bounds_or_visited:
            continue

        for idx2, (dx2, dy2) in enumerate(directions):
            end_coords2 = (start_coord[0] + dx + dx2, start_coord[1] + dy + dy2)
            node_color2 = color_good
            index2 = (idx + 1) * 4 + idx2 + 2
            if check_bounds and index2 in out_of_bound_nodes:
                node_color2 = color_out_of_bounds
            if check_bounds and index2 in visited_nodes:
                node_color2 = color_visited

            new_label2 = Text(f"({end_coords2[0]}, {end_coords2[1]})", font_size=18, color=node_color2)
            if replace_nodes:
                new_label2 = replace_nodes[index2]
            new_label2.move_to(pos[index2])
            labels.append(new_label2)
            # Connect the new dot to the previous level
            arrow = Arrow(new_label.get_bottom(), new_label2.get_top(), buff=0.1, color=node_color2)
            arrows.append(arrow)

            if show_animation:
                self.play(Write(new_label2), run_time=0.3)
                self.play(GrowArrow(arrow), run_time=0.5)


    if not show_animation:
        self.play(Write(VGroup(*arrows)), Write(VGroup(*labels)))
    self.wait(1.43)

    return labels, arrows

