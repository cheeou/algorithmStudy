count_num = int(input())

num_list = list(map(int, input().split()))

count = 0
for num in num_list:
    if num > 1:
        for i in range(2, int(num ** 0.5 + 1)):
            if num % i == 0:
                break
        else:
            count += 1
print(count)