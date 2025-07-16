# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop for rows
while row < size:
    # Inner for loop for columns
    for _ in range(size):
        print("*", end="")
    print()  # Newline after each row
    row += 1
