def numbers():
    ans = []
    while True:
        num = int(input('Ваше число (для отключения - напишите ноль):'))
        if num == 0:
            break
        ans.append(num)
    ans.sort()
    print(ans)

print(numbers())