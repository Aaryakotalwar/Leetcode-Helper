# LeetCode Extension

LeetCode  extension allows you to fetch test cases for LeetCode problems and execute your solutions in C++ or Python without leaving VS Code.

## Features
- **Fetch Test Cases**: Get testcases by using the command "CPH: Fetch Test Cases"
- **Run Solutions**: Run testcases using the command "CPH: Run Test Cases"
- You will get result poped up in vs code.
  
## Installation
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Aaryakotalwar/leetcode-Helper.git
    ```

2. **Install Dependencies**:
    Navigate to the extension's directory and install the required Node.js packages:
    ```bash
    cd leetcode
    npm install
    ```

3. **Open in VS Code**:
    Open the extension folder in Visual Studio Code:
    ```bash
    code .
    ```

4. **Build the Extension**:
    Compile the extension by running:
    ```bash
    npm run compile
    ```

5. **Launch the Extension**:
    Press `F5` to open a new VS Code window with the extension loaded.

## Usage
1. **Activate the Command**:
    Press `Ctrl+Shift+P` to open the command palette, type `CPH: Fetch Test Cases`, and press Enter.

2. **Enter the Title**:
    Input the LeetCode problem's title when prompted.

3. **View Test Cases**:
    The extension will fetch the test cases and display them in a pop-up message.

4. **Open Solution Files**:
    open the corresponding C++ (`1.cpp`) or Python (`solution.py`) solution files.

5. **Run Solutions**:
    open the command palette, type `CPH: Run Test Cases`, and press Enter.
