# split
names = "Dave,David,Andy"

print(type(names.split(',')))

for names_list in names.split(','):
    print(names_list)

# include index
# enumerate
for index, name in enumerate(names.split(','), start=1):
    print(f"{index}번 {name}")

# 기본 for
i = 1
for name in names.split(','):
    print(i, name)
    i += 1

# range len
namae = ['mimi', 'nana', 'wawa']
namaes = ""
for i in range(len(namae)):
    namaes += namae[i]
    print(f"순번:{i + 1}, 이름:{namaes}")


# 파일 확장자
filename = "exercise01.docx"

print(filename.split('.docx')[0]) # split으로 리스가 만들어졌으니 원하는 데이터의 인덱싱 위치를 생각해야됨


