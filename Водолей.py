def gcd(a, b):
    while a != b != 0:
        a, b = b, a % b
    return(a + b)

a = int(input())
b = int(input())
n = int(input())

if (n > a and n > b) or (n % gcd(a, b) != 0):
    print("Impossible")
else:
    av = a
    bv = b
    a = 0
    b = 0    
    while a!= n and b != n:
        if a == 0:
            a = av
            print('>A')
        elif b != bv:
            free = bv - b
            if free >= a:
                b += a
                a = 0
            else:
                a -= free
                b += free
            print('A>B')
        elif b == bv:
            b = 0
            print('B>')
