def uniqueDigits(l,r):
    cout = 0
    for i in range(l, r+1):
        n = i
        v = [0 for i in range(r+1)]
        while(n):
            if v[n%10] == 1:
                break
            v[n%10] = 1
            n //= 10
        if n == 0:
            cout += 1
    return cout

 
l = int(input())
r = int(input())
print(uniqueDigits(l,r))