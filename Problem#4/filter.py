def process_and_print(input_string):
    #input_string = input("Enter a space-separated string of numbers: ")
    split_string = list(map(int, input_string.split()))

    new_list = []
    # Convert strings to integers and filter out negative values

    for i in split_string:
        if int(i) < 0:
          new_list.append(int(i))
        new_list.sort(reverse=True)
    # Sort integers in reverse order

    for i in new_list:
      print(i, end=' ')

    # Print sorted integers
    
    
if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")
    # Call the function to process and print the result
    process_and_print(user_input)
