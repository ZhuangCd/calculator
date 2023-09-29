import os
import argparse

"""Run: python adder.py --input /path/to/input.txt --output /path/to/output.txt"""

parser = argparse.ArgumentParser(
    description="Add numbers from an input file and write results to an output file."
)

parser.add_argument("--input", type=str, help="Input file path")
parser.add_argument("--output", type=str, help="Output file path")

args = parser.parse_args()

input_txt = args.input
output_txt = args.output


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
            result = number_list[i] + number_list[i + 1]
            results.append(result)
    return results


def floats_to_strings(results):
    string_list = [str(result) for result in results]
    return string_list


def write_results_to_file(output_file, string_list):
    with open(output_file, "w") as file:
        for text in string_list:
            file.write(text + "\n")


if __name__ == "__main__":
    if os.path.exists(input_txt):
        validate_file(input_txt)
        number_list = collect_numbers(input_txt)
        results = add_numbers(number_list)
        string_list = floats_to_strings(results)
        write_results_to_file(output_txt, string_list)
