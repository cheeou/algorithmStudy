# 구구단
# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

gugu_num = int(input())

for i in range(9):
    print(f"{gugu_num} * {i + 1} = {gugu_num * (i + 1)}")