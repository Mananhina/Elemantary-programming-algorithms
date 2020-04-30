a = int(input())
b = int(input())
c = 0
while a != 0 and b != 0:
    c += a // b
    a, b = b, a % b
print(c)