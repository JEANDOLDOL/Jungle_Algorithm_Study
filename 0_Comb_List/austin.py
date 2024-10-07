a_size, b_size = map(int, input().split())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

combined_list = sorted(a_list + b_list)

print(' '.join(map(str, combined_list)))
