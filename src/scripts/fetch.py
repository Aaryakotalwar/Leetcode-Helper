# import re
# import requests
# import json
# import argparse
# from bs4 import BeautifulSoup
# import os
# import shutil

# # Base URL for LeetCode GraphQL API
# base_url = "https://leetcode.com/graphql"

# # GraphQL queries
# problem_details_query = """
# query getProblem($titleSlug: String!) {
#   question(titleSlug: $titleSlug) {
#     questionId
#     title
#     content
#     difficulty
#   }
# }
# """
# code_snippets_query = """
# query questionHints($titleSlug: String!) {
#     question(titleSlug: $titleSlug) {
#         title
#         codeSnippets {
#             lang
#             langSlug
#             code
#         }
#     }
# }
# """
# # Parse the problem slug from command-line arguments
# parser = argparse.ArgumentParser()
# parser.add_argument("--titleSlug", required=True, help="Slug of the problem title")
# args = parser.parse_args()

# variables = {"titleSlug": args.titleSlug}

# # Define request headers
# headers = {"Content-Type": "application/json"}
# # Function to fetch data from LeetCode GraphQL API
# def fetch_data(query, variables):
#     response = requests.post(base_url, json={"query": query, "variables": variables}, headers=headers)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         raise Exception(f"Error: HTTP {response.status_code}, {response.text}")

# # Function to extract data structures from C++ and Python3 code snippets
# def extract_data_structure(code, lang):
#     """
#     Extract data structure types from code snippets (C++/Python3).
#     """
#     data_structure = {}
#     if lang == 'C++':
#         pattern = r'\((.*?)\)'
#         match = re.search(pattern, code)
#         if match:
#             params = match.group(1)
#             # Split by comma to separate multiple variables
#             variables = params.split(',')
#             for var in variables:
#                 var = var.strip()
#                 if var:
#                     # Extract type and variable name
#                     type_and_name = var.split()
#                     if len(type_and_name) >= 2:
#                         var_type = type_and_name[0]
#                         var_name = type_and_name[1]
#                         data_structure[var_name] = var_type

#         # Extract the return type (just after public/private)
#         return_type_pattern = r'public:\s*(\w+)'
#         return_type_match = re.search(return_type_pattern, code)
#         if return_type_match:
#             return_type = return_type_match.group(1)
#             data_structure['return'] = return_type

#         # print(f"Extracted C++ data structures: {data_structure}")

#     # Extracting Python3 variable types from function signature
#     elif lang == 'Python3':
#         # Extract the function signature between the parentheses
#         pattern = r'\((.*?)\)'
#         match = re.search(pattern, code)
#         if match:
#             params = match.group(1)
#             # Split by comma to separate multiple variables
#             variables = params.split(',')
#             for var in variables:
#                 var = var.strip()
#                 if var and "self" not in var:  # Skip the 'self' parameter
#                     # Extract type and variable name
#                     type_and_name = var.split(":")
#                     if len(type_and_name) == 2:
#                         var_name = type_and_name[0].strip()
#                         var_type = type_and_name[1].strip()
#                         data_structure[var_name] = f"{var_type} (Python3)"

#         # Extract the return type (after -> symbol)
#         return_type_pattern = r'->\s*(\w+)'
#         return_type_match = re.search(return_type_pattern, code)
#         if return_type_match:
#             return_type = return_type_match.group(1)
#             data_structure['return'] = f"{return_type} (Python3)"

#         # print(f"Extracted Python3 data structures: {data_structure}")

#     return data_structure
# # Fetch problem details and code snippets
# problem_data = fetch_data(problem_details_query, variables)
# code_snippet_data = fetch_data(code_snippets_query, variables)

# # Extract and process problem details
# output = {}
# question = problem_data.get("data", {}).get("question", {})
# if question:
#     question_id = question.get("questionId")
#     title = question.get("title")
#     content_html = question.get("content", "")
#     difficulty = question.get("difficulty")

#     # Parse and clean HTML content
#     soup = BeautifulSoup(content_html, "html.parser")
#     examples = {}
#     description_parts = []
#     example_counter = 1

#     # Extract examples
#     for example_tag in soup.find_all("pre"):
#         example_text = example_tag.get_text()

#         # Remove the explanation text if it exists
#         if "Explanation:" in example_text:
#             example_text = example_text.split("Explanation:", 1)[0].strip()

#         examples[f"Example {example_counter}"] = example_text
#         example_counter += 1

