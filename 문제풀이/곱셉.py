a = int(input())
b = int(input())
c = 0
d = 0
e = b

while b >= 10:
    b -= 10
    c += 1

print(a*b)

while c >= 10:
    c -= 10
    d += 1

print(a * c)

while d >= 10:
    d -= 10

print(a * d)
print(a * e)