
'''
Emmie Kennemer
3/3/24
'''

def food_input():
    user_input = input()
    tokens = user_input.split()
    
    while True:
        food = tokens[0]
        amount = tokens[1]
        if (food == "quit" and amount == "0"):
            break
        else:
            print_this = ("Eating " + str(tokens[1]) + " " + str(tokens[0] + " a day keeps you happy and healthy."))

        print(print_this)
    
        user_input = input()
        tokens = user_input.split()

        
        

if __name__ == "__main__":
    food_input()
