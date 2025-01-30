import statistics
import random


def validate_temperature(value):
    try:
        float(value)
    except ValueError:
        print(f"Error: Invalid input: {value}. Ignoring this input.")
        return None

    if -50 <= value <= 150:
        return value
    print(f"Error: Invalid temperature: {value}. Ignoring this input.")
    return None


def process_temperatures(temp_list):
    if not temp_list:
        return "No Input Provided."

    """Process the list of temperatures and return min, max, and avg."""
    # valid_temps = [float(temp) for temp in temp_list]
    valid_temps = [validate_temperature(temp) for temp in temp_list if validate_temperature(temp) is not None]

    if not valid_temps:
        return "No valid input provided."

    min_temp = min(valid_temps)
    max_temp = max(valid_temps)
    avg_temp = round(statistics.mean(valid_temps), 2)

    return f"Min: {min_temp}°C, Max: {max_temp}°C, Avg: {avg_temp}°C"

def generate_random_list(size):
    rand_list = []
    for i in range(size):
        rand_list.append(random.randint(-50, 150))
    return rand_list

# Test Cases
# Students should analyze and ensure the correctness of the outputs

test_cases = [
    [20], # Single element list
    [15, 35], # Two element list
    [], # Empty list
    [10, -10, 30], # Negative temperature
    [-50, 20, 150, 25], # Bound Testing
    [10, "abc", 30], # String input
    [2**31, -1, -2**31], # Large numbers
    [10, 10, 10], # Same numbers
    [5, 151, -51], # Out of bound
    [12.521, -0.23, 11.424], # Float numbers
    generate_random_list(100) # Many Inputs
]

# Running the test cases
for i, case in enumerate(test_cases, start=1):
    print(f"Test Case {i}: {case}")
    print(process_temperatures(case))
    print("-" * 40)