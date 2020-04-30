n = int(input())
A = [list(map(int, input().split())) for i in range(n)]
c = 0
m = 0
for i in A:
    c = 0
    for j in A:
        if  j[0] <= i[1] <= j[1] or j[0] <= i[0] <= j[1]:
            c += 1
    c -= 1
    if c > m:
        m = c
print(m)