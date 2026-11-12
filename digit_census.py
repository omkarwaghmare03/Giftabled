num=input("Enter a number:")

even= 0
odd= 0
zero= 0

for digit in str(num):
    if digit == "0":
        zero += 1
    elif int(digit)% 2 == 0:
        even += 1
    else:
        odd += 1

print("Even digits:", even)
print("odd digits:", odd)
print("zero digits:", zero)