from manim import *
from utils.utils import generate_tree

def define_paths_for_grid(axes):
    l_path = VMobject(color=GREEN, stroke_width=4)
    l_path.set_points_as_corners([axes.c2p(0, 0), axes.c2p(0, 7), axes.c2p(6, 7)])

    # Step-by-step path (zigzag for demonstration)
    step_path = VMobject(color=ORANGE, stroke_width=4)
    step_path.set_points_as_corners([
        axes.c2p(0, 0), axes.c2p(1, 0), axes.c2p(1, 1), axes.c2p(2, 1),
        axes.c2p(2, 2), axes.c2p(3, 2), axes.c2p(3, 3), axes.c2p(4, 3),
        axes.c2p(4, 4), axes.c2p(5, 4), axes.c2p(5, 5), axes.c2p(6, 5), axes.c2p(6, 7)
    ])

    # Additional Paths
    # Path 1: A simple straight path, taking a longer route
    path1 = VMobject(color=PURPLE, stroke_width=4)
    path1.set_points_as_corners([axes.c2p(0, 0), axes.c2p(10, 0), axes.c2p(10, 7), axes.c2p(6, 7)])

    # Path 2: A more direct but still detoured path
    path2 = VMobject(color=TEAL, stroke_width=4)
    path2.set_points_as_corners([
        axes.c2p(0, 0), axes.c2p(3, 0), axes.c2p(3, 3), axes.c2p(6, 3), axes.c2p(6, 7)
    ])

    # Path 3: Circuitous path to demonstrate variability
    path3 = VMobject(color=MAROON, stroke_width=4)
    path3.set_points_as_corners([
        axes.c2p(0, 0), axes.c2p(0, 10), axes.c2p(10, 10), axes.c2p(10, 7), axes.c2p(6, 7)
    ])
    return [l_path, step_path, path1, path2, path3]

def grid_preview(self):
    intro_text = Text("Pathfinding on a Grid", font_size=36, color=WHITE)
    explanation_text = Text("There is a grid, you can move only in four directions: UP, DOWN, LEFT, RIGHT",
                            font_size=24, color=WHITE)
    explanation2_text = Text("You need to get from (0,0) to (n,m).", font_size=24, color=WHITE)
    question1_text = Text("1. How long is the shortest path?", font_size=24, color=WHITE)
    question2_text = Text("2. How many shortest paths are there?", font_size=24, color=WHITE)
    question3_text = Text("3. How many different paths are there?", font_size=24, color=WHITE)

    # Position text objects
    intro_text.to_edge(UP)
    intro_text.shift(DOWN * 0.5)
    explanation_text.next_to(intro_text, DOWN)
    explanation2_text.next_to(explanation_text, DOWN)
    question1_text.next_to(explanation2_text, DOWN)
    question2_text.next_to(question1_text, DOWN)
    question3_text.next_to(question2_text, DOWN)

    # Display text sequentially
    self.play(Write(intro_text))
    self.wait(1)
    self.play(Write(explanation_text))
    self.wait(1)
    self.play(Write(explanation2_text))
    self.wait(1)
    self.play(Write(question1_text))
    self.wait(1)
    self.play(Write(question2_text))
    self.wait(1)
    self.play(Write(question3_text))
    self.wait(1.43)

    self.play(
        FadeOut(intro_text),
        FadeOut(explanation_text),
        FadeOut(explanation2_text),
        FadeOut(question1_text),
        FadeOut(question2_text),
        FadeOut(question3_text)
    )

def grid_visualising(self):
    # Axis and grid configuration
    axis_config = {
        "x_range": [0, 10, 1],  # min, max, step
        "y_range": [0, 10, 1],
        "axis_config": {
            "color": BLUE,
            "stroke_width": 2,
            "include_ticks": False,  # No need for ticks on every unit
            "numbers_to_exclude": [0]
        },
        "tips": True  # Arrow tips on the axes
    }
    axes = Axes(**axis_config)
    axes.center()

    # Prepare grid lines (but do not add them yet)
    grid_lines = VGroup()
    for x in range(11):  # Includes end point to cover the full range
        vertical_line = axes.get_vertical_line(axes.c2p(x, 10), color=LIGHT_GRAY, stroke_width=0.5)
        grid_lines.add(vertical_line)
    for y in range(11):
        horizontal_line = axes.get_horizontal_line(axes.c2p(10, y), color=LIGHT_GRAY, stroke_width=0.5)
        grid_lines.add(horizontal_line)

    # Animate grid lines appearing
    self.play(Create(axes), LaggedStart(*[Create(line) for line in grid_lines], lag_ratio=0.1), run_time=2)

    # Define and plot points of interest
    origin_point = Dot(axes.c2p(0, 0), color=BLUE, radius=0.1)
    target_point = Dot(axes.c2p(6, 7), color=RED, radius=0.1)
    origin_label = Text("(0,0)", font_size=14).next_to(origin_point, DOWN)
    target_label = Text("(6,7)", font_size=14).next_to(target_point, UP)
    self.add(origin_point, target_point, origin_label, target_label)

    # Path definitions
    paths = define_paths_for_grid(axes)

    # Animate paths
    for path in paths:
        self.play(Create(path), run_time=1.5)
        self.wait(0.5)
    self.wait(1.43)
    # Optionally, fade out paths after viewing
    self.play(*[FadeOut(path) for path in paths])

    self.wait(1.43)
    self.clear()

