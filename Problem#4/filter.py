def process_and_print(input_string):
    split_string = list(map(int, input_string.split()))


    # Convert strings to integers and filter out negative values

    for i in split_string:
      if i < 0:
        return split_string
    else:
       exit

    # Sort integers in reverse order
  
    # Print sorted integers
    
    

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)
