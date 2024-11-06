while True:
    nums = input()
    if nums == '0':
        break
    else:
        if nums == nums[::-1]:
            print('yes')
        else:
            print('no')

