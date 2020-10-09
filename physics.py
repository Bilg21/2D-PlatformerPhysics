import math

gravity = (0, 0.981)
drag = 0.999
elasticity = 0.75

def addVectors(v1, v2):
    (angle1, length1) = v1
    (angle2, length2) = v2
    x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y  = math.cos(angle1) * length1 + math.cos(angle2) * length2
    
    angle = 0.5 * math.pi - math.atan2(y, x)
    length  = math.hypot(x, y)

    return (angle, length)

def testAddVectors():
    gravity = (0, 0.2)
    v1 = (math.pi, 4.8)
    (r1, r2) = addVectors(v1, gravity)
    print("({},{}):({},{})".format(v1, gravity, r1, r2))
    

