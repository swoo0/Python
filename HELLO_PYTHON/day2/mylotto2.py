import random

arr45 = [
         1,2,3,4,5,       6,7,8,9,10,
         11,12,13,14,15,  16,17,18,19,20,
         21,22,23,24,25,  26,27,28,29,30,
         31,32,33,34,35,  36,37,38,39,40,
         41,42,43,44,45
        ]

arr6 = []

while len(arr6) < 6 :
    rnd = int(random.random() * 45)
    if arr45[rnd] > 0:
        arr6.append(arr45[rnd])
        arr45[rnd] = -1
    else :
        continue

print(arr6)