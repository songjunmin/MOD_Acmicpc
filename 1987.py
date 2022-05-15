
board = []

max = 0

r, c = map(int,input().split())

for i in range(r):
    board.append(input())


def alpha(locX, locY, path ,dept):
    global max

    path[ord(board[locY][locX]) - ord("A")] = True
    dept += 1

    #print(dept, len(findTure(path)), findTure(path))

    check = False

    if locX + 1 < c and not path[ord(board[locY][locX + 1]) - ord("A")]:
        alpha(locX + 1, locY, path, dept)
        check = True

    if locY + 1 < r and not path[ord(board[locY + 1][locX]) - ord("A")]:
        alpha(locX, locY + 1, path, dept)
        check = True

    if locX - 1 >= 0 and not path[ord(board[locY][locX - 1]) - ord("A")]:
        alpha(locX - 1, locY, path, dept)
        check = True

    if locY - 1 >= 0 and not path[ord(board[locY - 1][locX]) - ord("A")]:
        alpha(locX, locY - 1, path, dept)
        check = True

    if not check:
        if max < dept:
            max = dept
        #print(path,dept)
    path[ord(board[locY][locX]) - ord("A")] = False


startPath = [False] * 26
alpha(0, 0, startPath, 0)
print(max)