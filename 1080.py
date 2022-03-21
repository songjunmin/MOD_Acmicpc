def Change(x,y,list):
    for i in range(3):
        for j in range(3):
            list[x+i][y+j] = (list[x+i][y+j]+1) % 2
    return list

n , m = map(int,input().split())

matA=[]
matB=[]
count = 0
ansPrint = True

for i in range(n):
    matA.append(list(map(int,input())))

for i in range(n):
    matB.append(list(map(int,input())))

for i in range(n-2):
    for j in range(m-2):
        if matA[i][j] != matB[i][j]:
            matA = Change(i,j,matA)
            count += 1

    if matA[i][m-2] != matB[i][m-2] or matA[i][m-1] != matB[i][m-1]:
        print(-1)
        ansPrint = False
        break

if matA[n-2] != matB[n-2] or matA[n-1] != matB[n-1]:
    if ansPrint:
        print(-1)

else:
    if ansPrint:
        print(count)
