import sys
import heapq

heap = []

for i in range(int(input())):
    num = sys.stdin.readline()
    num = int(num)

    if num > 0:
        heapq.heappush(heap, (num , num))

    elif num < 0:
        heapq.heappush(heap, (-num , num))

    else:
        if len(heap) == 0:
            sys.stdout.write("0\n")
        else:
            sys.stdout.write(str(heapq.heappop(heap)[1]) + "\n")