def groups_preview(self):

    # Title for the scene
    intro_text = Text("Grouping Problem on an Array", font_size=36, color=WHITE)
    intro_text.to_edge(UP)
    intro_text.shift(DOWN * 0.5)

    # Detailed explanation of the problem
    explanation_text = Text("Given an array, you must divide its elements into the smallest number of groups.",
                            font_size=24, color=WHITE).next_to(intro_text, DOWN, buff=0.25)

    explanation2_text = Text("Each group can contain a maximum sum of k.",
                             font_size=24, color=WHITE).next_to(explanation_text, DOWN, buff=0.25)

    # Specific question about the problem
    question_text = Text("What is the least amount of groups needed?",
                         font_size=24, color=WHITE).next_to(explanation2_text, DOWN, buff=0.25)

    # Displaying the texts sequentially with proper waits in between
    self.play(Write(intro_text))
    self.wait(1)
    self.play(Write(explanation_text))
    self.play(Write(explanation2_text))
    self.wait(1)
    self.play(Write(question_text))
    self.wait(1.43)

    # Optionally, fade out all text
    self.play(FadeOut(intro_text), FadeOut(explanation_text), FadeOut(explanation2_text),
              FadeOut(question_text))
    self.wait(1)

def group_and_animate(self, numbers, groups, array):
    # Colors for different groups
    colors = [RED, BLUE, GREEN, YELLOW, PURPLE]

    # Create groups and arrange them in a single line
    group_mobjects = VGroup()
    for i, group in enumerate(groups):
        group_text = VGroup(*[Text(str(num), font_size=24, color=colors[i % len(colors)]) for num in group])
        group_text.arrange(RIGHT, buff=0.2)
        group_mobjects.add(group_text)

    group_mobjects.arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
    group_mobjects.next_to(array, DOWN, buff=1)

    # Animate the creation of the groups
    for group_text, group in zip(group_mobjects, groups):
        self.play(TransformFromCopy(VGroup(*[array[numbers.index(num)] for num in group]), group_text))

    # Display the groups briefly
    groups_len_text = Text(f"Number of groups: {len(groups)}", font_size=30, color=WHITE)
    groups_len_text.to_edge(DOWN)
    groups_len_text.shift(UP * 0.5)
    self.play(Write(groups_len_text))
    self.wait(1.2)

    # Clean up the groups
    self.play(FadeOut(group_mobjects), FadeOut(groups_len_text))

def groups_visualising(self):
    max_sum_text = Text("Maximum sum per group: 100", font_size=36, color=WHITE)
    max_sum_text.to_edge(UP)
    max_sum_text.shift(DOWN * 0.5)

    # Array of numbers
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    array = VGroup(*[Text(str(num), font_size=36) for num in numbers])
    array.arrange(RIGHT, buff=0.2)
    array.next_to(max_sum_text, DOWN, buff=1)
    self.play(Write(max_sum_text))
    self.play(LaggedStart(*[FadeIn(mob) for mob in array], lag_ratio=0.04))

    # Initial grouping (example)
    initial_groups = [[10, 30, 60], [40, 50], [70], [20], [80], [90]]
    group_and_animate(self, numbers, initial_groups, array)
    self.wait(1.43)
    # Alternative grouping (example)
    alternative_groups = [[10, 90], [40, 60], [50], [30, 70], [20, 80]]
    group_and_animate(self, numbers, alternative_groups, array)

    self.play(FadeOut(array), FadeOut(max_sum_text))
    self.wait(1.43)

