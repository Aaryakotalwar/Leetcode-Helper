import * as vscode from 'vscode';
import { exec, spawn } from 'child_process';
import * as fs from 'fs';
import * as path from 'path';

export function activate(context: vscode.ExtensionContext) {
    // Register the command to fetch test cases
    let fetchTestCaseDisposable = vscode.commands.registerCommand('cph.fetchTestCase', async () => {
        const titleSlug = await vscode.window.showInputBox({
            prompt: 'Enter the LeetCode problem title slug',
        });

        if (!titleSlug) {
            vscode.window.showErrorMessage('Title slug is required!');
            return;
        }
        const scriptPath = "C:\\Users\\Arya\\OneDrive\\Desktop\\clone\\leetcode\\src\\scripts\\fetch.py";
        const testCaseDir = "C:\\Users\\Arya\\OneDrive\\Desktop\\clone\\leetcode\\src\\testcases";

        exec(`python3 ${scriptPath} --titleSlug ${titleSlug}`, (error, stdout, stderr) => {
            if (error) {
                vscode.window.showErrorMessage(`Error: ${error.message}`);
                return;
            }
            if (stderr) {
                vscode.window.showWarningMessage(`Warning: ${stderr}`);
                return;
            }
            function formatTestCaseMessage(inputContent: string, outputContent: string, testCaseNumber: number): string {
                return `
**Test Case ${testCaseNumber}:**
---
**Input:**
\`\`\`
${inputContent}
\`\`\`

**Output:**
\`\`\`
${outputContent}
\`\`\`
---
`;
            }

            // Read all input and output files in the directory
            try {
                const files = fs.readdirSync(testCaseDir);

                const inputFiles = files.filter(file => file.startsWith('input_'));
                const outputFiles = files.filter(file => file.startsWith('output_'));

                inputFiles.sort(); // Ensure files are in the correct order
                outputFiles.sort();

                let outputMessage = `Fetched Test Cases for ${titleSlug}:\n\n`;

                inputFiles.forEach((inputFile, index) => {
                    const inputContent = fs.readFileSync(path.join(testCaseDir, inputFile), 'utf-8');
                    const outputContent = fs.readFileSync(path.join(testCaseDir, outputFiles[index]), 'utf-8');

                    outputMessage += formatTestCaseMessage(inputContent, outputContent, index + 1);
                    // outputMessage += `Test Case ${index + 1}:\n`;
                    // outputMessage += `Input:\n${inputContent}\n`;
                    // outputMessage += `Output:\n${outputContent}\n\n`;
                });

                vscode.window.showInformationMessage(outputMessage);
            } catch (err) {
                if (err instanceof Error) {
                    vscode.window.showErrorMessage(`Error reading test cases: ${err.message}`);
                } else {
                    vscode.window.showErrorMessage('Error reading test cases');
                }
                return;
            }
        });
    });

    context.subscriptions.push(fetchTestCaseDisposable);

    // Register the run test command
//     let runTestDisposable = vscode.commands.registerCommand('cph.runTest', async () => {
//         const workspaceFolders = vscode.workspace.workspaceFolders;

//         if (!workspaceFolders || workspaceFolders.length === 0) {
//             vscode.window.showErrorMessage('No workspace folder is open. Cannot run test cases.');
//             return;
//         }

//         const workspaceFolder = workspaceFolders[0].uri.fsPath;
//         const cppFilePath = path.join(workspaceFolder, '1.cpp');
//         const pythonFilePath = path.join(workspaceFolder, 'solution.py');
//         const testCaseDir = "C:\\Users\\Arya\\OneDrive\\Desktop\\clone\\leetcode\\src\\testcases";

//         const isCppFilePresent = fs.existsSync(cppFilePath);
//         const isPythonFilePresent = fs.existsSync(pythonFilePath);

//         if (!isCppFilePresent && !isPythonFilePresent) {
//             vscode.window.showErrorMessage('Neither C++ file nor Python solution file is found in the workspace folder.');
//             return;
//         }

//         if (isCppFilePresent) {
//             // Compile and run the C++ file
//             const executablePath = path.join(workspaceFolder, '1');
//             exec(`g++ -o "${executablePath}" "${cppFilePath}"`, (compileError, stdout, stderr) => {
//                 if (compileError) {
//                     vscode.window.showErrorMessage(`Compilation error: ${stderr || compileError.message}`);
//                     return;
//                 }

//                 runCppTests(executablePath, testCaseDir);
//             });
//         } else if (isPythonFilePresent) {
//             // Run the Python solution file
//             runPythonTests(pythonFilePath, testCaseDir);
//         }
//     });

//     context.subscriptions.push(runTestDisposable);
// }
let runTestDisposable = vscode.commands.registerCommand('cph.runTest', async () => {
    const workspaceFolders = vscode.workspace.workspaceFolders;

    if (!workspaceFolders || workspaceFolders.length === 0) {
        vscode.window.showErrorMessage('No workspace folder is open. Cannot run test cases.');
        return;
    }

    const workspaceFolder = workspaceFolders[0].uri.fsPath;
    const cppFilePath = path.join(workspaceFolder, '1.cpp');
    const pythonFilePath = path.join(workspaceFolder, 'solution.py');
    const testCaseDir = "C:\\Users\\Arya\\OneDrive\\Desktop\\clone\\leetcode\\src\\testcases";

    const isCppFilePresent = fs.existsSync(cppFilePath);
    const isPythonFilePresent = fs.existsSync(pythonFilePath);

    if (!isCppFilePresent && !isPythonFilePresent) {
        vscode.window.showErrorMessage('Neither C++ file nor Python solution file is found in the workspace folder.');
        return;
    }

    // Ask the user which language to run if both files exist
    if (isCppFilePresent && isPythonFilePresent) {
        const choice = await vscode.window.showQuickPick(
            ['C++', 'Python'],
            { placeHolder: 'Both C++ and Python files exist. Which one would you like to run?' }
        );

        if (!choice) {
            vscode.window.showErrorMessage('No language selected to run.');
            return;
        }

        if (choice === 'C++') {
            // Compile and run the C++ file
            const executablePath = path.join(workspaceFolder, '1');
            exec(`g++ -o "${executablePath}" "${cppFilePath}"`, (compileError, stdout, stderr) => {
                if (compileError) {
                    vscode.window.showErrorMessage(`Compilation error: ${stderr || compileError.message}`);
                    return;
                }

                runCppTests(executablePath, testCaseDir);
            });
        } else if (choice === 'Python') {
            // Run the Python solution file
            runPythonTests(pythonFilePath, testCaseDir);
        }
    } else if (isCppFilePresent) {
        // Only C++ file exists, run it
        const executablePath = path.join(workspaceFolder, '1');
        exec(`g++ -o "${executablePath}" "${cppFilePath}"`, (compileError, stdout, stderr) => {
            if (compileError) {
                vscode.window.showErrorMessage(`Compilation error: ${stderr || compileError.message}`);
                return;
            }

            runCppTests(executablePath, testCaseDir);
        });
    } else if (isPythonFilePresent) {
        // Only Python file exists, run it
        runPythonTests(pythonFilePath, testCaseDir);
    }
});

function runCppTests(executablePath: string, testCaseDir: string) {
    const pythonScriptPath = "C:/Users/Arya/OneDrive/Desktop/clone/leetcode/src/scripts/run_cpp.py"; // Path to the Python script
    console.log("Reached before Python process spawn");

    const pythonProcess = spawn(
        '"C:/Program Files/Python313/python.exe"',
        [
            pythonScriptPath,
            `"${executablePath}"`, // Quote the file path
            `"${testCaseDir}"`     // Quote the test case directory
        ],
        { shell: true }
    );

    let output = '';
    let errorOutput = '';

    pythonProcess.stdout.on('data', (data) => {
        output += data.toString();
        console.log("Stdout Data:", data.toString());  // Log stdout
    });

    pythonProcess.stderr.on('data', (data) => {
        errorOutput += data.toString();
    });

    pythonProcess.on('close', (code) => {
        if (code === 0) {
            vscode.window.showInformationMessage('Test cases executed successfully.');
            vscode.window.showInformationMessage(`Execution Output:\n${output}`);
        } else {
            vscode.window.showErrorMessage(`Error executing test cases: ${errorOutput}`);
        }
    });
}

function runPythonTests(pythonFilePath: string, testCaseDir: string) {
    const pythonScriptPath = "C:/Users/Arya/OneDrive/Desktop/clone/leetcode/src/scripts/run_python.py"; // Path to the Python script

    const pythonProcess = spawn(
        '"C:/Program Files/Python313/python.exe"',
        [
            pythonScriptPath,
            `"${pythonFilePath}"`, // Quote the file path
            `"${testCaseDir}"`     // Quote the test case directory
        ],
        { shell: true }
    );
    
    let output = '';
    let errorOutput = '';

    pythonProcess.stdout.on('data', (data) => {
        output += data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
        errorOutput += data.toString();
    });

    pythonProcess.on('close', (code) => {
        console.log(`Python process exited with code ${code}`);
        if (code === 0) {
            vscode.window.showInformationMessage('Test cases executed successfully.');
            vscode.window.showInformationMessage(`Execution Output:\n${output}`);
        } else {
            vscode.window.showErrorMessage(`Error executing test cases: ${errorOutput}`);
        }
    });
    
    }
}

export function deactivate() {}
