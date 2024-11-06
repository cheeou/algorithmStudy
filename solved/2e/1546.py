score_count = int(input()) # 과목 갯수

subjects = list(map(int, input().split()))

print(subjects)
new_avg = sum(subjects)/max(subjects)*100/score_count
print(new_avg)
