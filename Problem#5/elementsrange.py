def filter_and_print_range(input_list, min_val, max_val):
    #write your code here
#    user_input = input("Enter a space-separated string of numbers: ")
#    tokens = user_input.split()
 #   input_list = list(tokens)
  #  range_input = input("enter range: ")
   # min_val = min(range_input)
    #max_val = max(range_input)

    for i in input_list:
        if int(i) > int(min_val) and int(i) < int(max_val):
                print(i)
        else:
            exit

if __name__ == '__main__':
        # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    integer_list = [int(a) for a in user_input.split()]
    user_input = input("Enter the min and max values separated by a space: ")
    min_val, max_val = min(user_input), max(user_input)
    filter_and_print_range(integer_list, min_val, max_val)

        # #range_input = input("enter range: ")
        #min_val, max_val = min(range_input), max(range_input)

        # Get input for the range (min and max values)
        # call the function to filter and print the numbers in the given range
    
