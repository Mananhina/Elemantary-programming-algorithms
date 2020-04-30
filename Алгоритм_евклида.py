def gcd(a, b):
    while a != b != 0:
        a, b = b, a % b
    return(a)
a = int(input())
b = int(input())
print(gcd(a, b))