T = int(input())

for i in range(T):
    S = input().split()

    for j in S[1]:
         print(j * int(S[0]), end="")

    print()