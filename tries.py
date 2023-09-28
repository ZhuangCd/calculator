import os

input_file = "/home/lapos-erdo/Desktop/calculator/numbers.txt"
output_file = "/home/lapos-erdo/Desktop/calculator/results.txt"

def validate_file(input_file):
    if not (os.path.exists(input_file) and os.access(input_file, os.R_OK)):
        print(f"Input file '{input_file}' does not exist or is not readable.")
        exit(1)

def write_results_to_file(output_file, results):
    try:
        with open(output_file, "w") as file:
            for number in results:
                formatted_number = "{:.1f}".format(number)
                file.write(f"{formatted_number}\n")
    except Exception as e:
        print(f"An error occurred while writing to '{output_file}': {e}")

if __name__ == "__main__":
    if os.path.exists(input_file):
        validate_file(input_file)
        number_list = collect_numbers(input_file)
        results = add_numbers(number_list)
        write_results_to_file(output_file, results)
