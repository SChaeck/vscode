n = int(input())
n1_ro = int(n**(1/2))
se = set()
check1 = check2 = 1

if n == n1_ro**2 : se.add(1)
else :
    for a in range(n1_ro, 0, -1) :
        n2_ro = int((n - a**2)**(1/2))
        if n == a**2 + n2_ro**2 : 
            se.add(2)
            break
        elif check1 :
            for b in range(n2_ro, 0, -1) :
                n3_ro = int((n-a**2-b**2)**(1/2))
                if n == a**2 + b**2 + n3_ro**2 : 
                    se.add(3)
                    check1 = 0
                    break
                elif check2 :
                    for c in range(n3_ro, 0, -1) :
                        n4_ro = int((n-a**2-b**2-c**2)**(1/2))
                        if n == a**2 + b**2 + c**2 + n4_ro**2 :
                            se.add(4)
                            check2 = 0
                            break

print(min(se))

# 다음번에는 동적계획법으로 풀고 싶음 check