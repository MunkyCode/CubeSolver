import pycuber as pc
from pycuber.solver import CFOPSolver
from SimpleSolver.HumanSolver import HumanSolver as Solver
from SimpleSolver.util import Solved
import kociemba
import time
import os
import re

def UIMainTesting():
    c = pc.Cube()
    alg = pc.Formula()
    random_alg = alg.random()
    #c(random_alg)
    cStr = c.__str__()
    cStr = (cStr.replace('[', '')).replace(']','')
    cStr = cStr.split()
    cubeDict = {"R":"","O":"","G":"","B":"","Y":"","W":""}
    row1 = list(cStr[3])
    row2 = list(cStr[4])
    row3 = list(cStr[5])
    cubeDict["Y"] = cStr[0] + cStr[1] + cStr[2]
    cubeDict["W"] = cStr[6] + cStr[7] + cStr[8]
    cubeDict["R"] = row1[0] + row1[1] + row1[2] + row2[0] + row2[1] + row2[2] + row3[0] + row3[1] + row3[2]
    cubeDict["G"] = row1[3] + row1[4] + row1[5] + row2[3] + row2[4] + row2[5] + row3[3] + row3[4] + row3[5]
    cubeDict["O"] = row1[6] + row1[7] + row1[8] + row2[6] + row2[7] + row2[8] + row3[6] + row3[7] + row3[8]
    cubeDict["B"] = row1[9] + row1[10] + row1[11] + row2[9] + row2[10] + row2[11] + row3[9] + row3[10] + row3[11]
    print(cubeDict)
    #print(c.select_type("edge"))
    #print(list(c.select_type("edge")))
    temp = list(list(c.select_type("edge"))[0].children)
    temp2 = list(list(c.select_type("edge"))[0].facings)
    #print(list(list(c.select_type("edge"))[0]))
    #print(temp[0], temp2[0], temp[1], temp2[1])

    
    #Get a set of the edges for the side down ("D"). Take an edge and get the square on side edge["side"] and convert to string square.__str__()
    setEdge = (c.has_colour(c["D"].colour) & c.select_type("edge"))
    print(setEdge)
    for i in setEdge:
        child = list(i.facings)
        print(i[child[0]].__str__())

    
   
    
    
def UIMain():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    timeS = time.time()
    for y in range(100):
        with open(dir_path + "/cubeX.csv", "a+") as X:
            with open(dir_path + "/cubeY.csv", "a+") as Y:
                for x in range(100):
                    c = pc.Cube()
                    c(pc.Formula().random())
                    cStr = c.__str__()
                    cStr = (cStr.replace('[', '')).replace(']','')
                    cStr = cStr.replace('r','L')
                    cStr = cStr.replace('o','R')
                    cStr = cStr.replace('y','U')
                    cStr = cStr.replace('w','D')
                    cStr = cStr.replace('g','F')
                    cStr = cStr.replace('b','B')
                    cStr = cStr.split()
                    cubeDict = {"L":"","R":"","F":"","B":"","U":"","D":""}
                    row1 = list(cStr[3])
                    row2 = list(cStr[4])
                    row3 = list(cStr[5])
                    cubeDict["U"] = cStr[0] + cStr[1] + cStr[2]
                    cubeDict["D"] = cStr[6] + cStr[7] + cStr[8]
                    cubeDict["L"] = row1[0] + row1[1] + row1[2] + row2[0] + row2[1] + row2[2] + row3[0] + row3[1] + row3[2]
                    cubeDict["F"] = row1[3] + row1[4] + row1[5] + row2[3] + row2[4] + row2[5] + row3[3] + row3[4] + row3[5]
                    cubeDict["R"] = row1[6] + row1[7] + row1[8] + row2[6] + row2[7] + row2[8] + row3[6] + row3[7] + row3[8]
                    cubeDict["B"] = row1[9] + row1[10] + row1[11] + row2[9] + row2[10] + row2[11] + row3[9] + row3[10] + row3[11]
                    cKStr = cubeDict["U"] + cubeDict["R"] + cubeDict["F"] + cubeDict["D"] + cubeDict["L"] + cubeDict["B"]
                    sol = kociemba.solve(cKStr)
                    X.write(cKStr + "\n")
                    Y.write(sol + "\n")
                    print(x + y * 100)

        
    print(time.time() - timeS)
    

def testingSolver():
    c = pc.Cube()
    c(pc.Formula().random())
    solver = CFOPSolver(c)

    solution = solver.solve()

    print(kociemba.solve('DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD'))
    

#UIMainTesting()
UIMain()
#testingSolver()