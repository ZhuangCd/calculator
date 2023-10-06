"""
- For default config.yaml run
    python3 calculator.py
- For different path, run
    python adder.py --input /path/to/input.txt --output /path/to/output.txt
        like:
    python3 calculator.py --input numbers.txt --output results.txt
"""

import os
import argparse
import yaml
import logging


logger = logging.getLogger(__name__)

config_file_path = os.path.join(os.path.dirname(__file__), "config.yaml")

with open(config_file_path, "r") as file:
    cfg = yaml.safe_load(file)


def validate_file(input_file):
    if not (os.path.exists(input_file) and os.access(input_file, os.R_OK)):
        raise FileNotFoundError(
            f"Input file '{input_file}' does not exist or is not readable."
        )
    return True


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
    string_list = [str(float) for float in results]
    return string_list


def write_results_to_file(output_file, string_list):
    with open(output_file, "w") as file:
        for text in string_list:
            file.write(text + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, help="Input file path")
    parser.add_argument("--output", type=str, help="Output file path")
    args = parser.parse_args()

    input_file = args.input or cfg.get("input")
    output_file = args.output or cfg.get("output")

    if os.path.exists(input_file):
        validate_file(input_file)
        number_list = collect_numbers(input_file)
        results = add_numbers(number_list)
        string_list = floats_to_strings(results)
        write_results_to_file(output_file, string_list)
