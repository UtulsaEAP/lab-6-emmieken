def food_input():
    user_input = input()
    tokens = user_input.split()
    
    while user_input != "quit":
        if user_input == "quit" and tokens[1] == tokens[1]:
            print()
        else:
            exit
            #user_input = input()
            #tokens = user_input.split()

        print("Eating " + str(tokens[1]) + " " + str(tokens[0] + " a day keeps you happy and healthy."))
        
        

if __name__ == "__main__":
    food_input()
