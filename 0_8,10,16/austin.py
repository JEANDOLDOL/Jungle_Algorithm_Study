"""
int(number, 진법)을 활용하여 변환.
각각의 케이스 마다 예외 처리 해주기

"""
N =input()
ans = N

# If N is 8 or 16
if N[0] == '0':
    # 16
    if N[1] == 'x':
        ans = int(N,16)
    # 8
    else:
        ans = int(N,8)
print(ans)