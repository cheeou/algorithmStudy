num_count = int(input())
numbers = input().split()

real_numbers = list(map(int, numbers))

print(f"{int(min(real_numbers))} {int(max(real_numbers))}")