# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from manim import *
from utils.utils import *
from Backtracking import *

class Backtracking(Scene):

    def construct(self):
        intro(self)
        grid_preview(self)
        grid_visualising(self)
        groups_preview(self)
        groups_visualising(self)
        backtracking_intro_guide(self)
        how_to_run(self)
        generate_grid_full_tree(self)
        generate_grid_tree(self)
        backtracking_structure(self)
        grid_problem_code_rec(self)
        grid_problem_code_wrapper(self)
        groups_problem_code(self)
        animate_groups_tree(self)
        backtracking_structure(self)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Backtracking().construct()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
