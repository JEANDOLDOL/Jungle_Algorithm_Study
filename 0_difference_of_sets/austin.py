# // 자연수를 원소로 갖는 공집합이 아닌 두 집합 A와 B가 있다. 이때, 두 집합의 대칭 차집합의 원소의 개수를 출력하는 프로그램을 작성하시오. 두 집합 A와 B가 있을 때, (A-B)와 (B-A)의 합집합을 A와 B의 대칭 차집합이라고 한다.

# // 예를 들어, A = { 1, 2, 4 } 이고, B = { 2, 3, 4, 5, 6 } 라고 할 때,  A-B = { 1 } 이고, B-A = { 3, 5, 6 } 이므로, 대칭 차집합의 원소의 개수는 1 + 3 = 4개이다.

# // 2초 까지 가능 이중 for loopd -> dont need to bc I can use "in"
# 각각리스트에서 공통된 것들은 제외 하기
# 남아 있는 것들 카운트
# 걍 set사용하자


# a_length, b_length = map(int, input().split())


# a_list = list(map(int, input().split()))
# b_list = list(map(int, input().split()))


# a_check = a_list
# b_check = b_list
# for i in range(a_length):
#     # print("Iter: ",i)
#     if a_list[i] in b_list:
#         a_check.remove(a_list[i])
#         b_check.remove(a_list[i])
        



# a_left = len(a_check)
# b_left = len(b_check)


# print(a_left + b_left)



a_length, b_length = map(int, input().split())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))


set_a = set(a_list)
set_b = set(b_list)

symmetric_difference = (set_a - set_b).union(set_b - set_a)

print(len(symmetric_difference))
