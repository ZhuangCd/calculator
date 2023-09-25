import os

def read_number_pairs(input_file):
    """Reads number pairs from a file and returns them as a list."""
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    number_pairs = []
    for line in lines:
        num1, num2 = map(int, line.strip().split())
        number_pairs.append((num1, num2))
    
    return number_pairs

def calculate_and_print_results(number_pairs):
    """Calculates the sum of number pairs and prints them."""
    results = []
    for num1, num2 in number_pairs:
        result = num1 + num2
        results.append(result)
        print(result)

def write_results_to_file(output_file, results):
    """Writes results to an output file."""
    with open(output_file, 'w') as file:
        for result in results:
            file.write(str(result) + '\n')

if __name__ == "__main__":
    input_txt = '/home/lapos-erdo/Desktop/calculator/numbers.txt'
    output_txt = '/home/lapos-erdo/Desktop/calculator/results.txt'

    if os.path.exists(input_txt):
        number_pairs = read_number_pairs(input_txt)
        calculate_and_print_results(number_pairs)
        write_results_to_file(output_txt, number_pairs)
    else:
        print(f"Input file '{input_txt}' not found.")
