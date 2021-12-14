L = [2, 8, 0, 9, 0, 7, 10, 0, 13]
for i in range(3):
    L.remove(min(L))
for i in range(3):
    L.append(0)
print(L)