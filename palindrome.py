i=12321

i=int(input("Enter a number:"))

rev=0
x=i

while(i>0):
    rev=(rev*10)+i%10
    i=i//10

if(x==rev):
    print("Palindrome Number")

else:
    print("Not Palindrome ");