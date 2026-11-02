num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print(original, "is a palindrome")
else:
    print(original, "is not a palindrome")

    limit = int(input("Enter the limit: "))

print("Perfect numbers are:")

for num in range(1, limit + 1):

    sum = 0

    for i in range(1, num):
        if num % i == 0:
            sum = sum + i

    if sum == num:
        print(num)
