test_case = int(input())
compare_s = []

for i in range(test_case):
    s = input()
    compare_s.append(s)

del_duplicate_s = list(set(compare_s))
print(del_duplicate_s.sort(key=lambda x: (len(x),x)))

