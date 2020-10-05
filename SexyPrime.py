def isprime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
    
def primepairs(l,r):
    lst = []
    pairs = []
    count = 0
    for i in range(l,r):
        if(isprime(i)):
            lst.append(i)
    # print(lst)
    for k in range(len(lst)): 
        for j in range(k + 1, len(lst)): 
            # print(k, j ,lst[k],lst[j])
            if (SexyPrime(lst[k], lst[j])):
                pairs.append((lst[k],lst[j]))
                count += 1
    print(pairs) def isprime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
    
def primepairs(l,r):
    lst = []
    pairs = []
    count = 0
    for i in range(l,r):
        if(isprime(i)):
            lst.append(i)
    # print(lst)
    for k in range(len(lst)): 
        for j in range(k + 1, len(lst)): 
            # print(k, j ,lst[k],lst[j])
            if (SexyPrime(lst[k], lst[j])):
                pairs.append((lst[k],lst[j]))
                count += 1
    return count

def SexyPrime(n1, n2): 
    return (abs(n1 - n2) == 6)
 
l = int(input())
r = int(input())
print(primepairs(l,r))
