def process_user_contacts(user_input):
    user_contacts = ""

    user_input = input().split()
    tokens = input()

    # Put word pairs into a dictionary
    dictionary = dict(zip(user_input[::2], tokens[1::2]))

    # Get contact name from input, output contact's phone number
    contact_name = input("Enter the contact name: ")
    return dictionary 
    
   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts

    process_user_contacts(user_input)
