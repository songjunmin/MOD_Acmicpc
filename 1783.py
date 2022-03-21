row, line = map(int, input().split())

ans = 0
if row < 2:
    ans = 1

elif row < 3:
    ans = (line-1)//2 +1
    if ans > 4:
        ans = 4

else:
    if line < 5:
        ans = line
    elif line < 6:
        ans = line-1
    else:
        ans = line-2

print(ans)

