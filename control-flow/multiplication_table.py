# multiplication_table.py

# Prompt user for a number
num = int(input("Enter a number to see its multiplication table: "))

# Print multiplication table from 1 to 10
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")
