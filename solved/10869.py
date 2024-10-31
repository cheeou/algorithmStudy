"""
문제
두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.

입력
두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)

출력
첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

====
처음에 시도한 더러운 코드
a = input().split()

print(int(a[0]) + int(a[1])) # a + b
print(int(a[0]) - int(a[1])) # a - b
print(int(a[0]) * int(a[1])) # a * b
print(int(a[0]) / int(a[1])) # a / b
print(int(a[0]) % int(a[1])) # a % b

나누기 연산자 값에서 소수자리가 나타나는데 저 연산을 int로 한번 감아야되니까 접근 자체가 잘못됨
"""

a, b = map(int, input().split())
print(a, b)
print(type(a))

print(a + b)

print(a - b)
print(a * b)
print(a // b)
print(a % b)
