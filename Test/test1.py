T = int(input())
for i in range(T):
    a = input()
    b = input()
    count = 0
    for x in a:
        for y in b:
            if x == y:
                count+=1
    tlen = len(a) + len(b)
    print(tlen - (2*count))
