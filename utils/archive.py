from manim import *

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
