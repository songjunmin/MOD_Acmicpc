posiList=[]
negaList=[]
zeroCount = 0
oneCount = 0
sum = 0

lot = int(input())

for i in range(lot):
    num = int(input())
    if num < 0:
        negaList.append(num)
    elif num == 1:
        oneCount += 1
    elif num > 0:
        posiList.append(num)
    else:
        zeroCount += 1

negaList.sort()
posiList.sort()

if len(negaList) % 2 == 0:
    for i in range(0,len(negaList),2):
        sum += (negaList[i] * negaList[i+1])

else:
    for i in range(0,len(negaList)-1,2):
        sum += (negaList[i] * negaList[i+1])

    if zeroCount == 0:
        sum += negaList[-1]

if len(posiList) % 2 ==0:
    for i in range(len(posiList)-1,-1,-2):
        sum += (posiList[i] * posiList[i-1])

else:
    for i in range(len(posiList)-1,0,-2):
        sum += (posiList[i] * posiList[i-1])

    sum += posiList[0]


sum += oneCount

print(sum)