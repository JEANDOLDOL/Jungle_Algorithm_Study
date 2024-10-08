"""
L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
P $	$라는 문자를 커서 왼쪽에 추가함


해결 방법: 
커서를 기준으로 양쪽에 스택으로 구현. 이를 통해 O(1)의 시간 복잡도를 성취할수 있다. (0.3초가 맥시멈 초기 때문)
"""

import sys

st1 = list(sys.stdin.readline().rstrip())  # 초기 문자열을 스택1에 저장
st2 = []  # 커서 오른쪽에 있는 문자를 저장할 스택2

# 명령의 수만큼 반복
for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()  # 명령을 입력받음
    
    if command[0] == 'L':  # 커서를 왼쪽으로 이동
        if st1:
            st2.append(st1.pop())
            
    elif command[0] == 'D':  # 커서를 오른쪽으로 이동
        if st2:
            st1.append(st2.pop())
    
    elif command[0] == 'B':  # 커서 왼쪽의 문자를 삭제
        if st1:
            st1.pop()
    
    else:  # 'P' 명령: 커서 왼쪽에 새로운 문자를 삽입
        st1.append(command[1])

# 최종적으로 st1에 st2를 역순으로 붙여서 출력
st1.extend(reversed(st2))
print(''.join(st1))

