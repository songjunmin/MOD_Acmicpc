import sys

count = int(input())

s = []

for i in range(count):
    order = sys.stdin.readline()

    if order[0:3] == "add":
        temp , num = order.split()

        if num not in s:
            s.append(num)

    elif order[0:3] == "che":
        temp, num = order.split()

        if num not in s:
            sys.stdout.write("0\n")
        else:
            sys.stdout.write("1\n")

    elif order[0:3] == "rem":
        temp, num = order.split()

        if num in s:
            s.remove(num)

    elif order[0:3] == "all":
        s = [str(i) for i in range(1,21)]

    elif order[0:3] == "emp":
        s = []

    elif order[0:3] == "tog":
        temp, num = order.split()

        if num not in s:
            s.append(num)

        else:
            s.remove(num)