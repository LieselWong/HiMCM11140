import random
chart = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]
sum = [0, 0, 0, 0, 0]
for i in range(5):
    for z in range(5):
        if i == z:
            chart[i][z] = 1
        if chart[i][z] != 0:
            continue
        x = random.randint(1, 9)
        chart[i][z] = x
        chart[z][i] = 1/x
print(chart)

for i in range(5):
    for z in range(5):
        sum[i] = sum[i] + chart[z][i]
print(sum)

for i in range(5):
    for z in range(5):
        chart[z][i] = chart[z][i]/sum[i]

print(chart)