def backtracking_intro_guide(self):
    # Create an intro text for the scene
    question_text = Text("How to solve problems using backtracking?", font_size=36, color=WHITE)
    question_text.to_edge(UP)
    question_text.shift(DOWN * 0.5)
    self.play(Write(question_text))
    self.wait(1)

    # Explanation text about backtracking
    explanation_text = Text(
        "Backtracking aims to explore all potential solutions systematically,",
        font_size=24, color=WHITE
    ).next_to(question_text, DOWN, buff=0.5)

    explanation2_text = Text(
        "by making choices, and if a choice leads to a dead end, it backtracks to try another.",
        font_size=24, color=WHITE
    ).next_to(explanation_text, DOWN)

    solution_text = Text(
        "We want to go over all solutions in a systematic way.",
        font_size=24, color=WHITE
    ).next_to(explanation2_text, DOWN)

    # Display the explanation texts
    self.play(Write(explanation_text))
    self.play(Write(explanation2_text))
    self.play(Write(solution_text))
    self.wait(1.43)

    #cleanup
    self.play(FadeOut(question_text), FadeOut(explanation_text), FadeOut(explanation2_text),
              FadeOut(solution_text))

def generate_grid_full_tree(self):
    color_good = BLUE
    start_coord = (0, 0)
    start_label = Text(f"({start_coord[0]}, {start_coord[1]})", font_size=18, color=color_good)
    start_label.move_to([0, 2, 0])
    start_label.shift(UP * 0.2)
    self.play(Write(start_label), run_time=0.3)
    visited_nodes = [4,10,12,18]
    out_of_bounds = [5,9,11,13,14,15,16,17,19,20]
    labels, arrows = generate_tree(self, start_coord, visited_nodes, show_animation=False, check_bounds=False)

    out_of_bounds_labels = [labels[idx-1] for idx in out_of_bounds]
    visited_nodes_labels = [labels[idx-1] for idx in visited_nodes]
    self.play(*[vgroup.animate.scale(1.2).set_color(RED) for vgroup in out_of_bounds_labels])
    self.play(*[vgroup.animate.scale(1.2).set_color(YELLOW) for vgroup in visited_nodes_labels])
    self.wait(1.43)
    self.play(FadeOut(VGroup(*arrows)), FadeOut(VGroup(*labels)), FadeOut(start_label))

def generate_grid_tree(self):

    color_good = BLUE
    start_coord = (0, 0)
    start_label = Text(f"({start_coord[0]}, {start_coord[1]})", font_size=18, color=color_good)
    start_label.move_to([0, 2, 0])
    start_label.shift(UP * 0.2)

    start_label1 = Text("(0, 1)", font_size=18, color=BLUE)
    start_label1.move_to([2, 2.5, 0])

    start_coord2 = (0, 2)
    start_label2 = Text(f"({start_coord2[0]}, {start_coord2[1]})", font_size=18, color=color_good)
    start_label2.move_to([0, 2, 0])
    start_label2.shift(UP * 0.2)

    start_coord3 = (1, 2)
    start_label3 = Text(f"({start_coord3[0]}, {start_coord3[1]})", font_size=18, color=color_good)
    start_label3.move_to([0, 2, 0])
    start_label3.shift(UP * 0.2)

    #play first round
    self.play(Write(start_label), run_time=0.3)
    visited_nodes = [8,13]
    labels, arrows = generate_tree(self,start_coord, visited_nodes)
    self.play(FadeOut(VGroup(*arrows)), FadeOut(VGroup(*labels)))

    self.play(start_label.animate.move_to([4, 3, 0]))
    self.play(Write(start_label1))

    #play second round
    arrow0_1 = Arrow(start_label.get_bottom(), start_label1.get_right(), buff=0.1, color=color_good)
    self.play(Create(arrow0_1))
    arrow1_2 = Arrow(start_label1.get_bottom(),start_label2.get_right(), buff=0.1, color=color_good)
    self.play(Create(arrow1_2))

    self.play(Write(start_label2))
    visited_nodes2 = [4, 8, 13]
    labels, arrows = generate_tree(self, start_coord2, visited_nodes2)
    self.play(FadeOut(VGroup(*arrows)), FadeOut(VGroup(*labels)))

    # play third round
    obj_list = [start_label, start_label1, start_label2, arrow0_1, arrow1_2]
    self.play(*[vgroup.animate.shift(RIGHT*2 + UP*0.5) for vgroup in obj_list])

    arrow2_3 = Arrow(start_label2.get_bottom(), start_label3.get_right(), buff=0.1, color=color_good)
    self.play(Create(arrow2_3))

    self.play(Write(start_label3))
    visited_nodes3 = [5,8,13,14,17]
    labels, arrows = generate_tree(self, start_coord3, visited_nodes3)
    obj_list.append(arrow2_3)
    obj_list.append(start_label3)
    self.play(FadeOut(VGroup(*arrows)), FadeOut(VGroup(*obj_list)), FadeOut(VGroup(*labels)))








