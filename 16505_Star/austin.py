"""
 - 길이
0 -> 1
1 -> 2
2 -> 4
3 -> 8
 - 넓이
1 ~ 2의 N 제곱

 
 - 예시
****************
* * * * * * * *
**  **  **  **
*   *   *   *
****    ****
* *     * *
**      **
*       *
********
* * * *
**  **
*   *
****
* *
**
*
16 ----
8
8
4
8
4
4
2
8 ---
4
4
2
4 --
2
2
1
"""
"""1차시도 실패"""
# n = int(input())
    
# def print_stars(n):
#     if n == 0:
#         print("*")
#         return
    
#     stars = ["*" * (2 ** (n + 1))]
#     for i in range(2 ** n - 1):
#         if i % 2 == 0:
#             stars.append("*" + " " * (2 ** n - 1) + "*")
#         else:
#             stars.append("*" * (2 ** n) + " " * (2 ** (n - 1)) + "*" * (2 ** n))
    
#     for line in stars:
#         print(line)
    
#     print_stars(n - 1)

# print_stars(n)


"""정답 코드 보고 이해하기"""

def Rec(i, x, y, count, arr):
    if i == 0:
        arr[x][y] = True

    else:
        count //= 2
        
        Rec(i-1, x, y, count, arr)
        Rec(i-1, x+count, y, count, arr)
        Rec(i-1, x, y+count, count, arr)


N = int(input()) #인풋받기

count = 2**N #인풋의 제곱의 수 = 시작 줄에 별 갯수(width), 총높이(heigh)

arr = [[False for _ in range(count)] for _ in range(count)] # 총높이, 총 넓이 만큼 리스트 만들기

Rec(N, 0, 0, count, arr) # 만든 arr에 별 넣기

for i in range(count):
    for j in range(count - i):
        if arr[i][j]:
            print("*", end="")
        else:
            print (" ", end="")
    print("")

"""
카운트를 통해 재귀를 했을때의 범위가 정해진다. 
n =2일때 Count = 2^2 인 4가 된다. 

최초의 rec실행시에는 4의 범위로서 시작한다. 그다음은 2 그다음은 1이다. 그리고 마침네 0이 되는데, 이때 해당 x, y 좌표에 true로 반환이 된다. 
총 3번의 재귀가 있다. 이는:
- x,y 
- x +count, y
- x, y+count
로 이루어져 있는데, 이는 왼쪽 위, 왼쪽 아래, 오른쪽 위를 뜻한다. 


"""