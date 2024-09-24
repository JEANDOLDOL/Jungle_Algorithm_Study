"""
키보드
헤어드라이기
핸드폰 충전기
디지털 카메라 충전기
키보드
헤어드라이기

순으로 사용하는데 오직 3구 인 멀티텝이다. 가장 적은 횟수의 플러그인하는 방법을 구하는 문제다. 

1. 아직 멀티탭이 다 안차있을경우
2. 다 차있을 경우
    1. 새로 사용해야 하는 도구가 이미 꽃혀 있는 경우 컨티뉴
    2. 기존것을 뺴고 새로 꽂아야 하는 경우
        1. 앞으로 다시 써야 하는 경우 
            1. 1개 이상 다시 써야 한느 경우
                1. 다시 쓰는 것 끼리 순서 비교
        2. 앞으로 다시 안쓰거나 먼 나중에 다시 쓰는경우

"""

N, K = map(int, input().split())

iter = list(map(int, input().split()))

multitap = [-1 for i in range(N)]

unplug_count = 0


check_empty = False
for i in range(K):
    # 앞으로 넣을 기기
    current_device = iter[i]

    # 멀티탭에 이미 꽂혀 있으면 넘어감
    if current_device in multitap:
        continue

    # 빈 공간이 있으면 꽂음
    if -1 in multitap:
        for i in range(N):
            if multitap[i] == -1:
                multitap[i] = current_device
                break

    #다 차있을 경우
    else:
        fartest_ind = -1
        to_unplug = -1
        
        for j in range(N):
            # 앞으로 다시 안쓰는 기기
            if multitap[j] not in iter[i:]:
                to_unplug = j
                break
            # 앞으로 다시 쓰는 기기
            else:
                # 일찍 다시 쓰는 경우 
                next = iter[i:].index(multitap[j])
                # 나중에 다시 쓰는 경우 (빼도 됨)
                if next > fartest_ind:
                    fartest_ind = next
                    to_unplug = j

        multitap[to_unplug] = current_device
        unplug_count+=1

                

print(unplug_count)