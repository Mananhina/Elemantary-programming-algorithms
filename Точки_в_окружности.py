r = int(input())
k = 0
for i in range(r + 1):
    c = int((r ** 2 - i ** 2) ** 0.5)
    k += c
print(k * 4 + 1)