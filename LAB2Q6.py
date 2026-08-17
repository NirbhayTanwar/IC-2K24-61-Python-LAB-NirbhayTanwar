# Pattern Printing using Nested Loops

n = int(input("Enter the number of rows: "))

# --------------------------------
# 1. Right-angled triangle of stars
# --------------------------------
print("\n1. Right-angled Triangle")

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


# --------------------------------
# 2. Number pattern
# --------------------------------
print("\n2. Number Pattern")

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# --------------------------------
# 3. Centered Pyramid
# --------------------------------
print("\n3. Centered Pyramid")

for i in range(1, n + 1):

    # Print spaces
    for j in range(1, n - i + 1):
        print(" ", end=" ")

    # Print stars
    for j in range(1, 2 * i):
        print("*", end=" ")

    print()