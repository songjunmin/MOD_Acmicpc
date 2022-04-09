import sys
sys.setrecursionlimit(10**5)

n = int(input())
inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))

pos = [0]*(n+1)
for i in range(n):
    pos[inOrder[i]] = i

def divide(inStart, inEnd, postStart, postEnd):
    if(inStart > inEnd) or (postStart > postEnd):
        return
    parents = postOrder[postEnd]
    print(parents, end=" ")

    left = pos[parents] - inStart
    right = inEnd - pos[parents]

    divide(inStart, inStart+left-1, postStart, postStart+left-1)
    divide(inEnd-right+1, inEnd, postEnd-right, postEnd-1)

divide(0, n-1, 0, n-1)

