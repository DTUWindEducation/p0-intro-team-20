# Milton Mahdi - s242810 

# Exercise 1
def greet(name):
    print(f"Hello, {name}!")

greet('world')

# Exercise 2
bed_length = int(input("Enter the bed length: "))

# Call the goldilocks function with the user input
def goldilocks(bed_length):
    if bed_length < 140:
        print("The bed is too small.")
    elif bed_length > 150:
        print("The bed is too large.")
    else:
        print("Goldilocks is happy with the bed.")

# Call the goldilocks function with the user input
goldilocks(bed_length)

# Exercise 3
def square_list_from_user():

    print("Enter numbers separated by spaces:")
    user_input = input()  # Get input from the user as a single string
    numbers = [float(num) for num in user_input.split()]  # Convert input to a list of numbers
    squared_numbers = [num ** 2 for num in numbers]  # Square each number
    return squared_numbers

# Example usage
print("The squared numbers are:", square_list_from_user())

# Exercise 4
def fibonacci_stop():

    # Ask the user for the maximum value
    max_value = int(input("Enter the maximum value for the Fibonacci sequence: "))
    
    # Initialize the Fibonacci sequence
    fibonacci = [1, 1]  # Starting values: 1, 1
    
    # Generate the sequence using a while loop
    while True:
        next_value = fibonacci[-1] + fibonacci[-2]  # Calculate the next number
        if next_value > max_value:  # Stop if the next number exceeds the max value
            break
        fibonacci.append(next_value)  # Add the next number to the sequence
    
    return fibonacci

# Example usage
print("Fibonacci sequence:", fibonacci_stop())

# Exercise 5
def clean_pitch(pitch_angles, status_signals):
    cleaned = []
    
    for pitch, status in zip(pitch_angles, status_signals):
        if (pitch < 0 or pitch > 90) and status > 0:
            cleaned.append(-999)  # Replace bad values with -999
        else:
            cleaned.append(pitch)  # Keep good values unchanged
    
    return cleaned

# Example usage
x = [-1, 2, 6, 95,76]  # "raw" pitch angles
status = [1, 0, 0, 0,0]  # status signals
print(clean_pitch(x, status))  # Output: [-999, 2, 6, 95]

# this is the end, lets push again
