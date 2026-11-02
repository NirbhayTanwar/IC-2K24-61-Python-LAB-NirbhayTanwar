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

    n = int(input("Enter an odd number: "))

# Upper half
for i in range(n // 2 + 1):
    spaces = n // 2 - i
    print(" " * spaces, end="")

    if i == 0:
        print("*")
    else:
        middle_spaces = 2 * i - 1
        print("" + " " * middle_spaces + "")

# Lower half
for i in range(n // 2 - 1, -1, -1):
    spaces = n // 2 - i
    print(" " * spaces, end="")

    if i == 0:
        print("*")
    else:
        middle_spaces = 2 * i - 1
        print("" + " " * middle_spaces + "")
        
