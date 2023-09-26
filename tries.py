import os
# Comments DO lie!
# You did not add much extra info with your docstrings, so they are crap.
# You repeate yourself. Don't do that. You can skip on docstring if you do not have anything to add.
def read_number_pairs(input_file):  
    """Reads number pairs from a file and returns them as a list."""
    # TODO: Check if file exists, if not exit program.
    # TODO: Check if file is readable, if not exit program
    with open(input_file, 'r') as file:
        lines = file.readlines() # Kinda ok, but you need to understand the bottleneck introduced by "readlines()". Whaaat CAN be a problem here?

    # TDOD: Separate this into 2 functions.
    # One function should do 1 thing. You are reading and making an assumption what your data is like. 
    # Even if you do not check your data. This should be separated into 2 function and logged in the design document that
    # it is an assumption that you dont need to check input.  
    number_pairs = []
    for line in lines:
        num1, num2 = map(int, line.strip().split())
        number_pairs.append((num1, num2))
    
    return number_pairs

def calculate_and_print_results(number_pairs):
    """Calculates the sum of number pairs and prints them."""
    # TODO: Make this a oneliner key terms: List comprehension, map, reduce.
    results = []
    for num1, num2 in number_pairs:
        result = num1 + num2
        results.append(result)
        print(result) # No print pls! only return!!!!

def write_results_to_file(output_file, results):
    """Writes results to an output file."""
    with open(output_file, 'w') as file:
        for result in results:
            file.write(str(result) + '\n')

if __name__ == "__main__":
    input_txt = '/home/lapos-erdo/Desktop/calculator/numbers.txt' #TODO: Never ever hardcode a path in your code!
    output_txt = '/home/lapos-erdo/Desktop/calculator/results.txt' 
    #TODO: Especially not in the middle of your code. 
    # If you really have to do that hard code it at the top of the file as static variable
    # Bit better: Make a config file and hardcode there
    # Even better make a default in a config file and add the option to dinamically overwrite at start by the user who runs the program with a flag like
    # python ./adder.py --input "/whatever/mypath/input.txt" --output "/whatever/mypath/outpot.txt"
    if os.path.exists(input_txt):
        number_pairs = read_number_pairs(input_txt)
        calculate_and_print_results(number_pairs)
        write_results_to_file(output_txt, number_pairs)
    else:
        print(f"Input file '{input_txt}' not found.") #TODO: Implement a logger around this. DO NOT USE print!