#     # Extract description (everything before the examples)
#     for element in soup.find_all(["p", "strong"], recursive=False):
#         if element.name == "pre":
#             break
#         description_parts.append(element.get_text(strip=True))

#     # Join description paragraphs
#     description_clean = " ".join(description_parts)

#     # Process code snippets
#     code_snippets = {}
#     snippet_question = code_snippet_data.get("data", {}).get("question", {})
#     data_structures = {}
#     if snippet_question:
#         for snippet in snippet_question.get("codeSnippets", []):
#             lang = snippet.get("lang")
#             code = snippet.get("code")
#             code_snippets[lang] = code
#             if lang in ["C++", "Python3"]:
#                 data_structures[lang] = extract_data_structure(code, lang)

#     # Prepare test case directory
#     testcase_dir = "C:\\Users\\Arya\\OneDrive\\Desktop\\clone\\leetcode\\src\\testcases"
#     if os.path.exists(testcase_dir):
#         shutil.rmtree(testcase_dir)
#     os.makedirs(testcase_dir, exist_ok=True)

#     # Save examples to test case files
#     input_counter = 1
#     for example_key, example_text in examples.items():
#         parts = example_text.split("Output:", 1)
#         if len(parts) == 2:
#             # Process input
#             input_text = parts[0].replace("Input:", "").strip()

#             # Convert input format
#             input_lines = input_text.split(", ")
#             formatted_input = []
#             for line in input_lines:
#                 line = line.replace('"', '')  # Replace double quotes with space

#                 # Check if the line contains an array and format it
#                 if "[" in line and "]" in line:  
#                     line = line.split("=")[1].strip()  # Get the value after the "="
#                     line = line.replace("[", "").replace("]", "")  # Remove square brackets
#                     line = line.replace(",", " ")  # Replace commas with spaces
#                     vector_size = len(line.split())  # Calculate the size of the vector
#                 else:
#                     # Get the value after "=" for other types
#                     line = line.split("=")[1].strip()
#                 formatted_input.append(line.strip())

#             # Prepend the vector size as the first line of the output
#             formatted_input.insert(0, str(vector_size))

#             # Join the formatted input lines into a single output
#             input_text = "\n".join(formatted_input)

#             # Process output
#             output_text = parts[1].strip().split("Explanation:", 1)[0].strip()
#             output_text = output_text.replace('"', '')

#             if "[" in output_text and "]" in output_text:  # Replace arrays
#                 # Remove the brackets entirely and replace commas with spaces
#                 output_text = output_text.replace("[", "").replace("]", "").replace(",", " ").strip()

#             if "C++" in data_structures:
#                 # first_key = next(iterator)  # Get the first key
#                 # value_of = data_structures["C++"][first_key]  # Access the value using the key
#                 output_text = output_text   # Append semicolon
#             print(output_text)
#             print(input_text)
#             # File paths
#             input_file = os.path.join(testcase_dir, f"input_{input_counter}.txt")
#             output_file = os.path.join(testcase_dir, f"output_{input_counter}.txt")

#             # Write input and output to files
#             with open(input_file, "w") as infile:
#                 infile.write(input_text)
#             with open(output_file, "w") as outfile:
#                 outfile.write(output_text)

#             input_counter += 1


#     # Prepare output dictionary
#     output = {
#         "id": question_id,
#         "title": title,
#         "description": description_clean.strip(),
#         "difficulty": difficulty,
#         "examples": examples,
#         "codeSnippets": code_snippets,
#         "dataStructures": data_structures,
#     }
# else:
#     output = {"error": "No question data found."}

# # Print JSON output
# print(json.dumps(output, indent=2))
# import re
# import requests
# import json
# import argparse
# from bs4 import BeautifulSoup
# import os
# import shutil

# # Base URL for LeetCode GraphQL API
# base_url = "https://leetcode.com/graphql"

# # GraphQL queries
# problem_details_query = """
# query getProblem($titleSlug: String!) {
#   question(titleSlug: $titleSlug) {
#     questionId
#     title
#     content
#     difficulty
#   }
# }
# """

# code_snippets_query = """
# query questionHints($titleSlug: String!) {
#     question(titleSlug: $titleSlug) {
#         title
#         codeSnippets {
#             lang
#             langSlug
#             code
#         }
#     }
# }
# """

# # Parse the problem slug from command-line arguments
# parser = argparse.ArgumentParser()
# parser.add_argument("--titleSlug", required=True, help="Slug of the problem title")
# args = parser.parse_args()

# variables = {"titleSlug": args.titleSlug}

