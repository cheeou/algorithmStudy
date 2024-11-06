M = int(input())

first_list = set(map(int, input().split()))

N = int(input())

check_list = list(map(int, input().split()))


for num in check_list:
    if num in first_list:
        print(1)
    else:
        print(0)

