from manim import *
import networkx as nx

class Nati(Scene):

    def construct(self):
        self.sceneOpen()
        self.sceneOne()
        self.sceneTwo()
        self.sceneThree()
        self.sceneFour()
        self.sceneFive()
        self.sceneSix()
        # self.sceneSeven()
        self.sceneEight()
        self.sceneNine()
        self.sceneTen()
        self.sceneEleven()
        self.sceneSix(False)
        self.sceneTwelve()
        self.sceneTherteen()
        self.sceneNine()

    def sceneOpen(self):
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
            "1. Understanding the Problem",
            font="Arial", color=WHITE).scale(0.6)
        understanding.next_to(title, DOWN, buff=1)

        # Part 2: Example of Backtracking Questions
        examples = Text(
            "2. Examples of Backtracking Questions",
            font="Arial", color=WHITE).scale(0.6)
        examples.next_to(understanding, DOWN, buff=1)

        # Part 3: Solution Techniques
        solution = Text(
            "3. Solution Techniques",
            font="Arial", color=WHITE).scale(0.6)
        solution.next_to(examples, DOWN, buff=1)

        # Draw all parts to the screen
        self.play(Transform(with_text,title))
        self.play(FadeIn(understanding, shift=UP))
        self.play(FadeIn(examples, shift=UP))
        self.play(FadeIn(solution, shift=UP))

        # Hold the slide for a few seconds
        self.wait(2)

        self.play(FadeOut(with_text),FadeOut(solution),FadeOut(examples),FadeOut(understanding))

    def sceneOne(self):
        world = Rectangle(width=5.0, height=4.0)
        world.set_fill(BLUE, opacity=0.2)
        world.set_stroke(BLUE, width=1)

        world_label = Text("Universe", color=WHITE).scale(0.5).next_to(world, UP)

        objects = ["12", "(456, 789, -143)", "asdqwe", ":)"]
        dot_positions = [(1.55, 0.70, 0), (-0.36, -0.65, 0), (-0.98, 0.69, 0), (-1.58, -1.09, 0)]

        self.play(Create(world))
        self.play(Write(world_label))
        self.wait(1.43)

        # Create and animate dots with arrows and objects
        for i, pos in enumerate(dot_positions):
            dot = Dot().move_to(pos)
            arrow = Arrow(world.get_top(), dot.get_center(), buff=0, color=YELLOW,
                          stroke_width=1)
            self.play(Create(dot), GrowArrow(arrow))
            obj = Text(objects[i], color=WHITE).scale(0.5).next_to(dot, DOWN)
            self.play(Write(obj))
            self.wait(1)
            if i != len(dot_positions) - 1:
                self.play(FadeOut(dot), FadeOut(arrow), FadeOut(obj))

        self.wait(1.43)
        self.clear()

    def sceneTwo(self):

        world = Rectangle(width=5.0, height=4.0)
        world.set_fill(BLUE, opacity=0.2)
        world.set_stroke(BLUE, width=1)
        world_label = Text("Universe", color=WHITE).scale(0.5).next_to(world, LEFT)

        q1 = Text("1+1?", color=WHITE).scale(0.5).next_to(world, UP)

        objects = ["2"]
        dot_positions = [(1.55, 0.70, 0)]

        self.play(Create(world), Write(world_label))
        self.play(Write(q1))
        self.wait(1)

        # Create and animate dot with arrow and object
        dot = Dot().move_to(dot_positions[0])
        arrow = Arrow(world.get_top(), dot.get_center(), buff=0, color=YELLOW, stroke_width=1)
        obj = Text(objects[0], color=WHITE).scale(0.5).next_to(dot, DOWN)

        self.play(Create(dot), GrowArrow(arrow))
        self.play(Write(obj))
        self.wait(1.43)

        self.play(FadeOut(dot), FadeOut(arrow), FadeOut(obj))
        q22 = Text("(x1,x2) ?", color=WHITE).scale(0.5).next_to(world, UP)
        q2 = Text("x1 + x2 = 2", color=WHITE).scale(0.5).next_to(q22, UP)
        self.play(Transform(q1, q22), run_time=1)
        self.play(Write(q2))
        self.wait(1)

        objects = ["(1,1), (-1,3), (0,2), (1.34, 0.66)..."]
        dot_positions = [(-0.36, -0.65, 0)]

        # Create and animate dot with arrow and object
        dot = Circle().scale(0.2).move_to(dot_positions[0])
        dot.set_fill(GREEN, opacity=1)
        dot.set_stroke(width=0)
        arrow = Arrow(world.get_top(), dot.get_top(), buff=0, color=YELLOW, stroke_width=1)
        obj = Text(objects[0], color=WHITE).scale(0.5).next_to(dot, DOWN)

        self.play(Create(dot), GrowArrow(arrow))
        self.play(Write(obj))
        self.wait(1.43)
        self.clear()

    def define_paths(self, axes):
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

    def sceneThree(self):
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
        paths = self.define_paths(axes)

        # Animate paths
        for path in paths:
            self.play(Create(path), run_time=1.5)
            self.wait(0.5)
        self.wait(1.43)
        # Optionally, fade out paths after viewing
        self.play(*[FadeOut(path) for path in paths])

        self.wait(1.43)
        self.clear()

    def sceneFour(self):
        # Create and setup the 'world' rectangle
        world = Rectangle(width=5.0, height=4.0)
        world.set_fill(BLUE, opacity=0.2)
        world.set_stroke(BLUE, width=1)
        world_label = Text("Universe", color=WHITE).scale(0.5).next_to(world, LEFT)

        # First question related to path
        q1 = Text("Path from (0,0) to (6,7)?", color=WHITE).scale(0.5).next_to(world, UP)

        # Display the world and its label
        self.play(Create(world), Write(world_label))
        self.play(Write(q1))
        self.wait(1)

        # Introduce the outer polygon
        outer_vertices = [
            [-1, 1, 0], [-0.5, 0.5, 0], [0, 1, 0],
            [1, 0.5, 0], [0.5, -0.5, 0], [0, -1, 0], [-0.5, -0.5, 0]
        ]
        outer_polygon = VMobject()
        outer_polygon.set_points_smoothly([*outer_vertices])
        outer_polygon.set_fill(ORANGE, opacity=0.5)  # Set fill color and opacity
        outer_polygon.set_stroke(width=0)
        outer_polygon.move_to([-0.36, -0.65, 0])  # Adjust position within the world rectangle

        # Animate the creation of the outer polygon and an arrow
        arrow = Arrow(world.get_top(), outer_polygon.get_top(), buff=0, color=YELLOW, stroke_width=1)
        path_options = Text("(UP, LEFT, UP...) (LEFT, DOWN...) (...)", color=WHITE).scale(0.5).next_to(
            outer_polygon, DOWN)

        self.play(Create(outer_polygon), GrowArrow(arrow))
        self.play(Write(path_options))
        self.wait(1.43)

        # Clear the arrow and path options text
        self.remove(arrow, path_options)

        # New question about shortest paths
        q2 = Text("What are the shortest paths from (0,0) to (6,7)?", color=WHITE).scale(0.5).next_to(world, UP)
        self.play(Transform(q1, q2))
        self.wait(1)

        # Introduce the nested polygon with different vertices
        nested_vertices = [
            [-1, 0, 0], [-0.5, 1, 0], [0, 0.5, 0],
            [1, 0.5, 0], [0.5, -1, 0], [0, -0.5, 0], [-0.5, -1, 0]
        ]
        nested_polygon = VMobject()
        nested_polygon.set_points_smoothly([*nested_vertices])
        nested_polygon.set_fill(GREEN, opacity=0.75)  # Different fill color and higher opacity
        nested_polygon.set_stroke(width=0)
        nested_polygon.scale(0.3)
        nested_polygon.move_to(outer_polygon.get_center())  # Position inside the larger polygon
        arrow = Arrow(world.get_top(), nested_polygon.get_top(), buff=0, color=YELLOW, stroke_width=1)

        # Display the nested polygon
        self.play(FadeIn(nested_polygon), GrowArrow(arrow))
        self.wait(1.43)

        # Optionally, clean up the scene after the display
        self.play(FadeOut(world), FadeOut(world_label), FadeOut(q1), FadeOut(arrow), FadeOut(nested_polygon), FadeOut(outer_polygon))

    def sceneFive(self):

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
        max_sum_text = Text("Maximum sum per group: 100", font_size=36, color=WHITE).next_to(intro_text, DOWN, buff=0.5)

        # Array of numbers
        numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        array = VGroup(*[Text(str(num), font_size=36) for num in numbers])
        array.arrange(RIGHT, buff=0.2)
        array.next_to(max_sum_text, DOWN, buff=1)
        self.play(Write(max_sum_text))
        self.play(LaggedStart(*[FadeIn(mob) for mob in array], lag_ratio=0.04))

        # Initial grouping (example)
        initial_groups = [[10, 30, 60], [50, 40], [70], [20], [80], [90]]
        self.group_and_animate(numbers, initial_groups, array)
        self.wait(1.43)
        # Alternative grouping (example)
        alternative_groups = [[10, 90], [40, 60], [50], [30, 70], [80, 20]]
        self.group_and_animate(numbers, alternative_groups, array)

        self.play(FadeOut(array), FadeOut(max_sum_text))
        self.wait(1.43)

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

    def sceneSix(self, showTitle=True):
        # Create an intro text for the scene
        if showTitle:
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
            self.wait(1)

        # show backtracking
        self.show_backtracking_visual()
        self.clear()

    def show_backtracking_visual(self):
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

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        level_distance = 1  # Vertical spacing between levels
        nodes = VGroup(start_dot)
        new_nodes = VGroup()
        labels = []

        # Calculate positions for the next level
        for idx, (dx, dy) in enumerate(directions):
            end_coords = (start_coords[0] + dx, start_coords[1] + dy)
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
            self.generate_tree(new_dot, (end_coords[0], end_coords[1]), depth - 1, i, new_label, all_scene)



    def sceneSeven(self):
        world = Rectangle(width=5.0, height=4.0)
        world.set_fill(BLUE, opacity=0.2)
        world.set_stroke(BLUE, width=1)
        world_label = Text("Universe", color=WHITE).scale(0.5).next_to(world, LEFT)

        q1 = Text("1+1?", color=WHITE).scale(0.5).next_to(world, UP)

        objects = ["2"]
        dot_positions = [(1.55, 0.70, 0)]

        self.play(Create(world), Write(world_label))
        self.play(Write(q1))
        self.wait(1)

        # Create and animate dot with arrow and object
        dot = Dot().move_to(dot_positions[0])
        arrow = Arrow(world.get_top(), dot.get_center(), buff=0, color=YELLOW, stroke_width=1)
        obj = Text(objects[0], color=WHITE).scale(0.5).next_to(dot, DOWN)

        self.play(Create(dot), GrowArrow(arrow))
        self.play(Write(obj))
        self.wait(0.5)

        self.play(FadeOut(dot), FadeOut(arrow), FadeOut(obj))
        q22 = Text("(x1,x2) ?", color=WHITE).scale(0.5).next_to(world, UP)
        q2 = Text("x1 + x2 = 2", color=WHITE).scale(0.5).next_to(q22, UP)
        self.play(Transform(q1, q22), run_time=1)
        self.play(Write(q2))
        self.wait(1)

        objects = ["(1,1), (-1,3), (0,2), (1.34, 0.66)..."]
        dot_positions = [(-0.36, -0.65, 0)]

        # Create and animate dot with arrow and object
        dot = Circle().scale(0.2).move_to(dot_positions[0])
        dot.set_fill(GREEN, opacity=1)
        dot.set_stroke(width=0)
        arrow = Arrow(world.get_top(), dot.get_top(), buff=0, color=YELLOW, stroke_width=1)
        obj = Text(objects[0], color=WHITE).scale(0.5).next_to(dot, DOWN)

        self.play(Create(dot), GrowArrow(arrow))
        self.play(Write(obj))
        self.wait(1)
        self.play(FadeOut(obj), FadeOut(arrow), FadeOut(dot), FadeOut(q2))

        q3 = Text("Path from (0,0) to (6,7)?", color=WHITE).scale(0.5).next_to(world, UP)
        self.play(Transform(q1, q3))
        self.wait(1)

        # Introduce the outer polygon
        outer_vertices = [
            [-1, 1, 0], [-0.5, 0.5, 0], [0, 1, 0],
            [1, 0.5, 0], [0.5, -0.5, 0], [0, -1, 0], [-0.5, -0.5, 0]
        ]
        outer_polygon = VMobject()
        outer_polygon.set_points_smoothly([*outer_vertices])
        outer_polygon.set_fill(ORANGE, opacity=0.5)  # Set fill color and opacity
        outer_polygon.set_stroke(width=0)
        outer_polygon.move_to([-0.36, -0.65, 0])  # Adjust position within the world rectangle

        # Animate the creation of the outer polygon and an arrow
        arrow = Arrow(world.get_top(), outer_polygon.get_top(), buff=0, color=YELLOW, stroke_width=1)
        path_options = Text("(UP, LEFT, UP...) (LEFT, DOWN...) (...)", color=WHITE).scale(0.5).next_to(
            outer_polygon, DOWN)

        self.play(Create(outer_polygon), GrowArrow(arrow))
        self.play(Write(path_options))
        self.wait(2)

        # Clear the arrow and path options text
        self.remove(arrow, path_options)

        # New question about shortest paths
        q2 = Text("What are the shortest paths from (0,0) to (6,7)?", color=WHITE).scale(0.5).next_to(world, UP)
        self.play(Transform(q1, q2))
        self.wait(1)

        # Introduce the nested polygon with different vertices
        nested_vertices = [
            [-1, 0, 0], [-0.5, 1, 0], [0, 0.5, 0],
            [1, 0.5, 0], [0.5, -1, 0], [0, -0.5, 0], [-0.5, -1, 0]
        ]
        nested_polygon = VMobject()
        nested_polygon.set_points_smoothly([*nested_vertices])
        nested_polygon.set_fill(GREEN, opacity=0.75)  # Different fill color and higher opacity
        nested_polygon.set_stroke(width=0)
        nested_polygon.scale(0.3)
        nested_polygon.move_to(outer_polygon.get_center())  # Position inside the larger polygon
        arrow = Arrow(world.get_top(), nested_polygon.get_top(), buff=0, color=YELLOW, stroke_width=1)

        # Display the nested polygon
        self.play(FadeIn(nested_polygon), GrowArrow(arrow))
        self.wait(2)

        # Optionally, clean up the scene after the display
        self.play(FadeOut(world), FadeOut(world_label), FadeOut(q1), FadeOut(arrow), FadeOut(nested_polygon), FadeOut(outer_polygon))
        self.wait(1.43)

    def sceneEight(self):

        start_title = Text("How to run?", font_size=36).to_edge(UP)

        # Title for the grid scenario
        grid_title = Text("Grid Pathfinding", font_size=36).to_edge(UP)
        grid_title.shift(LEFT * 3)
        grid_title.shift(DOWN * 0.5)

        # Title for the grouping problem, positioned relative to the grid
        grouping_title = Text("Groups Problem", font_size=36).to_edge(UP)
        grouping_title.shift(RIGHT * 3)  # Position to the right of the grid
        grouping_title.shift(DOWN * 0.5)
        self.play(Create(start_title),Create(grid_title),Create(grouping_title), run_time=0.5)

        grid = VGroup()
        for i in range(5):
            for j in range(5):
                cell = Dot()
                cell.move_to(np.array([i - 5 / 2, j - 5 / 2, 0]))
                grid.add(cell)
        grid.to_edge(LEFT, buff=1)

        numbers = [10, 20, 30, 40, 50]
        num_objects = VGroup(*[Text(str(num), font_size=30) for num in numbers])
        num_objects.arrange(RIGHT, buff=0.5)
        num_objects.next_to(grouping_title)
        num_objects.shift(LEFT * 4)
        num_objects.shift(DOWN * 3)

        # Introduce all numbers at once
        self.play(FadeIn(num_objects), Create(grid), run_time=1)
        path = self.animate_grid_path(grid, start=(0, 0), end=(4, 4))
        self.animate_grouping_sequence(num_objects)

        self.wait(0.5)  # Hold the scene to view
        self.play(FadeOut(start_title), FadeOut(path), FadeOut(grid), FadeOut(num_objects), FadeOut(grid_title), FadeOut(grouping_title))

    def animate_grid_path(self, grid, start, end):
        path = VMobject(color=RED, stroke_width=3)
        points = [grid[start[0] * 5 + start[1]].get_center()]  # Start from the initial position

        # Calculate horizontal and vertical steps
        x_steps = end[0] - start[0]  # Difference in x
        y_steps = end[1] - start[1]  # Difference in y

        # Generate path points horizontally first, then vertically (or vice versa)
        for i in range(abs(x_steps)):
            next_point = grid[(start[0] + (i + 1) * (1 if x_steps > 0 else -1)) * 5 + start[1]].get_center()
            points.append(next_point)

        for j in range(abs(y_steps)):
            next_point = grid[(end[0]) * 5 + (start[1] + (j + 1) * (1 if y_steps > 0 else -1))].get_center()
            points.append(next_point)

        # Set points to the VMobject path
        path.set_points_as_corners(points)
        self.play(Create(path), run_time=2)
        return path

    def animate_grouping_sequence(self, num_objects):

        for num in num_objects:
            self.play(num.animate.scale(1.5), run_time=0.5)
            self.play(num.animate.scale(2 / 3), run_time=0.5)

    def sceneNine(self):
        # Title for the scene
        title = Text("Backtracking Solution Structure", font_size=36)
        self.play(Write(title))
        self.wait(1)

        # Move title to top and create space for further explanations
        self.play(title.animate.to_edge(UP))

        # Solution Structure Heading
        structure_heading = Text("Solution Structure:", font_size=30)
        structure_heading.next_to(title, DOWN, buff=1)
        self.play(Write(structure_heading))
        self.wait(1)

        # Wrapper Function Description
        wrapper_description = Text(
            "1. Wrapper Function: Sets up initial state and starts recursive exploration.",
            font_size=24,
            t2c={"Wrapper Function": YELLOW}
        )
        wrapper_description.next_to(structure_heading, DOWN, buff=0.5)
        self.play(Write(wrapper_description))
        self.wait(2)

        # Recursive Function Description
        recursive_description = Text(
            "2. Recursive Function:\n"
            "   - Base Case (Stopping Condition): Successful Stop or Unsuccessful Stop.\n"
            "   - Recursive Call: Explores further if current state is promising.",
            font_size=24,
            t2c={"Recursive Function": YELLOW, "Base Case": BLUE, "Recursive Call": GREEN}
        )
        recursive_description.next_to(wrapper_description, DOWN, buff=0.5)
        self.play(Write(recursive_description))
        self.wait(2)

        # Logic Function Description
        logic_description = Text(
            "3. Logic Function: Decides whether this step is valid.",
            font_size=24,
            t2c={"Logic Function": YELLOW}
        )
        logic_description.next_to(wrapper_description, DOWN, buff=2)
        logic_description.shift(LEFT * 1.4)
        self.play(Write(logic_description))
        self.wait(2)

        # Concluding the explanation
        conclusion = Text(
            "This methodical approach allows systematic exploration of all potential solutions.",
            font_size=24,
            color=TEAL
        )
        conclusion.next_to(recursive_description, DOWN, buff=2)
        self.play(Write(conclusion))
        self.wait(3)

        # Fade out all to end scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def sceneTen(self):
        # Introduction Text
        intro_text = Text("Solving the Grid Problem", font_size=24)
        intro_text.to_edge(UP)
        self.play(Write(intro_text))
        self.wait(1)
        info_text = Text("Find min path", font_size=24)
        info_text.next_to(intro_text, DOWN)
        self.play(Write(info_text))

        # Display Recursive Function Explanation - get_min_path
        get_min_path = self.display_code_get_min_path()
        get_min_path.next_to(intro_text, DOWN, buff=0.7)
        self.play(Write(get_min_path))
        self.wait(2)

        info2_text = Text("Find number of min paths", font_size=24)
        info2_text.next_to(intro_text, DOWN)
        self.play(Transform(info_text, info2_text))
        # Prepare the second text - count_min_paths
        count_min_paths = self.display_code_count_min_paths()
        count_min_paths.move_to(get_min_path.get_center())  # Ensure identical positioning

        # Animate the transformation without changing their place
        self.play(Transform(get_min_path, count_min_paths))
        self.wait(3)

        info3_text = Text("Find number of min paths with legal", font_size=24)
        info3_text.next_to(intro_text, DOWN)
        self.play(Transform(info_text, info3_text))
        # Prepare the second text - count_min_paths
        count_min_paths = self.display_code_count_min_paths_with_legal()
        count_min_paths.move_to(get_min_path.get_center())  # Ensure identical positioning

        # Animate the transformation without changing their place
        self.play(Transform(get_min_path, count_min_paths))
        self.wait(3)
        self.play(FadeOut(intro_text), FadeOut(info_text), FadeOut(get_min_path))

    def display_code_get_min_path(self):
        code = Text(
            "Recursion function:\n"
            "not real code!\n"
            "    if i, j == m, n: \n "
            "       return path  # Good stop \n"
            "    if i or j out of bounds or grid[i][j] == 2: \n"
            "       return N*N+1  # Bad stop\n"
            " directions = [(0,1),(1,0),(-1,0),(0,-1)]\n"
            " min_path = N*N+1\n"
            " grid[i][j] = 2 # So we dont return to the same place\n"
            " for x,y in directions:\n"
            "   new_i = i + x\n"
            "   new_j = j + y\n"
            "   min_path = min(min_path, recursion(new_i, new_j, path+1))\n"
            " grid[i][j] = 0 # So we can return to here\n"
            " return min_path  # end of function\n",
            t2c={"N*N+1": GREEN, "grid[i][j] = 2":BLUE,"grid[i][j] = 0":BLUE},
            line_spacing=1,
            font_size=20,
        ).to_edge(DOWN)
        return code

    def display_code_count_min_paths(self):
        code = Text(
            "Recursion function:\n"
            "not real code!\n"
            "    if i, j == m, n: \n "
            "       return 1  # Good stop \n"
            "    if i or j out of bounds or grid[i][j] == 2 or path > m + n: \n"
            "       return 0  # Bad stop\n"
            " directions = [(0,1),(1,0),(-1,0),(0,-1)]\n"
            " paths = 0\n"
            " grid[i][j] = 2 # So we dont return to the same place\n"
            " for x,y in directions:\n"
            "   new_i = i + x\n"
            "   new_j = j + y\n"
            "   paths += recursion(new_i, new_j, path+1)\n"
            " grid[i][j] = 0 # So we can return to here\n"
            " return paths  # end of function\n",
            t2c={"or path > m + n:": YELLOW, "return 1": YELLOW, "return 0": YELLOW, "grid[i][j] = 2":BLUE,"grid[i][j] = 0":BLUE},
            line_spacing=1,
            font_size=20,
        ).to_edge(DOWN)
        return code

    def display_code_count_min_paths_with_legal(self):
        code = Text(
            "Recursion function:\n"
            "not real code!\n"
            "    if i, j == m, n: \n "
            "       return 1  # Good stop \n"
            "    if not_legal_move: \n"
            "       return 0  # Bad stop\n"
            " directions = [(0,1),(1,0),(-1,0),(0,-1)]\n"
            " paths = 0\n"
            " grid[i][j] = 2 # So we dont return to the same place\n"
            " for x,y in directions:\n"
            "   new_i = i + x\n"
            "   new_j = j + y\n"
            "   paths += recursion(new_i, new_j, path+1)\n"
            " grid[i][j] = 0 # So we can return to here\n"
            " return paths  # end of function\n",
            t2c={"not_legal_move": YELLOW},
            line_spacing=1,
            font_size=20,
        ).to_edge(DOWN)
        return code

    def sceneEleven(self):
        intro_text = Text("Solving the Grid Problem", font_size=24)
        intro_text.to_edge(UP)
        self.play(Write(intro_text))
        self.wait(1)
        info_text = Text("Wrapper Function", font_size=24)
        info_text.next_to(intro_text, DOWN)
        self.play(Write(info_text))

        # Display Recursive Function Explanation - get_min_path
        get_wrapper_code = Text(
            "not real code!\n"
            " need grid, start, end, steps\n\n"
            " return rec(grid, 0,0,n,m,0)\n",
            line_spacing=1,
            font_size=20,
        )
        get_wrapper_code.next_to(intro_text, DOWN, buff=1.5)
        self.play(Write(get_wrapper_code))
        self.wait(3)
        self.play(FadeOut(intro_text), FadeOut(info_text), FadeOut(get_wrapper_code))

    def sceneTwelve(self):
        # Introduction Text
        intro_text = Text("Solving the Groups Problem", font_size=24)
        intro_text.to_edge(UP)
        self.play(Write(intro_text))
        self.wait(1)
        info_text = Text("Find min groups", font_size=24)
        info_text.next_to(intro_text, DOWN)
        self.play(Write(info_text))

        # Display Recursive Function Explanation - get_min_path
        code_rec_group = self.display_code_rec_groups()
        code_rec_group.next_to(intro_text, DOWN, buff=0.5)
        self.play(Write(code_rec_group))
        self.wait(2)

        # Prepare the second text - count_min_paths
        legal_groups = Text(
            "Legal function:\n"
            "not real code!\n\n"
            " for group in groups:\n"
            "   if group > k:\n"
            "       return true # not legal\n"
            " return false  # all groups are legal\n",
            line_spacing=1,
            font_size=20,
        )
        legal_groups.move_to(code_rec_group.get_center())  # Ensure identical positioning

        self.play(Transform(code_rec_group, legal_groups))
        self.wait(3)

        wrapper_groups = Text(
            "not real code!\n"
            " need arr, groups, start, end, k - max in group\n\n"
            " groups = [0] * n \n"
            " return rec(arr,groups,0,n,k)\n",
            line_spacing=1,
            font_size=20,
        )
        wrapper_groups.move_to(code_rec_group.get_center())  # Ensure identical positioning

        # Animate the transformation without changing their place
        self.play(Transform(code_rec_group, wrapper_groups))
        self.wait(3)
        self.play(FadeOut(intro_text), FadeOut(info_text), FadeOut(code_rec_group))

    def display_code_rec_groups(self):
        code = Text(
            "Recursion function:\n"
            "not real code!\n"
            " if groups_is_not_legal:\n"
            "    return n + 1 \n"
            " if index == n: \n"
            "    return num_of_groups \n"
            " min_groups = n + 1 \n"
            " for j in range(n): \n"
            "   groups[j] += arr[index] \n"
            "   min_groups = min(min_groups, rec(arr, groups, index + 1, n, k)) \n"
            "   groups[j] -= arr[index]  \n"
            " return min_groups \n",
            line_spacing=1,
            font_size=20,
        ).to_edge(DOWN)
        return code
    def sceneTherteen(self):

        # show backtracking
        intro_text = Text("Groups Backtracking Exploration", font_size=36, color=WHITE)
        intro_text.to_edge(UP)
        self.play(Write(intro_text))

        numbers = [10, 20, 30, 40, 50]
        num_objects = VGroup(*[Text(str(num), font_size=30) for num in numbers])
        num_objects.arrange(RIGHT, buff=0.3)
        num_objects.next_to(intro_text)
        num_objects.shift(DOWN)

        # Introduce all numbers at once
        self.play(FadeIn(num_objects), run_time=0.4)

        # Define the starting position and create the main node
        start_pos = np.array([0, 2, 0])  # Start at the center top
        start_dot = Dot(start_pos, color=RED)
        start_label = text = MarkupText(
            f'0, <span fgcolor="{WHITE}">0</span>, <span fgcolor="{PINK}">0</span>, <span fgcolor="{GREEN}">0</span>', color=YELLOW, font_size=30).next_to(start_dot, UP, buff=SMALL_BUFF)
        self.play(Write(start_label))
        all_scene = VGroup()
        all_scene.add(intro_text)
        all_scene.add(start_label)
        # Generate the tree vertically downwards

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dict_labels_depth_2 = {
            (0, 1): Text("10", t2c={"10": YELLOW}, font_size=30),
            (1, 0): Text("10", t2c={"10": WHITE}, font_size=30),
            (0, -1): Text("10", t2c={"10": PINK}, font_size=30),
            (-1, 0): Text("10", t2c={"10": GREEN}, font_size=30),
        }
        dict_labels = [
            {
                (0, 2): Text("30 ", t2c={"30": YELLOW}, font_size=23),
                (1, 1): Text("20,10 ", t2c={"20": YELLOW, "10": WHITE}, font_size=23),
                (0, 0): Text("20,10 ", t2c={"20": YELLOW, "10": PINK}, font_size=23),
                (-1, 1): Text("20,10 ", t2c={"20": YELLOW, "10": GREEN}, font_size=23),
            }, {
                (1, 1): Text("10,20 ", t2c={"10": YELLOW, "20": WHITE}, font_size=23),
                (2, 0): Text("30 ", t2c={"30": WHITE}, font_size=23),
                (1, -1): Text("10,20 ", t2c={"10": PINK, "20": WHITE}, font_size=23),
                (0, 0): Text("10,20 ", t2c={"10": GREEN, "20": WHITE}, font_size=23),
            }, {
                (0, 0): Text("10,20 ", t2c={"10": YELLOW, "20": PINK}, font_size=23),
                (1, -1): Text("10,20 ", t2c={"10": WHITE, "20": PINK}, font_size=23),
                (0, -2): Text("30 ", t2c={"30": PINK}, font_size=23),
                (-1, -1): Text("10,20 ", t2c={"10": GREEN, "20": PINK}, font_size=23),
            }, {
                (-1, 1): Text("10,20 ", t2c={"10": YELLOW, "20": GREEN}, font_size=23),
                (0, 0): Text("10,20 ", t2c={"10": WHITE, "20": GREEN}, font_size=23),
                (-1, -1): Text("10,20 ", t2c={"10": PINK, "20": GREEN}, font_size=23),
                (-2, 0): Text("30 ", t2c={"30": GREEN}, font_size=23),
            }]
        pos = {
            # Layer 1: Root
            1: [0, 2, 0],  # Root node

            # Layer 2: First set of children
            2: [-5.095, 0.5, 0],  # Four children, spaced wider
            3: [-1.695, 0.5, 0],
            4: [1.705, 0.5, 0],
            5: [5.105, 0.5, 0],

            # Layer 3: Children of Node 2
            6: [-6.37, -1.5, 0],
            7: [-5.52, -1.5, 0],
            8: [-4.67, -1.5, 0],
            9: [-3.82, -1.5, 0],

            # Children of Node 3
            10: [-2.97, -1.0, 0],
            11: [-2.12, -1.0, 0],
            12: [-1.27, -1.0, 0],
            13: [-0.42, -1.0, 0],

            # Children of Node 4
            14: [0.43, -1.5, 0],
            15: [1.28, -1.5, 0],
            16: [2.13, -1.5, 0],
            17: [2.98, -1.5, 0],

            # Children of Node 5
            18: [3.83, -1.0, 0],
            19: [4.68, -1.0, 0],
            20: [5.53, -1.0, 0],
            21: [6.38, -1.0, 0],
        }
        labels = []
        color = BLUE
        for idx, (dx, dy) in enumerate(directions):
            end_coords = (dx, dy)
            new_label = dict_labels_depth_2[end_coords]
            new_label.move_to(pos[idx+2])
            new_label.shift(UP * 0.2)
            self.play(num_objects[0].animate.scale(1.5), run_time=0.3)
            self.play(Write(new_label), run_time=0.3)
            arrow = Arrow(pos[1], new_label.get_top(), buff=0.1, color=color)
            self.play(GrowArrow(arrow), run_time=0.5)
            self.play(num_objects[0].animate.scale(2 / 3), run_time=0.3)
            labels.append(new_label)
            all_scene.add(new_label)
            all_scene.add(arrow)
            for idx2, (dx2, dy2) in enumerate(directions):
                end_coords2 = (dx + dx2, dy + dy2)
                new_label2 = dict_labels[idx2][end_coords2]
                new_label2.move_to(pos[(idx+1)*4 + idx2 + 2])
                self.play(num_objects[1].animate.scale(1.5), run_time=0.3)
                self.play(Write(new_label2), run_time=0.3)
                # Connect the new dot to the previous level
                arrow = Arrow(new_label.get_bottom(), new_label2.get_top(), buff=0.1, color=color)
                self.play(GrowArrow(arrow), run_time=0.5)
                self.play(num_objects[1].animate.scale(2 / 3), run_time=0.3)
                labels.append(new_label2)
                all_scene.add(new_label2)
                all_scene.add(arrow)

        self.wait(2)
        self.play(FadeOut(all_scene), FadeOut(num_objects))


