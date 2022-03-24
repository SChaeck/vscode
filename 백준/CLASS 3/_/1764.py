import sys

n, m = map(int, sys.stdin.readline().split())
se1 = set()
se2 = set()
se3 = set()
for _ in range(n) :
    name = sys.stdin.readline().rstrip()
    se1.add(name)
for _ in range(m) :
    name = sys.stdin.readline().rstrip()
    se2.add(name)

su = len(se1) + len(se2) - len(se1.union(se2))

print(su)

for i in se1 :
    if i in se2 :
        se3.add(i)
print('\n'.join(sorted(se3)))