# import os
# import subprocess
# import sys
# import tempfile

# def write_temp_input(input_file, temp_input_file):
#     """
#     Copies the content of the input file directly into a temporary input file.
#     """
#     with open(input_file, "r") as infile, open(temp_input_file, "w") as temp_infile:
#         temp_infile.write(infile.read())

# def run_python_solution(python_file, temp_input_file, temp_output_file):
#     """
#     Runs the Python solution using the temporary input file and captures the output.
#     """
#     with open(temp_input_file, "r") as infile, open(temp_output_file, "w") as outfile:
#         # subprocess.run(["python3", python_file], stdin=infile, stdout=outfile)
#         subprocess.run(["python", python_file], stdin=infile, stdout=outfile)


# def compare_output(temp_output_file, expected_output_file):
#     """
#     Compares the output of the Python solution with the expected output.
#     """
#     with open(temp_output_file, "r") as outfile, open(expected_output_file, "r") as expected_file:
#         actual_output = outfile.read().strip()
#         expected_output = expected_file.read().strip()
#         return actual_output == expected_output, actual_output, expected_output

# def run_test_cases(python_file, testcase_dir):
#     """
#     Automates running test cases for the Python solution.
#     - python_file: Path to the Python program.
#     - testcase_dir: Directory containing the input and output files.
#     """
#     # Use tempfile to create platform-independent temporary files
#     temp_input_file = tempfile.mktemp(suffix=".txt")
#     temp_output_file = tempfile.mktemp(suffix=".txt")
#     print("running test cases")
#     i = 1
#     while True:
#         input_file = os.path.join(testcase_dir, f"input_{i}.txt")
#         output_file = os.path.join(testcase_dir, f"output_{i}.txt")
        
#         if not os.path.exists(input_file) or not os.path.exists(output_file):
#             break  # Stop if files are not found

#         # Step 1: Write temporary input file
#         write_temp_input(input_file, temp_input_file)

#         # Step 2: Run Python solution
#         run_python_solution(python_file, temp_input_file, temp_output_file)

#         # Step 3: Compare outputs
#         is_correct, actual_output, expected_output = compare_output(temp_output_file, output_file)
        
#         # Display results
#         if is_correct:
#             print(f"Test Case {i}: PASSED")
#         else:
#             print(f"Test Case {i}: FAILED")
#             print(f"  Expected Output: {expected_output}")
#             print(f"  Actual Output: {actual_output}")
#             print()
        
#         i += 1
    
#     print("Test cases execution completed.")

# # Example usage
# if __name__ == "__main__":
#     # print("Script started.")
#     # print("Arguments received:", sys.argv)
#     if len(sys.argv) != 3:
#         # print("Error: Incorrect number of arguments.")
#         # print("Usage: python run_python.py <solution_file_path> <test_case_directory>")
#         sys.exit(1)
#         # print("Arguments are valid.")

#     python_file = sys.argv[1]
#     testcase_dir = sys.argv[2]
#     # print(python_file)
#     # print(testcase_dir)

#     run_test_cases(python_file, testcase_dir)

import os
import subprocess
import sys
import tempfile

def copy_to_tempfile(src_file, dest_file):
    """
    Copies content from the source file to a temporary destination file.
    """
    with open(src_file, "r") as src, open(dest_file, "w") as dest:
        dest.write(src.read())

def execute_python_script(script_path, temp_input, temp_output):
    """
    Executes the provided Python script with temporary input and captures the output.
    """
    with open(temp_input, "r") as input_stream, open(temp_output, "w") as output_stream:
        subprocess.run([sys.executable, script_path], stdin=input_stream, stdout=output_stream)

def validate_output(generated_output, reference_output):
    """
    Compares the generated output against the reference output.
    """
    with open(generated_output, "r") as gen_out, open(reference_output, "r") as ref_out:
        actual = gen_out.read().strip()
        expected = ref_out.read().strip()
        return actual == expected, actual, expected

def process_test_cases(solution_script, test_dir):
    """
    Executes test cases for the given solution script.
    - solution_script: Path to the Python solution.
    - test_dir: Directory containing test case files.
    """
    temp_input = tempfile.mktemp(suffix=".txt")
    temp_output = tempfile.mktemp(suffix=".txt")
    print("Executing test cases...")

    test_index = 1
    while True:
        input_path = os.path.join(test_dir, f"input_{test_index}.txt")
        output_path = os.path.join(test_dir, f"output_{test_index}.txt")

        if not os.path.exists(input_path) or not os.path.exists(output_path):
            break

        # Step 1: Prepare temporary input file
        copy_to_tempfile(input_path, temp_input)

        # Step 2: Execute the solution script
        execute_python_script(solution_script, temp_input, temp_output)

        # Step 3: Validate output
        passed, actual, expected = validate_output(temp_output, output_path)

        # Log test case results
        if passed:
            print(f"Test Case {test_index}: PASSED")
        else:
            print(f"Test Case {test_index}: FAILED")
            print(f"  Expected: {expected}")
            print(f"  Actual: {actual}")

        test_index += 1

    print("All test cases have been processed.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python test_runner.py <solution_script_path> <test_cases_directory>")
        sys.exit(1)

    solution_script_path = sys.argv[1]
    test_cases_directory = sys.argv[2]

    process_test_cases(solution_script_path, test_cases_directory)

