import pycuber as pc
import os

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "/cubeY.csv", "r") as Yraw:
        with open(dir_path + "/cubeXRNN.csv", "w") as Xrnn:
            with open(dir_path + "/cubeYRNN.csv", "w") as Yrnn:
                for yline in Yraw:
                    yline = yline.strip("\n")
                    c = pc.Cube()
                    formula = pc.Formula(yline.strip("\n"))
                    formula.reverse()
                    c(formula)
                    for ch in yline.split(" "):
                        Yrnn.write(ch + "\n")
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
                        Xrnn.write(cKStr + "\n")
                        c(ch)
main()