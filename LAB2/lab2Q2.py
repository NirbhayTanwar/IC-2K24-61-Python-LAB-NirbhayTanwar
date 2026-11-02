limit = int(input("Enter the limit: "))

print("Prime numbers are:")

for num in range(2, limit + 1):

    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)
