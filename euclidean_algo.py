import sys

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
gcd = 0

#Since gcd(|a|,|b|)=gcd(a,b)
a = abs(a)
b = abs(b)
    
#Checking for a>b
if(a<b):
    a,b=b,a

#Checking for 0,0 condition
if b==0:
    print("GCD:",a)
    sys.exit()
if a==0 and b==0:
    print("GCD:0")
    sys.exit()

r = a%b

while (r > 0):
    a = b
    b = r
    r = a%b
    
    

print("GCD:",b)