# # Define request headers
# headers = {"Content-Type": "application/json"}

# # Function to fetch data from LeetCode GraphQL API
# def fetch_data(query, variables):
#     response = requests.post(base_url, json={"query": query, "variables": variables}, headers=headers)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         raise Exception(f"Error: HTTP {response.status_code}, {response.text}")

# # Function to save code snippets to files
# def save_code_snippets_to_files(output, testcase_dir):
#     if "codeSnippets" not in output:
#         raise KeyError("The key 'codeSnippets' is missing in the output dictionary.")

#     for lang, code in output["codeSnippets"].items():
#         if lang == "C++":
#             boilerplate = """
# #include <bits/stdc++.h>
# using namespace std;

# typedef long long ll;

# void solve() {
#     // Write your solution here
# }

# int main() {
#     ios_base::sync_with_stdio(false); cin.tie(nullptr);
#     ll t = 1;
#     cin >> t;
#     while (t--) {
#         solve();
#     }
#     return 0;
# }
# """
#             code = f"{boilerplate.strip()}\n\n{code.strip()}"

#         snippet_file_path = os.path.join(testcase_dir, f"{lang.lower()}.cpp")
#         with open(snippet_file_path, "w") as snippet_file:
#             snippet_file.write(code)

# # Main logic
# problem_data = fetch_data(problem_details_query, variables)
# code_snippet_data = fetch_data(code_snippets_query, variables)

# # Extract and process problem details
# output = {}
# question = problem_data.get("data", {}).get("question", {})
# if question:
#     question_id = question.get("questionId")
#     title = question.get("title")
#     content_html = question.get("content", "")
#     difficulty = question.get("difficulty")

#     # Parse and clean HTML content
#     soup = BeautifulSoup(content_html, "html.parser")
#     examples = {}
#     description_parts = []
#     example_counter = 1

#     # Extract examples
#     for example_tag in soup.find_all("pre"):
#         example_text = example_tag.get_text()
#         examples[f"Example {example_counter}"] = example_text
#         example_counter += 1

#     # Extract description
#     for element in soup.find_all(["p", "strong"], recursive=False):
#         description_parts.append(element.get_text(strip=True))
#     description_clean = " ".join(description_parts)

#     # Process code snippets
#     code_snippets = {}
#     snippet_question = code_snippet_data.get("data", {}).get("question", {})
#     if snippet_question:
#         for snippet in snippet_question.get("codeSnippets", []):
#             lang = snippet.get("lang")
#             code = snippet.get("code")
#             code_snippets[lang] = code

#     # Prepare test case directory
#     testcase_dir = "testcases"
#     if os.path.exists(testcase_dir):
#         shutil.rmtree(testcase_dir)
#     os.makedirs(testcase_dir, exist_ok=True)

#     # Save examples to test case files
#     for idx, (example_key, example_text) in enumerate(examples.items(), start=1):
#         parts = example_text.split("Output:")
#         if len(parts) == 2:
#             input_text = parts[0].replace("Input:", "").strip()
#             output_text = parts[1].strip().split("Explanation:", 1)[0].strip()

#             input_file = os.path.join(testcase_dir, f"input_{idx}.txt")
#             output_file = os.path.join(testcase_dir, f"output_{idx}.txt")

#             with open(input_file, "w") as infile:
#                 infile.write(input_text)
#             with open(output_file, "w") as outfile:
#                 outfile.write(output_text)

#     # Save code snippets to files
#     save_code_snippets_to_files({"codeSnippets": code_snippets}, testcase_dir)

#     # Prepare output dictionary
#     output = {
#         "id": question_id,
#         "title": title,
#         "description": description_clean.strip(),
#         "difficulty": difficulty,
#         "examples": examples,
#         "codeSnippets": code_snippets,
#     }
# else:
#     output = {"error": "No question data found."}

# # Print JSON output
# print(json.dumps(output, indent=2))



import re
import requests
import json
import argparse
from bs4 import BeautifulSoup
import os
import shutil

# Base URL for LeetCode GraphQL API
BASE_URL = "https://leetcode.com/graphql"

# GraphQL queries
PROBLEM_DETAILS_QUERY = """
query getProblem($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    title
    content
    difficulty
  }
}
"""
CODE_SNIPPETS_QUERY = """
query questionHints($titleSlug: String!) {
    question(titleSlug: $titleSlug) {
        title
        codeSnippets {
            lang
            langSlug
            code
        }
    }
}
"""

# Parse the problem slug from command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--titleSlug", required=True, help="Slug of the problem title")
args = parser.parse_args()

