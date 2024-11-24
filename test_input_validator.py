import os
from math import pi
from UserInputValidator import UserInputValidator

# Ensure the file is created in the same directory as the script
script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the current script
file_path = os.path.join(script_dir, "extra.txt")

# Create a separate file named extra.txt with the mathematical constant π to the 12th digit
with open(file_path, "w") as file:
    file.write(f"{round(pi, 12)}")
    
# Sample lists to validate
sample_list1 = ["10", "eth", "30", "-4", "50", "0895"]
sample_list2 = ["5", "15", "0", "-20", "der", "25"]


# Add this line as part of Commit 3
if __name__ == "__main__":
	validator1 = UserInputValidator()
	validator2 = UserInputValidator()
	
	# Validate the lists
	valid_set1 = validator1.validate_positive_integers(sample_list1)
	valid_set2 = validator2.validate_positive_integers(sample_list2)
	
	# Print results and message
	validator1.display_message()
	print("Valid Positive Integers from sample_list1:", valid_set1)
	validator2.display_message()
	print("Valid Positive Integers from sample_list2:", valid_set2)