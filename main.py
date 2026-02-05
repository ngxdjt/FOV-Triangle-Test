import math
import triangle

A = 50
pos = (7,4)
fov = 50*(math.pi/180)

sight = triangle.generate(pos, A, fov)

print(triangle.pointBFS(pos, sight))

