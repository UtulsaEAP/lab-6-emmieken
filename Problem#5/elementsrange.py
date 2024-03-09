def filter_and_print_range(input_list, min_val, max_val):
    #write your code here
    #min_val = int(min_val)
    #max_val = int(max_val)
    
    for num in input_list:
        if min_val <= num <= max_val:
            print(num, end=",")
    

if __name__ == '__main__':
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    integer_list = user_input.split(" ") #[int(a) for a in user_input.split()]
    user_input = input("Enter the min and max values separated by a space: ").split(" ")
    #min_val, max_val = min(user_input), max(user_input)
    min_val = user_input[0]
    max_val = user_input[1]
    filter_and_print_range(integer_list, min_val, max_val)

        #range_input = input("enter range: ")
        #min_val, max_val = min(range_input), max(range_input)
        #Get input for the range (min and max values)
        #call the function to filter and print the numbers in the given range
    
