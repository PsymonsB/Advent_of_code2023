import re

# Define a dictionary for spelled-out numbers
spelled_out_numbers = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,

    "orez": 0, "eno": 1, "owt": 2, "eerht": 3, "ruof": 4,
    "evif": 5, "xis": 6, "neves": 7, "thgie": 8, "enin": 9,
}

def extract_numbers_from_text(text):
    """Extract all valid numbers (either digit or spelled-out) from the text."""
    pattern = re.compile(r'zero|orez|one|eno|two|owt|three|eerht|four|ruof|five|evif|six|xis|seven|neves|eight|thgie|nine|enin|\d', re.IGNORECASE)
    matches = pattern.finditer(text)
    numbers = []
    
    for match in matches:
        word = match.group()
        number = extract_number(word)
        if number is not None:
            numbers.append(number)
    
    return numbers

def extract_number(word):
    """Convert a spelled-out number or digit to an integer."""
    word = word.lower()
    if word in spelled_out_numbers:
        return spelled_out_numbers[word]
    if word.isdigit():
        return int(word)
    return None

def extract_and_combine_numbers(line):
    # Extract numbers from the line
    leftnumbers = extract_numbers_from_text(line)
    rightnumbers = extract_numbers_from_text(line[::-1])
    
    # Take the first left and the first right
    left_number = leftnumbers[0]
    right_number = rightnumbers[0]

    # Combine the two numbers into a single number
    combined_number = int(f"{left_number}{right_number}")

    return combined_number

total_sum = 0
    
with open('input.txt', 'r') as file:
    for line in file:
        combined_number = extract_and_combine_numbers(line.strip())
        print(combined_number)
        total_sum += combined_number

print(f"Total sum of combined numbers: {total_sum}")


