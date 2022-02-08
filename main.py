h = 175
w = 65
s = 7000
t = 300
l = h / 4 + 0.37
dis = l * s
u = dis / t
rashod = 0.035 * w + (u**2 / h) * 0.029 * w
col = rashod * t
print(dis)
print(col)

