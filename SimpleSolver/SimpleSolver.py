import pycuber as pc
from SimpleSolver.util import Solved

class SimpleSolver:

    def Solve(self, cube):
        assert type(cube) == pc.Cube, "Cannot solve a non cube"
        Cross(cube)

    def Cross(self, cube):
        assert type(cube) == pc.Cube, "Cannot solve a non cube"
        edges = list(cube.select_type("edge"))
        pc.Edge
