import pycuber as pc

def UIMain():
    c = pc.Cube()
    alg = pc.Formula()
    random_alg = alg.random()
    c(random_alg)
    x = c.__str__()


UIMain()
