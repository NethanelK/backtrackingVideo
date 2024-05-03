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

def how_to_run(self):

    start_title = Text("How to run?", font_size=36).to_edge(UP)
    # Title for the grid scenario
    grid_title = Text("Grid Pathfinding", font_size=36).to_edge(UP)
    grid_title.shift(LEFT * 3)
    grid_title.shift(DOWN * 0.7)

    # Title for the grouping problem, positioned relative to the grid
    grouping_title = Text("Groups Problem", font_size=36).to_edge(UP)
    grouping_title.shift(RIGHT * 3)  # Position to the right of the grid
    grouping_title.shift(DOWN * 0.7)
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
    path = animate_grid_path(self, grid, start=(0, 0), end=(4, 4))

    for num in num_objects:
        self.play(num.animate.scale(1.5), run_time=0.5)
        self.play(num.animate.scale(2 / 3), run_time=0.5)

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

def backtracking_structure(self):
    # Title for the scene
    title = Text("Backtracking Solution Structure", font_size=36)
    self.play(Write(title))
    self.wait(1)

    # Move title to top and create space for further explanations
    self.play(title.animate.to_edge(UP,buff=1.5))

    # Solution Structure Heading
    structure_heading = Text("Solution Structure:", font_size=30)
    structure_heading.next_to(title, DOWN, buff=0.5)
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

def grid_problem_code_rec(self):
    # Introduction Text
    intro_text = Text("Solving the Grid Problem", font_size=24)
    intro_text.to_edge(UP)
    self.play(Write(intro_text))
    self.wait(1)
    info_text = Text("Find min path", font_size=24)
    info_text.next_to(intro_text, DOWN)
    self.play(Write(info_text))

    # Display Recursive Function Explanation - get_min_path
    get_min_path = display_code_get_min_path()
    get_min_path.next_to(intro_text, DOWN, buff=0.7)
    self.play(Write(get_min_path))
    self.wait(2)

    info2_text = Text("Find number of min paths", font_size=24)
    info2_text.next_to(intro_text, DOWN)
    self.play(Transform(info_text, info2_text))
    # Prepare the second text - count_min_paths
    count_min_paths = display_code_count_min_paths()
    count_min_paths.next_to(intro_text, DOWN, buff=0.7)  # Ensure identical positioning

    # Animate the transformation without changing their place
    self.play(FadeOut(get_min_path), Write(count_min_paths))
    self.wait(3)

    info3_text = Text("Find number of min paths with legal", font_size=24)
    info3_text.next_to(intro_text, DOWN)
    self.play(Transform(info_text, info3_text))
    # Prepare the second text - count_min_paths
    count_min_paths_with_legal = display_code_count_min_paths_with_legal()
    count_min_paths_with_legal.next_to(intro_text, DOWN, buff=0.7)  # Ensure identical positioning

    # Animate the transformation without changing their place
    self.play(FadeOut(count_min_paths), Write(count_min_paths_with_legal))
    self.wait(3)
    self.play(FadeOut(intro_text), FadeOut(info_text), FadeOut(count_min_paths_with_legal))

def display_code_get_min_path():

    code_text = '''
                if i, j == m, n: 
                    return path  // Good stop 
                if i or j  out  of  bounds  or grid[ i ][ j ] == 2 or path > m + n: 
                    return N*N+1  // Bad stop
                directions = [(0,1),(1,0),(-1,0),(0,-1)]
                min_path = N*N+1
                grid[ i ][ j ] = 2 // So we dont return to the same place
                for x,y in directions:
                    new_i = i + x
                    new_j = j + y
                    min_path = min(min_path, recursion(new_i, new_j, path+1))
                grid[ i ][ j ] = 0 // So we can return to here
                return min_path  // end of function'''

    code = Code(code=code_text, line_spacing=1, language='C++', font_size=18)
    return code

def display_code_count_min_paths():

    code_text = '''
            if i, j == m, n: 
                return 1  // Good stop 
            if i or j  out  of  bounds  or grid[ i ][ j ] == 2 or path > m + n: 
                return 0  // Bad stop
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            paths = 0
            grid[ i ][ j ] = 2 // So we dont return to the same place
            for x,y in directions:
                new_i = i + x
                new_j = j + y
                paths += recursion(new_i, new_j, path+1)
            grid[ i ][ j ] = 0 // So we can return to here
            return paths  // end of function'''

    code = Code(code=code_text, line_spacing=1, language='C++', font_size=18)
    return code

def display_code_count_min_paths_with_legal():

    code_text = '''
        if i, j == m, n: 
            return 1  // Good stop 
        if not_legal_move: 
            return 0  // Bad stop
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        paths = 0
        grid[ i ][ j ] = 2 // So we dont return to the same place
        for x,y in directions:
            new_i = i + x
            new_j = j + y
            paths += recursion(new_i, new_j, path+1)
        grid[ i ][ j ] = 0 // So we can return to here
        return paths  // end of function'''

    code = Code(code=code_text, line_spacing=1, language='C++', font_size=18)
    return code

def grid_problem_code_wrapper(self):
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

def groups_problem_code(self):
    # Introduction Text
    intro_text = Text("Solving the Groups Problem", font_size=24)
    intro_text.to_edge(UP)
    info_text = Text("Find min groups", font_size=24)
    info_text.next_to(intro_text, DOWN)
    self.play(Write(intro_text), Write(info_text))

    # Display Recursive Function Explanation - get_min_path
    code_rec_group = display_code_rec_groups()
    code_rec_group.next_to(intro_text, DOWN, buff=1)
    self.play(Write(code_rec_group))
    self.wait(1.43)

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

    self.play(FadeOut(code_rec_group), FadeIn(legal_groups))
    self.wait(1.43)

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
    self.play(FadeOut(legal_groups), FadeIn(wrapper_groups))
    self.wait(1.43)
    self.play(FadeOut(intro_text), FadeOut(info_text), FadeOut(wrapper_groups))

def display_code_rec_groups():
    code_text = '''
         if groups_is_not_legal:
            return n + 1 
         if index == n: 
            return num_of_groups 
         min_groups = n + 1 
         for j in range(n): 
           groups[ j ] += arr[ index ] 
           min_groups = min(min_groups, rec(arr, groups, index + 1, n, k)) 
           groups[ j ] -= arr[ index ]  
         return min_groups 
        '''

    code = Code(code=code_text, line_spacing=1, language='C++', font_size=18)
    return code


def animate_groups(self):

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

