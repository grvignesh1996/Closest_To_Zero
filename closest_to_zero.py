import sys
import math

n = int(input())  # the number of temperatures to analyse


def close_zero():
    li = []
    pos = []
    neg = []
    j = 1
    for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(i)
        li.append(t)
    m = len(li)
    for i in range(m):
        if li[i] > 0:
            pos.append(li[i])
        elif li[i] < 0:
            neg.append(li[i])
        else:
            j = 0
            
    pos = sorted(pos)
    neg = sorted(neg)
    
    if j == 0:
        print(j)
    elif len(pos) == 0:
        print(neg[-1])
    elif len(neg) == 0:
        print(pos[0])
    elif pos[0] == abs(neg[-1]):
        print(pos[0])
    elif pos[0] < abs(neg[-1]):
        print(pos[0])
    else:
        print(-abs(neg[-1]))
    
        
if n == 0:
    print(n)
else:
    close_zero()
    

