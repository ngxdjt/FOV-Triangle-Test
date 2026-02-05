import math

def generate(pos: tuple, A: int, fov: int):
    h = math.ceil(math.sqrt(A/math.tan(fov/2)))
    v1 = (math.ceil(pos[0] + h*math.tan(fov/2)), pos[1]-h)
    v2 = (math.floor(pos[0] - h*math.tan(fov/2)), pos[1]-h)
    return (pos, v1, v2)

def area(triangle:tuple):
    v1 = triangle[0]
    v2 = triangle[1]
    v3 = triangle[2]
    return abs((v1[0] * (v2[1] - v3[1]) + v2[0] * (v3[1] - v1[1]) + v3[0] * (v1[1] - v2[1])) / 2.0)

def isInside(point: tuple, triangle: tuple):
    A = area(triangle)
    A1 = area([point,triangle[1],triangle[2]])
    A2 = area([triangle[0],point,triangle[2]])
    A3 = area([triangle[0],triangle[1],point])

    if A == A1 + A2 + A3:
        return True
    else:
        return False
    
def pointBFS(pos:tuple, triangle:tuple):
    pointer = [pos[0], pos[1]-1]
    passes = abs(triangle[0][1] - triangle[1][1])
    points = []
    while passes > 0:
        if isInside((pointer[0],pointer[1]), triangle):
            points.append((pointer[0],pointer[1]))
            if (pointer[0]-2*(abs(pointer[0]-pos[0])), pointer[1]) not in points:
                points.append((pointer[0]-2*(abs(pointer[0]-pos[0])), pointer[1]))
            pointer[0] += 1
        else:
            pointer[0] = pos[0]
            pointer[1] -= 1
            passes -= 1
    return points