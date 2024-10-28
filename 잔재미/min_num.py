digit1 = int(input("첫번째 숫자 입력: "))
digit2 = int(input("두번째 숫자 입력: "))
digit3 = int(input("세번째 숫자 입력: "))

if digit1 < digit2:
    min = digit1
else:
    min = digit2

if min < digit3:
    print(f"min: {min}")
else:
    print(f"min: {digit3}")