class One(Scene):
    def construct(self):
        # Introduction Text
        intro_text = Text("Solving the Groups Problem", font_size=24)
        intro_text.to_edge(UP)
        self.play(Write(intro_text))
        self.wait(1)
        info_text = Text("Find min groups", font_size=24)
        info_text.next_to(intro_text, DOWN)
        self.play(Write(info_text))

        # Display Recursive Function Explanation - get_min_path
        code_rec_group = self.display_code_rec_groups()
        code_rec_group.next_to(intro_text, DOWN, buff=0.5)
        self.play(Write(code_rec_group))
        self.wait(2)

        # Prepare the second text - count_min_paths
        legal_groups = Text(
            "Legal function:\n"
            "not real code!\n\n"
            " for group in groups:\n"
            "   if group > k:\n"
            "       return true # not legal\n"
            " return false  # all groups are legal\n",
            line_spacing=1,
            font_size=20,
        )
        legal_groups.move_to(code_rec_group.get_center())  # Ensure identical positioning

        self.play(Transform(code_rec_group, legal_groups))
        self.wait(3)

        wrapper_groups = Text(
            "not real code!\n"
            " need arr, groups, start, end, k - max in group\n\n"
            " groups = [0] * n \n"
            " return rec(arr,groups,0,n,k)\n",
            line_spacing=1,
            font_size=20,
        )
        wrapper_groups.move_to(code_rec_group.get_center())  # Ensure identical positioning

        # Animate the transformation without changing their place
        self.play(Transform(code_rec_group, wrapper_groups))
        self.wait(3)
        self.play(FadeOut(intro_text), FadeOut(info_text), FadeOut(code_rec_group))

    def display_code_rec_groups(self):
        code = Text(
            "Recursion function:\n"
            "not real code!\n"
            " if groups_is_not_legal:\n"
            "    return n + 1 \n"
            " if index == n: \n"
            "    return num_of_groups \n"
            " min_groups = n + 1 \n"
            " for j in range(n): \n"
            "   groups[j] += arr[index] \n"
            "   min_groups = min(min_groups, rec(arr, groups, index + 1, n, k)) \n"
            "   groups[j] -= arr[index]  \n"
            " return min_groups \n",
            line_spacing=1,
            font_size=20,
        ).to_edge(DOWN)
        return code
