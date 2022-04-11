num = int(input())
numList = list(map(int,input().split()))

check = 0
for i in range(num-1,0,-1):
    if numList[i] > numList[i-1]:
        check = i
        break

if check == 0:
    print(-1)

else:
    numList2 = [i for i in range(1,num+1)]

    for i in range(0,check-1):
        print(numList[i] , end=" ")
        numList2.remove(numList[i])

    nextNum = numList2[numList2.index(numList[check-1])+1]

    print(nextNum, end = " ")
    numList2.remove(nextNum)

    for i in range(len(numList2)-1):
        print(numList2[i] , end= " ")
    print(numList2[-1])

