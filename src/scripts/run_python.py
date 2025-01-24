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

