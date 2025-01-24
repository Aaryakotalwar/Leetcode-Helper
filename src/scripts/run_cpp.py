import os
import subprocess
import sys
import tempfile

def parse_input(file_path):
    """
    Parses the input file and extracts variables into a dictionary.
    Handles arrays and other types of inputs like integers or strings.
    """
    with open(file_path, "r") as infile:
        raw_input = infile.read().strip()
    
    inputs = {}
    for part in raw_input.split(","):
        key_value = part.split("=", 1)
        if len(key_value) == 2:
            key, value = key_value[0].strip(), key_value[1].strip()
            # Handle arrays in square brackets
            if value.startswith("[") and value.endswith("]"):
                value = list(map(int, value.strip("[]").split(",")))  # Convert to list of integers
            else:
                try:
                    value = int(value)  # Convert to integer if possible
                except ValueError:
                    value = value.strip('"')  # Otherwise, keep as a string
            inputs[key] = value
    return inputs

def write_temp_input(parsed_input, temp_input_file):
    """
    Writes the parsed input into a temporary file in the required format for the C++ program.
    """
    with open(temp_input_file, "w") as infile:
        for key, value in parsed_input.items():
            if isinstance(value, list):
                infile.write(" ".join(map(str, value)) + "\n")
            else:
                infile.write(str(value) + "\n")

def run_cpp_solution(cpp_executable, temp_input_file, temp_output_file):
    """
    Runs the compiled C++ solution using the temporary input file and captures the output.
    """
    with open(temp_input_file, "r") as infile, open(temp_output_file, "w") as outfile:
        subprocess.run([cpp_executable], stdin=infile, stdout=outfile)

def compare_output(temp_output_file, expected_output_file):
    """
    Compares the output of the C++ solution with the expected output.
    """
    with open(temp_output_file, "r") as outfile, open(expected_output_file, "r") as expected_file:
        actual_output = outfile.read().strip()
        expected_output = expected_file.read().strip()
        return actual_output == expected_output, actual_output, expected_output

def run_test_cases(cpp_executable, testcase_dir):
    """
    Automates running test cases for the C++ solution.
    - cpp_executable: Path to the compiled C++ program.
    - testcase_dir: Directory containing the input and output files.
    """
    # Temporary files for input and output
    temp_input_file = tempfile.mktemp(suffix=".txt")
    temp_output_file = tempfile.mktemp(suffix=".txt")
    
    # print("Running test cases...\n")
    
    # Iterate over test cases in the directory
    for i in range(1, 100):  # Adjust range based on the number of test cases
        input_file = os.path.join(testcase_dir, f"input_{i}.txt")
        output_file = os.path.join(testcase_dir, f"output_{i}.txt")
        
        if not os.path.exists(input_file) or not os.path.exists(output_file):
            break  # Stop when no more test cases are found

        # print(f"Running Test Case {i}...")

        # Step 1: Parse input
        parsed_input = parse_input(input_file)

        # Step 2: Write temporary input file
        write_temp_input(parsed_input, temp_input_file)

        # Step 3: Run C++ solution
        run_cpp_solution(cpp_executable, temp_input_file, temp_output_file)

        # Step 4: Compare outputs
        is_correct, actual_output, expected_output = compare_output(temp_output_file, output_file)
        
        # Display results
        if is_correct:
            print(f"Test Case {i}: PASSED")
        else:
            print(f"Test Case {i}: FAILED")
            print(f"  Expected Output: {expected_output}")
            print(f"  Actual Output: {actual_output}")
            print()
    
    print("Test cases execution completed.")

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 automation_script.py <cpp_executable> <testcase_dir>")
        sys.exit(1)

    cpp_executable = sys.argv[1]
    testcase_dir = sys.argv[2]

    run_test_cases(cpp_executable, testcase_dir)

# import os
# import subprocess
# import sys
# import tempfile

# def parse_input(file_path):
#     """
#     Parses the input file and extracts variables into a dictionary.
#     Handles arrays and other types of inputs like integers or strings.
#     """
#     with open(file_path, "r") as infile:
#         raw_input = infile.read().strip()
    
#     inputs = {}
#     for part in raw_input.split(","):
#         key_value = part.split("=", 1)
#         if len(key_value) == 2:
#             key, value = key_value[0].strip(), key_value[1].strip()
#             # Handle arrays in square brackets
#             if value.startswith("[") and value.endswith("]"):
#                 value = list(map(int, value.strip("[]").split(",")))  # Convert to list of integers
#             else:
#                 try:
#                     value = int(value)  # Convert to integer if possible
#                 except ValueError:
#                     value = value.strip('"')  # Otherwise, keep as a string
#             inputs[key] = value
#     return inputs

# def write_temp_input(parsed_input, temp_input_file):
#     """
#     Writes the parsed input into a temporary file in the required format for the script.
#     """
#     with open(temp_input_file, "w") as infile:
#         for key, value in parsed_input.items():
#             if isinstance(value, list):
#                 infile.write(" ".join(map(str, value)) + "\n")
#             else:
#                 infile.write(str(value) + "\n")

# def run_solution_script(script_path, input_temp, output_temp):
#     """
#     Executes the provided script with the input from a temporary file.
#     """
#     with open(input_temp, "r") as stdin, open(output_temp, "w") as stdout:
#         subprocess.run([sys.executable, script_path], stdin=stdin, stdout=stdout)

# def compare_outputs(generated_output, expected_output):
#     """
#     Compares the output from the solution with the expected output.
#     """
#     with open(generated_output, "r") as gen_out, open(expected_output, "r") as exp_out:
#         actual = gen_out.read().strip()
#         expected = exp_out.read().strip()
#         return actual == expected, actual, expected

# def execute_test_cases(script_path, test_cases_dir):
#     """
#     Runs test cases for the solution script.
#     """
#     temp_input = tempfile.mktemp(suffix=".txt")
#     temp_output = tempfile.mktemp(suffix=".txt")

#     print("Starting test cases execution...")

#     test_number = 1
#     while True:
#         input_file = os.path.join(test_cases_dir, f"input_{test_number}.txt")
#         output_file = os.path.join(test_cases_dir, f"output_{test_number}.txt")

#         if not os.path.exists(input_file) or not os.path.exists(output_file):
#             break

#         print(f"Running Test Case {test_number}...")

#         # Step 1: Parse input
#         parsed_input = parse_input(input_file)

#         # Step 2: Write parsed input to temporary file
#         write_temp_input(parsed_input, temp_input)

#         # Step 3: Run the solution script
#         run_solution_script(script_path, temp_input, temp_output)

#         # Step 4: Compare outputs
#         success, actual, expected = compare_outputs(temp_output, output_file)

#         # Report results
#         if success:
#             print(f"Test Case {test_number}: PASSED")
#         else:
#             print(f"Test Case {test_number}: FAILED")
#             print(f"  Expected: {expected}")
#             print(f"  Actual: {actual}")

#         test_number += 1

#     print("All test cases have been processed.")

# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         print("Usage: python test_runner.py <solution_script_path> <test_cases_directory>")
#         sys.exit(1)

#     solution_script = sys.argv[1]
#     test_cases_directory = sys.argv[2]

#     execute_test_cases(solution_script, test_cases_directory)
