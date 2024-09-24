def draw_star(arr, x, y, n):
    if n == 1:
        arr[x][y] = "*"
        return
    div = n //3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            draw_star(arr, x + i * div, y + j * div,div)

N = int(input())

arr = [[' ' for _ in range(N)] for _ in range(N)]


draw_star(arr, 0, 0, N)


for row in arr:
    print(''.join(row))