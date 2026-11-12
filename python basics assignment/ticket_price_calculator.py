age = int(input("Enter your age: "))

if age < 5:
    price = 0
elif age <= 17:
    price = 100
elif age <= 59:
    price = 200
else:
    price = 100

print("Your ticket price is ₹", price)