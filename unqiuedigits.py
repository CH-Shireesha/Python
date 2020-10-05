def uniqueDigits(n):
    temp = 0
    l = []
    while(n != 0):
        temp = n%10
        if temp not in l:
            l.append(temp)
        n //= 10
    if(len(l) == 0):
        return "No unique"
    else:
        return len(l)

 
while True:
    try:
        n = int(input())
        print(uniqueDigits(n))
    except EOFError:
        break  