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

n = int(input())
    
def print_stars(n):
    if n == 0:
        print("*")
        return
    
    stars = ["*" * (2 ** (n + 1))]
    for i in range(2 ** n - 1):
        if i % 2 == 0:
            stars.append("*" + " " * (2 ** n - 1) + "*")
        else:
            stars.append("*" * (2 ** n) + " " * (2 ** (n - 1)) + "*" * (2 ** n))
    
    for line in stars:
        print(line)
    
    print_stars(n - 1)

print_stars(n)