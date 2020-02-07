import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

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
        
    if len(pos) == 0:
        pos.append(10000)
    elif len(neg) == 0:
        neg.append(10000)
    pos = sorted(pos)
    res_neg = [abs(i) for i in neg]
    res_neg = sorted(res_neg)
    
    if j == 0:
        print(j)
    elif pos[0] == 0:
        print(0)
    elif res_neg[0] == 0:
        print(0)
    elif pos[0] == res_neg[0]:
        print(pos[0])
    elif pos[0] < res_neg[0]:
        print(pos[0])
    else:
        print(-res_neg[0])
    
        
if n == 0:
    print(n)
else:
    close_zero()
    

