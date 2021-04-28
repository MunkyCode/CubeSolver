import pycuber as pc
from SimpleSolver.util import Solved

def SolvedTest():
    c = pc.Cube()
    c2 = pc.Cube()
    c3 = pc.Cube()
    c(pc.Formula().random())
    c2("U")
    print(c)
    print(Solved(c))
    print(c2)
    print(Solved(c2))
    print(c3)
    print(Solved(c3))
    

SolvedTest()