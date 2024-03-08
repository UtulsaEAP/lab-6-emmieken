def filter_and_print_range(input_list, min_val, max_val):
    #write your code here
        user_input = input("Enter a space-separated string of numbers: ")
        input_list = list(user_input)
        range_input = input("enter range: ")
        min_val = min(range_input)
        max_val = max(range_input)

        for i in input_list:
            if i > min_val:
                if i < max_val:
                    print(i)
            else:
                exit
        return

if __name__ == '__main__':
        # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    input_list = list(user_input)
    range_input = input("enter range: ")
    min_val, max_val = min(range_input), max(range_input)

        #for i in input_list:
         #   if i > min_val:
          #      if i < max_val:
           #         print(i)
          #  else:
           #     exit

    filter_and_print_range(input_list, min_val, max_val)


        # Get input for the range (min and max values)
        #user_input = input("Enter the min and max values separated by a space: ")
        #min_val, max_val = min(user_input), max(user_input)

        # Call the function to filter and print the numbers in the given range
    
