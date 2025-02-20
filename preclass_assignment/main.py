from functions import greet, goldilocks, square_list_from_user, fibonacci_stop, clean_pitch

# Exercise 1
print(greet('world'))

# Exercise 2
bed_length = int(input("Enter the bed length: "))
print(goldilocks(bed_length))

# Exercise 3
print("Enter numbers separated by spaces:")
user_input = input()  # Get input from the user as a single string
numbers = [float(num) for num in user_input.split()]  # Convert input to a list of numbers
print("The squared numbers are:", square_list_from_user(numbers))

# Exercise 4
max_value = int(input("Enter the maximum value for the Fibonacci sequence: "))
print("Fibonacci sequence:", fibonacci_stop(max_value))

# Exercise 5
x = [-1, 2, 6, 95, 76]  # "raw" pitch angles
status = [1, 0, 0, 0, 0]  # status signals
print("Cleaned pitch data:", clean_pitch(x, status))
