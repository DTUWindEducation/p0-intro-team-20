#task 1
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

#task 2
def goldilocks(length):
    if 140 <= length <= 150:
        print("Just Right!")
    elif length < 140:
            print("Too Short!")
    else:
            print(f"Too Long!")

goldilocks(139)

#task 3
def square(numbers):
    return[num**2 for num in numbers]
print(square([1,2,3]))

#task 4
def fibonacci_stop(max_value):
    fib_sequence = [1, 1]  # Start with the first two Fibonacci numbers
    while fib_sequence[-1] + fib_sequence[-2] <= max_value:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

print(fibonacci_stop(20))  # Output: [1, 1, 2, 3, 5, 8, 13]

#task 5
def clean_pitch(angles, statuses):
    cleaned = []
    for angle, status in zip(angles, statuses):
        if (angle < 0 or angle > 90) and status > 0:
            cleaned.append(-999)  # Mark as bad value
        else:
            cleaned.append(angle)  # Keep original value
    return cleaned

angles = [10, 95, 30, -5, 85, 100]
statuses = [0, 1, 0, 1, 2, 0]

print(clean_pitch(angles, statuses))
# Output: [10, -999, 30, -999, 85, 100]
