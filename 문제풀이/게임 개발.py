n, m = map(int, input().split())
d = [[0] * m for _ in range(n)]
x,y, diction = map(int(input().split()))
d[x][y] = 1

array = []
for i in range():
    array.append(list(map(int,input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global diction
    diction -= 1
    if diction == -1:
        diction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[diction]
    ny = y + dy[diction]
    if d[nx][ny] == 0 and array[nx][ny]:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[diction]
        ny = y - dy[diction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(count)
