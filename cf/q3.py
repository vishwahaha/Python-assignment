r1 = [int(n) for n in input().split()]
r2 = [int(n) for n in input().split()]
r3 = [int(n) for n in input().split()]
r4 = [int(n) for n in input().split()]
r5 = [int(n) for n in input().split()]

r = 0
c = 0

i1 = 0
while i1 < 5:
    if r1[i1] == 1:
        r = 1
        c = i1 + 1
        break
    i1 += 1

i2 = 0
while i2 < 5:
    if r2[i2] == 1:
        r = 2
        c = i2 + 1
        break
    i2 += 1

i3 = 0
while i3 < 5:
    if r3[i3] == 1:
        r = 3
        c = i3 + 1
        break
    i3 += 1

i4 = 0
while i4 < 5:
    if r4[i4] == 1:
        r = 4
        c = i4 + 1
        break
    i4 += 1

i5 = 0
while i5 < 5:
    if r5[i5] == 1:
        r = 5
        c = i5 + 1
        break
    i5 += 1

ans = abs(r-3) + abs(c-3)
print(ans)