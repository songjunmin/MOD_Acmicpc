size , goalY , goalX = map(int,input().split())
count = 0

def find(x,y,size):
    global count , goalX , goalY

    if size == 1:
        return

    if goalX < x+size//2 and goalY < y+size//2:
        find(x, y, size//2)

    elif goalY < y+size//2:
        count = count + (size // 2) ** 2
        find(x+size//2, y, size//2)

    elif goalX < x+size//2:
        count = count + (size//2)**2
        count = count + (size // 2) ** 2
        find(x, y+size//2, size//2)

    else:
        count = count + (size // 2) ** 2
        count = count + (size // 2) ** 2
        count = count + (size // 2) ** 2
        find(x+size//2, y + size // 2, size // 2)

find(0,0,2**size)

print(count)