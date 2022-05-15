#15 28 19

E, S, M = map(int,input().split())

num = S
while True:
    if num % 15 == E % 15:
        if num % 19 == M % 19:
            break

        else:
            num += (15*28)

    else:
        num += 28
print(num)
