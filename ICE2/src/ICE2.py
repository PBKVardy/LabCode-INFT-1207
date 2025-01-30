import statistics


def validate_temperature(value):
    # You have to complete this function
    if -50 <= value <= 150:
        return value
    return None


def process_temperatures(temp_list):
    if not temp_list:
        return "No Input Provided."

    """Process the list of temperatures and return min, max, and avg."""
    #valid_temps = [float(temp) for temp in temp_list]
    valid_temps = [validate_temperature(temp) for temp in temp_list if validate_temperature(temp) is not None]

    if not valid_temps:
        return "No valid input provided."

    min_temp = min(valid_temps)
    max_temp = max(valid_temps)
    avg_temp = round(statistics.mean(valid_temps), 2)

    return f"Min: {min_temp}°C, Max: {max_temp}°C, Avg: {avg_temp}°C"


# Test Cases
# Students should analyze and ensure the correctness of the outputs

test_cases = [
    [20],
    [15, 30],
    [],
    [10, -10, 30],
    [-50, 20, 150, 25],
    [10, "abc", 30],
    [2**31, -1, -2**31],
    [10, 10, 10]
]

# Running the test cases
for i, case in enumerate(test_cases, start=1):
    print(f"Test Case {i}: {case}")
    print(process_temperatures(case))
    print("-" * 40)