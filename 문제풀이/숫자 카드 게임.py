a,b = map(int,input().split())
result=0
for i in range(a):
    numbar=list(map(int,input().split()))
    minimum = min(numbar)
    result = max(result,minimum)

print(result)