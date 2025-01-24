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
