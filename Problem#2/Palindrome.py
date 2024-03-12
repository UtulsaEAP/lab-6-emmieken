'''
Emmie Kennemer
3/3/24
'''



def check_palindrome(user_input):
    
    stripped_user_input = user_input.replace(" ", "")
    if stripped_user_input == stripped_user_input[::-1]:
        print("palindrome: " + user_input)
    else:
        print("not a palindrome: " + user_input)
    return 
    
if __name__ == "__main__":
    user_input = input()
    
    check_palindrome(user_input)
    
