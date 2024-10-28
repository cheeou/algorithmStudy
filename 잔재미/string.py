# count, 포함된 문자열 갯수 반환

sentence = "파이썬 썬칩 칩거 거위 위선 선수 수달 달리기 기기 기린"

counts_gi = sentence.count("기")

print(counts_gi)

# find, 인덱스 반환

letter = input()

if letter.find('우') >= 0:
    print("True")
else:
    print("False")