HEIGHT = 175
WEIGHT = 65
steps = 7000
time = 300
length = HEIGHT / 4 + 0.37
dist = length * steps
speed = dist / time
rashod = 0.035 * WEIGHT + (speed**2 / HEIGHT) * 0.029 * WEIGHT
col = rashod * time
print(dist)
print(col)

