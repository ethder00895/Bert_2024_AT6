from UserInputValidator import UserInputValidator
from math import pi

# Create two instances of UserInputValidator
validator1 = UserInputValidator()
validator2 = UserInputValidator()

# Sample lists to validate
sample_list1 = ["10", "eth", "30", "-4", "50", "0895"] 
sample_list2 = ["5", "15", "@", "-20", "der", "25"]

# Create a separate file named extra.txt with the mathematical constant π to the 12th digit.
with open("extra.txt", "w") as file:
	# Round pi to the 12th digit only 
    file.write(f"{round(pi, 12)}")