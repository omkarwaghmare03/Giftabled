i=4073 

i=int(input("Enter a number:"))

rev=0

while (i>0):
    # 4073>0 is true 
    rev= (rev*10)+i%10
    # 0=(0*10=0)+4073 % 10 (4073 ÷ 10 leaves a remainder of 3,% operator gives the remainder.)
    #0+3=3
    i=i//10 # i=i double divide by 10= 407.3 and double divide means ignoring the value after decimal = 407

print("Reverse=",rev)