# numbers = input().split()
#
# print(numbers) # []
# print(type(numbers)) # list type
#
# print(numbers[0])
# print(numbers[1])
#
# print(int(numbers[0])/int(numbers[1]))

# num1, num2 = map(int, input().split())
# print(type(num1)) # int
# print(num1/num2)

# numbers = input().split()
#
# if int(numbers[0]) > int(numbers[1]):
#     print('>')
# elif int(numbers[0]) < int(numbers[1]):
#     print('<')
# elif int(numbers[0]) == int(numbers[1]):
#     print('==')

# star_num = int(input())
#
# for i in range(star_num):
#     print('*' * (i + 1))

# numbers = []
#
# for i in range(9):
#     number = int(input())
#     numbers.append(number)
#
# print(max(numbers)) # max()
# print(numbers.index(max(numbers)) + 1) # index()

# test_case_count = int(input())

# for i in range(test_case_count):
#     s = input().split()
#     # print(s)
#     for j in s[1]:
#         print(j * int(s[0]), end='') # 기본적으로 print 기본 end 값은 줄바꿈으로 end=''로 아무 값도 넣지 않고 한줄로 출력
#     print()

# count = int(input())
#
#
# for i in range(count):
#     S = input().split()
#     for j in S[1]:
#         print(j * int(S[0]), end='')
#     print()

# count = int(input())
# nums = input().split()
#
# max_n = map(int, nums)
# min_n = map(int, nums)
#
# print(max(max_n), min(min_n))

count = int(input())
nums = input()

sub = 0

for i in nums:
    sub += int(i)
print(sub)