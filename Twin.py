def equal_neckless (n1 , n2) :
    sort_n1 = sorted(n1)
    sort_n2 = sorted(n2)
    return sort_n1 == sort_n2

t = int(input())
result = []


for i in range(t) :
    n1 , n2 = input().split()
    if equal_neckless (n1 , n2) :
        result.append('YES')
    else :
        result.append('NO') 

print ('\n'.join(result))