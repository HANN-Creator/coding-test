input_value = input()
row = int(input_value[1])
coordinate = int(ord(input_value[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
result = 0
for step in steps:
    next_row = row + step[0]
    next_coordinate = coordinate + step[1]
    if next_row >= 1 and next_row <= 8 and next_coordinate >= 1 and next_coordinate <= 8:
        result += 1

print(result)