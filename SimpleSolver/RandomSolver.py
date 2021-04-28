import pycuber as pc
from SimpleSolver.util import Solved
import random

class RandomSolver:

    def Solve(self, cube):
        assert type(cube) == pc.Cube, "Cannot solve a non cube"
        moves = ["R","R'","R2","L","L'","L2","U","U'","U2","D","D'","D2","F","F'","F2","B","B'","B2"]
        itr = 0
        while itr < 500 and not Solved(cube):
            cube(random.choice(moves))
            itr += 1