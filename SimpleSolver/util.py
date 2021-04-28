import pycuber as pc

def Solved(cube):
    assert type(cube) == pc.Cube, "Cannot work with non cube"
    for x in ["U","D","R","L","F","B"]:
        face = cube.get_face(x)
        center = face[1][1].__str__()
        for i in face:
            for s in i:
                if(s.__str__() != center):
                    return False
    return True
            
    
