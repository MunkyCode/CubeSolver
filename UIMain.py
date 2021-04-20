import pycuber as pc
from SimpleSolver.HumanSolver import HumanSolver as Solver
from SimpleSolver.util import Solved

def UIMainTesting():
    c = pc.Cube()
    alg = pc.Formula()
    random_alg = alg.random()
    c(random_alg)
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

    print(c.select_type("edge"))
    print(c.get_face("U"))
    
def UIMain():
    c = pc.Cube()

    #Shuffle the Cube
    c(pc.Formula().random())
    #c("U D L R")

    print(c)

    S = Solver()

    S.Solve(c)

    print(c)
    


    

#UIMainTesting()
UIMain()
