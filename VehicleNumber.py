def vehiclenumber(n,alpha,num):
  start = int(num[0])
  end = int(num[1])
  alpha1 = alpha[0]
  alpha2 = alpha[1].rstrip()
  digit = end - start + 1
  alph = ord(alpha2)-ord(alpha1)+1
  result = n*(alph*alph)*(digit*digit*digit*digit)
  return result
  
n = int(input())
alpha = input().split(" ")
num = input().split(" ")
print(vehiclenumber(n,alpha,num))