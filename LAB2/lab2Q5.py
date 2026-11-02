# Fibonacci Series using Loop and Recursion

n = int(input("Enter the number of terms: "))

# -------------------------------
# Version 1: Using Loop
# -------------------------------
print("\nFibonacci series using loop:")

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# -------------------------------
# Version 2: Using Recursion
# -------------------------------

call_count = 0

def fibonacci(num):
    global call_count
    call_count += 1

    if num <= 1:
        return num

    return fibonacci(num - 1) + fibonacci(num - 2)


print("\n\nFibonacci series using recursion:")

for i in range(n):
    print(fibonacci(i), end=" ")

print("\n\nNumber of function calls made by recursion:", call_count)
