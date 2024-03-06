def process_input(input_string):
    numbers = list(map(float, input_string.split()))
    average_value = sum(numbers) / len(numbers)

    # Get max and average
    max_value = max(numbers) 
    #sum_value = sum(numbers)
    #average_value = sum_value / len(numbers)

    return max_value, average_value

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function and get the results
    max_value, average_value = process_input(user_input)

    print(f'Max Value: {max_value:.2f}')
    print(f'Average Value: {average_value:.2f}')
