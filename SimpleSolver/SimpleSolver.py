import pycuber as pc
from SimpleSolver.util import Solved

class SimpleSolver:
    ColorDict = {"[r]":"red","[b]":"blue","[o]":"orange", "[g]":"green","[w]":"white","[y]":"yellow"}

    def Solve(self, cube):
        assert type(cube) == pc.Cube, "Cannot solve a non cube"
        self.Cross(cube)

    def Cross(self, cube):
        assert type(cube) == pc.Cube, "Cannot solve a non cube"

        for col in {"[r]","[g]","[b]","[o]"}:
            e = list(cube.has_colour(cube["D"].colour) & cube.has_colour(self.ColorDict[col]) & cube.select_type("edge"))[0]
            faces = list(e.facings)
            white = faces[1]
            other = faces[0]
            if e[faces[0]].__str__() == "[w]":
                white = faces[0]
                other = faces[1]
            if white == 'D': # white square on the bottom face
                if self.ColorDict[col] != cube[other].colour: # If the other square does not match the face that it is on
                    cube(other + "2")
                    e = list(cube.has_colour(cube["D"].colour) & cube.has_colour(self.ColorDict[col]) & cube.select_type("edge"))[0]
                    faces = list(e.facings)
                    other = faces[0]
                    if e[faces[0]].__str__() == "[w]":
                        other = faces[1]
                    while self.ColorDict[col] != cube[other].colour:
                        cube("U")
                        e = list(cube.has_colour(cube["D"].colour) & cube.has_colour(self.ColorDict[col]) & cube.select_type("edge"))[0]
                        faces = list(e.facings)
                        other = faces[0]
                        if e[faces[0]].__str__() == "[w]":
                            other = faces[1]
                    cube(other + "2")
            elif white == 'U': # if the white square is on the top face
                while self.ColorDict[col] != cube[other].colour:
                    cube("U")
                    e = list(cube.has_colour(cube["D"].colour) & cube.has_colour(self.ColorDict[col]) & cube.select_type("edge"))[0]
                    faces = list(e.facings)
                    other = faces[0]
                    if e[faces[0]].__str__() == "[w]":
                        other = faces[1]
                cube(other + "2")
            elif other == 'U':
                while self.ColorDict[col] != cube[white].colour:
                    cube("U")
                    e = list(cube.has_colour(cube["D"].colour) & cube.has_colour(self.ColorDict[col]) & cube.select_type("edge"))[0]
                    faces = list(e.facings)
                    white = faces[1]
                    if e[faces[0]].__str__() == "[w]":
                        white = faces[0]
                cube("U")
                rotation = "FLBR"
                ind = list(rotation).index(white)
                cube(rotation[(ind + 1) % 4] + " " + rotation[ind] + "' " + rotation[(ind + 1) %4])                                

