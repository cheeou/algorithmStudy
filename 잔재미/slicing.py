# personal_id = "12345-67890"
# print(personal_id[0:2])

personal_id = input("주민번호를 입력하세요. '-' 반드시 포함: ")

if personal_id[7] == "1":
    print("남성입니다.")
elif personal_id[7] == "2":
    print("여성입니다.")
else:
    print("성별 확인 불가, ")

birth_place_code = personal_id[8:10]

# 비교식 직관적이지 않음
# if "00" <= birth_place_code <= "08":
#     print("서울 출생")
# elif "09" <= birth_place_code <= "12":
#     print("부산")

if birth_place_code >= "0" and birth_place_code <= "8":
    print("서울 출생")
elif birth_place_code >= "9" and birth_place_code <= "12":
    print("부산 출생")
