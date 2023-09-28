import os

input_file = "/home/lapos-erdo/Desktop/calculator/numbers.txt"
output_file = "/home/lapos-erdo/Desktop/calculator/results.txt"


def validate_file(input_file):
    if not (os.path.exists(input_file) and os.access(input_file, os.R_OK)):
        exit(1)


def collect_numbers(input_file):
    number_list = []
    with open(input_file, "r") as file:
        for line in file:
            line_numbers = list(map(float, line.strip().split()))
            number_list.extend(line_numbers)
    return number_list


def add_numbers(number_list):
    results = []
    for i in range(0, len(number_list), 2):
        if i + 1 < len(number_list):
            result = number_list[i] + number_list[i+1]
            results.append(result)
    return results


def write_results_to_file(output_file, results):
    with open(output_file, 'w') as file:
        for result in results:
            file.write(str(result) + '\n')


if __name__ == "__main__":
    if os.path.exists(input_file):
        validate_file(input_file)
        number_list = collect_numbers(input_file)
        results = add_numbers(number_list)
        write_results_to_file(output_file, results) 