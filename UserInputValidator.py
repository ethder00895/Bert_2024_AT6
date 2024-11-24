# New Python object class to be created
class UserInputValidator:
    
    def validate_positive_integers(self, string_list):
        ''' 
        Checks for the list that contains positive integers,
        Appends to the list and returns the integers collected.
            parameter [string_list] - string lists
        '''
        valid_positive_integers = []
        for item in string_list:
            if item.isdigit() and int(item) > 0:
                valid_positive_integers.append(int(item))
                
        return valid_positive_integers
    
    # Commit 1 - to be added
    def display_message(self):
        print("The list has been validated.")