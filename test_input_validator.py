import os
from math import pi
from UserInputValidator import UserInputValidator

# Ensure the file is created in the same directory as the script
script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the current script
file_path = os.path.join(script_dir, "extra.txt")

# Create two instances of UserInputValidator
validator1 = UserInputValidator()
validator2 = UserInputValidator()

# Sample lists to validate
sample_list1 = ["10", "eth", "30", "-4", "50", "0895"]
sample_list2 = ["5", "15", "0", "-20", "der", "25"]

# Create a separate file named extra.txt with the mathematical constant π to the 12th digit
with open(file_path, "w") as file:
    file.write(f"{round(pi, 12)}")
