# pallindrome or not using python

num = int(input("enter your number"))
s=0
m = num
while num > 0:
    r = num%10
    s = s*10 + r
    num= num // 10

if s==m:
    print(f"{m} is pallindrome")  
else:
    print(f"{m} is not pallindrome") 


