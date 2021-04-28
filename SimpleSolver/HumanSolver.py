import pycuber as pc
from SimpleSolver.util import Solved

class HumanSolver:
    
    def Solve(self, cube):
        assert type(cube) == pc.Cube, "Cannot solve non Cube"
        print(cube)
        moves = ["R","R'","R2","L","L'","L2","U","U'","U2","D","D'","D2","F","F'","F2","B","B'","B2"]
        inp = input("Enter Move or done: ")
        inp = inp.strip()
        inp = inp.upper()
        while inp != "DONE" and not Solved(cube):
            if(inp not in moves):
                print("Not Valid Move")
                print(cube)
                inp = input("Enter Move or done: ")
                inp = inp.strip()
                inp = inp.upper()
            else:
                cube(inp)
                print(cube)
                if(not Solved(cube)):
                    inp = input("Enter Move or done: ")
                    inp = inp.strip()
                    inp = inp.upper()
        if(Solved(cube)):
            print("Solved!!")