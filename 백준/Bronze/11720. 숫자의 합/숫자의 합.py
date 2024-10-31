numbers_count = int(input())

numbers = list(input())
# print(numbers)
subtotal = 0

for i in numbers:
    subtotal += int(i)
print(subtotal)