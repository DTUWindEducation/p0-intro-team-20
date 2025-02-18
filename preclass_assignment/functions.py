# TEAM 20
# Exercise 1
def greet(name):
    print(f"Hello, {name}!")

# Exercise 2
def goldilocks(bed_length):
    if bed_length < 140:
        print("The bed is too small.")
    elif bed_length > 150:
        print("The bed is too large.")
    else:
        print("Goldilocks is happy with the bed.")

# Exercise 3
def square_list_from_user(numbers):
    squared_numbers = [num ** 2 for num in numbers]  # Square each number
    return squared_numbers

# Exercise 4
def fibonacci_stop(max_value):
    fibonacci = [1, 1]  # Starting values: 1, 1
    while True:
        next_value = fibonacci[-1] + fibonacci[-2]
        if next_value > max_value:
            break
        fibonacci.append(next_value)
    return fibonacci

# Exercise 5
def clean_pitch(pitch_angles, status_signals):
    cleaned = []
    for pitch, status in zip(pitch_angles, status_signals):
        if (pitch < 0 or pitch > 90) and status > 0:
            cleaned.append(-999)  # Replace bad values with -999
        else:
            cleaned.append(pitch)  # Keep good values unchanged
    return cleaned
