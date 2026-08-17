num = int(input("Enter a number: "))

# Count the number of digits
digits = len(str(num))

# Store original number
original = num

sum = 0

# Calculate Armstrong sum
while num > 0:
    digit = num % 10
    sum = sum + digit ** digits
    num = num // 10

# Check
if sum == original:
    print(original, "is an Armstrong number")
else:
    print(original, "is not an Armstrong number")