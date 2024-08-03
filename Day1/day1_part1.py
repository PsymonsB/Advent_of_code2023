import re

def extract_and_combine_digits(line):
    # Extract the first digit from the left
    left_match = re.search(r'\d', line)
    left_digit = left_match.group(0)

    # Extract the first digit from the right
    right_match = re.search(r'\d', line[::-1])
    right_digit = right_match.group(0)

    # Combine the two digits into a single number
    combined_number = int(left_digit + right_digit)

    return combined_number

total_sum = 0
    
with open('input.txt', 'r') as file:
    for line in file:
        combined_number = extract_and_combine_digits(line.strip())
        total_sum += combined_number

print(f"Total sum of combined numbers: {total_sum}")


