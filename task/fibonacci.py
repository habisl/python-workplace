# -----------------------------------------------------------
# Python script to print first n Fibonacci numbers 
# and save the output to a file in the same folder
# -----------------------------------------------------------

def fibonacchi_function():
    """
    Function to return fibonacchi series with given input
    """
    valid_input = False
    # check if the number of terms is valid
    while not valid_input:
        try:
            num = int(input('How many Fibonacci numbers should be printed out in the sequence: '))
            if num > 0:
                valid_input = True
            else:
                print("That's not a positive number. Try again: ")
        except ValueError:
            print("That's not an integer. Try again: ")
                 
    # Initializing the starting numbers
    a,b = 0,1

    # Open the file to add the output
    with open("fib.txt", "a") as output_file:
        output_file.write('Febonacci series for input: ' + str(num) + '\n')
        for _ in range(num):
            print(a)
            output_file.write(str(a) + '\n')
            # apply the logic and calculate the value
            a,b = b, a+b
            
if __name__ == '__main__':
    fibonacchi_function()
