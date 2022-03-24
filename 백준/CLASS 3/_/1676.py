import math

n = int(input())
n_f = str(math.factorial(n))
cnt = 0

for i in n_f[::-1] :
    if i == '0' : cnt += 1
    else : break

print(cnt) 