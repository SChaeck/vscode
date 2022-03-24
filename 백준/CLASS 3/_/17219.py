import sys

n, m = map(int, sys.stdin.readline().split())
dic = {}
for _ in range(n) :
    site, Pw = sys.stdin.readline().rstrip().split()
    dic[site] = Pw

for _ in range(m) :
    lk_site = sys.stdin.readline().rstrip()
    print(dic[lk_site])