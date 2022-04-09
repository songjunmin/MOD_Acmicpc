def binSearch(num, start, end):
    if start > end:
        return 0

    elif start >= len(numList):
        return 0

    elif start == end:
        if num == numList[start]:
            return 1
        else:
            return 0

    elif num > numList[(start + end) // 2]:
        return binSearch(num, (start + end) // 2 + 1, end)

    elif num < numList[(start + end) // 2]:
        return binSearch(num, start, (start + end)//2)

    elif num == numList[(start + end) // 2]:
        return 1


temp = int(input())

numList = list(map(int, input().split()))
numList.sort()
numLen = int(input())

numList2 = list(map(int, input().split()))

for i in range(0, len(numList2)-1):
    if binSearch(numList2[i],0,temp) == 1:
        print(1, end=" ")
    else:
        print(0, end=" ")

if binSearch(numList2[len(numList2)-1],0,temp) == 1:
    print(1, end="")
else:
    print(0, end="")