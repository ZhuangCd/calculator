import os

input_txt = "/home/lapos-erdo/Desktop/calculator/numbers.txt"
output_txt = "/home/lapos-erdo/Desktop/calculator/results.txt"


def read_number_pairs(input_file):
    if not (os.path.exists(input_file) or not os.access(input_file, os.R_OK)):
        exit(1)
    with open(input_file, "r") as file:
        lines = file.readlines()

    number_pairs = []
    for line in lines:
        num1, num2 = map(float, line.strip().split())
        number_pairs.append((num1, num2))

    return number_pairs


def calculate_and_print_results(number_pairs):
    results = []
    for num1, num2 in number_pairs:
        result = num1 + num2
        results.append(result)

    return results


def write_results_to_file(output_file, results):
    with open(output_file, "w") as file:
        for result in results:
            file.write(str(result) + "\n")


if __name__ == "__main__":
    if os.path.exists(input_txt):
        number_pairs = read_number_pairs(input_txt)
        results = calculate_and_print_results(number_pairs)
        write_results_to_file(output_txt, results)
