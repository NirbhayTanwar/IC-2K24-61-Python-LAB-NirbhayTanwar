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


n = int(input("Enter the number of rows: "))

# Increasing section
for i in range(1, n + 1):
    left_stars = i
    right_stars = i
    middle_spaces = 2 * (n - i)

    print("*" * left_stars, end="")

    if middle_spaces > 0:
        print(" " * middle_spaces, end="")

    print("*" * right_stars)

# Decreasing section
for i in range(n - 1, 0, -1):
    left_stars = i
    right_stars = i
    middle_spaces = 2 * (n - i)

    print("*" * left_stars, end="")

    if middle_spaces > 0:
        print(" " * middle_spaces, end="")

    print("*" * right_stars)