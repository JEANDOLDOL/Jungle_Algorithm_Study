"""
첫 시도

두개의 색종이를 비교해서 겹치는 부분을 구함.
구한 겹치는 넓이를 총 넓이에서 뺌

근데 중복 값 처리며, 너무 노가다였다. 


N = int(input())

papers = []

for _ in range(N):
    a, b = map(int, input())
    papers.append([a,b])


default_area = N*10*10

for i in range(papers):
    for j in range(papers):
        # Continue if same
        if i[0] == j[0] and i[1] == j[1]:
            continue
        # check if i and j are overlapped
        if i[0] < j[0] < i[0]+10:
            if i[1] < j[1] < i[1]+10:
                #Case 1: left up
                width = i[0]+10 - j[0]
                height = i[1]+10 - j[1]
                overlapped_area = width*height
            elif i[1] < j[1]+10 < i[1]+10:
                #Case 2: right up
        elif i[0] < j[0]+10 < i[0]+10:
            if i[1] < j[1] < i[1]+10:
                #Case 3: left down
            elif i[1] < j[1]+10 < i[1]+10:
                #Case 3: right down

"""

N = int(input())

# 기본 판 만들기
canvas = [[0] * 100 for _ in range(100)]

# 색종이 번위 만큼 기본 판에 1로 변경하기
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            canvas[i][j] = 1

# 1인 공간들 count하기
black_area = 0
for i in range(100):
    for j in range(100):
        if canvas[i][j] == 1:
            black_area += 1

print(black_area)
