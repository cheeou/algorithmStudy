test_case = int(input())
compare_s = []

for i in range(test_case):
    s = input()
    compare_s.append(s)

del_duplicate_s = list(sorted(set(compare_s), key=lambda x: (len(x), x)))
for j in del_duplicate_s:
    print(j)
