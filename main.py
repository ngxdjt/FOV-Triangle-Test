import math
import triangle

A = 67
pos = (6,7)
fov = 67*(math.pi/180)

sight = triangle.generate(pos, A, fov)

print(triangle.pointBFS(pos, sight))

