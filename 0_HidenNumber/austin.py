"""
- First try
[char for char in word if char.isdigit()]

6자리 연속되는 하나의ㅏ 숫자도 있다. 

하나의 숫자를 발견 했을때, 더이상 숫자가 안나올때까지 확인 해야한다. 
Options:
1. 숫자를 찾고 나서 while loop돌며 연속된 숫자 탐색
2. 기본 for loop에 flag를 만들어 연속적인 숫자인지 체크한다

"""



N = int(input())
word = input()

flag = False
tempNum = []
numList = []
for i in range(N):
    if word[i].isdigit():
        #When continuous
        if flag == True:
            tempNum.append(word[i])
        #When Not continuous
        else:
            flag = True
            tempNum.append(word[i])
    else:
        if flag:
            flag = False
            if len(tempNum) == 1:
                numList.append(tempNum[0])
            elif len(tempNum) > 1:
                aNum = ''.join(tempNum)
                numList.append(aNum)
            tempNum.clear()

if flag:
    aNum = ''.join(tempNum)
    numList.append(aNum)

ans = [int(i) for i in numList]
print(sum(ans))



