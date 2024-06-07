import math

def check_nt(m):
    if m < 2:
        return False 
    for i in range(2,int(math.sqrt(m))+1):
        if m % i == 0: 
            return False
    return True

n = int(input())
for i in range(1,n):
    if check_nt(i):
        print(i,' ')