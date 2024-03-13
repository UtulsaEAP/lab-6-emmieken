
'''
Emmie Kennemer
3/5/24
'''


def filter_and_print_range(input_list, min_val, max_val):
    #write your code here
    for i in input_list:
        if min_val <= i <= max_val:
            print(i, end=",")
    

if __name__ == '__main__':
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    sort_list = [int(a) for a in user_input.split()]
    user_input = input("Enter the min and max values separated by a space: ")
    #min_val, max_val = min(user_input), max(user_input)
    
    min_val, max_val = map(int, user_input.split())
    filter_and_print_range(sort_list, min_val, max_val)

        #range_input = input("enter range: ")
        #min_val, max_val = min(range_input), max(range_input)
        #Get input for the range (min and max values)
        #call the function to filter and print the numbers in the given range
    
