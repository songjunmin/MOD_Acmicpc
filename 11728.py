import sys

a, b = map(int, sys.stdin.readline().split())
aList = list(map(int, sys.stdin.readline().split()))
bList = list(map(int, sys.stdin.readline().split()))
answerList = aList + bList
answer = ' '.join(map(str, sorted(answerList)))
print(answer)