# Request headers
HEADERS = {"Content-Type": "application/json"}

# Fetch data from LeetCode GraphQL API
def fetch_data(query, variables):
    response = requests.post(BASE_URL, json={"query": query, "variables": variables}, headers=HEADERS)
    response.raise_for_status()
    return response.json()

# Extract data structures from code snippets
def extract_data_structure(code, lang):
    data_structure = {}
    if lang == "C++":
        param_pattern = r"\((.*?)\)"
        param_match = re.search(param_pattern, code)
        if param_match:
            params = param_match.group(1).split(',')
            for param in params:
                tokens = param.strip().split()
                if len(tokens) >= 2:
                    data_structure[tokens[1]] = tokens[0]
        return_type_match = re.search(r"public:\s*(\w+)", code)
        if return_type_match:
            data_structure["return"] = return_type_match.group(1)

    elif lang == "Python3":
        param_pattern = r"\((.*?)\)"
        param_match = re.search(param_pattern, code)
        if param_match:
            params = param_match.group(1).split(',')
            for param in params:
                if "self" not in param:
                    tokens = param.strip().split(":")
                    if len(tokens) == 2:
                        data_structure[tokens[0].strip()] = f"{tokens[1].strip()} (Python3)"
        return_type_match = re.search(r"->\s*(\w+)", code)
        if return_type_match:
            data_structure["return"] = f"{return_type_match.group(1)} (Python3)"

    return data_structure

# Process and save test cases
def save_test_cases(testcase_dir, examples, data_structures):
    os.makedirs(testcase_dir, exist_ok=True)
    for idx, (example_key, example_text) in enumerate(examples.items(), start=1):
        parts = example_text.split("Output:", 1)
        if len(parts) != 2:
            continue

        input_text = parts[0].replace("Input:", "").strip()
        output_text = parts[1].strip().split("Explanation:", 1)[0].strip()

        input_text = format_input(input_text)
        output_text = format_output(output_text, data_structures)

        input_file = os.path.join(testcase_dir, f"input_{idx}.txt")
        output_file = os.path.join(testcase_dir, f"output_{idx}.txt")

        with open(input_file, "w") as infile:
            infile.write(input_text)
        with open(output_file, "w") as outfile:
            outfile.write(output_text)

# Format input string
def format_input(input_text):
    formatted = []
    for line in input_text.split(", "):
        line = line.split("=")[-1].strip()
        if "[" in line and "]" in line:
            line = line.strip("[]").replace(",", " ")
        formatted.append(line)
    return "\n".join(formatted)

# Format output string
def format_output(output_text, data_structures):
    if "[" in output_text and "]" in output_text:
        output_text = output_text.strip("[]").replace(",", " ")
    return output_text

# Main script
def main():
    variables = {"titleSlug": args.titleSlug}
    problem_data = fetch_data(PROBLEM_DETAILS_QUERY, variables)
    code_snippet_data = fetch_data(CODE_SNIPPETS_QUERY, variables)

    question = problem_data.get("data", {}).get("question", {})
    if not question:
        print(json.dumps({"error": "No question data found."}, indent=2))
        return

    examples = {}
    description_parts = []
    soup = BeautifulSoup(question.get("content", ""), "html.parser")

    for example_tag in soup.find_all("pre"):
        example_text = example_tag.get_text().split("Explanation:", 1)[0].strip()
        examples[f"Example {len(examples) + 1}"] = example_text

    for element in soup.find_all(["p", "strong"], recursive=False):
        if element.name == "pre":
            break
        description_parts.append(element.get_text(strip=True))

    code_snippets = {}
    data_structures = {}
    for snippet in code_snippet_data.get("data", {}).get("question", {}).get("codeSnippets", []):
        lang = snippet.get("lang")
        code = snippet.get("code")
        code_snippets[lang] = code
        if lang in ["C++", "Python3"]:
            data_structures[lang] = extract_data_structure(code, lang)

    testcase_dir = "C:\\Users\\Arya\\OneDrive\\Desktop\\clone\\leetcode\\src\\testcases"
    if os.path.exists(testcase_dir):
        shutil.rmtree(testcase_dir)

    save_test_cases(testcase_dir, examples, data_structures)

    output = {
        "id": question.get("questionId"),
        "title": question.get("title"),
        "description": " ".join(description_parts).strip(),
        "difficulty": question.get("difficulty"),
        "examples": examples,
        "codeSnippets": code_snippets,
        "dataStructures": data_structures,
    }
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
