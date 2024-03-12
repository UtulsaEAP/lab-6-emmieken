'''
Emmie Kennemer
3/6/24
'''

def process_user_contacts(user_input):
    '''
    user_input = input().split(",")
    contacts = {}

    #dictionary = {user_input[i]: user_input[i+1] for i in range(0, len(user_input), 2)}
    for i in user_input:
        split = i.split(",")
        contacts[split[0]] = split[1]
    
    person_name = input()
    print(contacts[person_name])
    
    
    '''
    

    #user_input = input("Enter word pairs (name, phone number): ")
    
    #user_contacts = {user_input}
    #search_name = input("Enter a contact name: ")

    #if search_name == user_input[i]:
        #print(user_input[i+1])


    #user_input = str(input()).split()
   # tokens = input()

    # Put word pairs into a dictionary
   # dictionary = dict(zip(user_input[::2], tokens[1::2]))

    # Get contact name from input, output contact's phone number
    #contact_name = input("Enter the contact name: ")

    user_input = input()
    dictionary = {}
    user_split = user_input.split(" ")

    for pair in user_split:
        name, number = pair.split(",")
        dictionary[name] = number
    
    search_name = input()
    print(dictionary[search_name])



if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")
    # Call the function to process user contacts
    process_user_contacts(user_input)
