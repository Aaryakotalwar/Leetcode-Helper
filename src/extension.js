"use strict";
// import * as vscode from 'vscode';
// import { exec, spawn } from 'child_process';
// import * as fs from 'fs';
// import * as path from 'path';
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = activate;
exports.deactivate = deactivate;
// export function activate(context: vscode.ExtensionContext) {
//     let disposable = vscode.commands.registerCommand('cph.fetchTestCase', async () => {
//         const titleSlug = await vscode.window.showInputBox({
//             prompt: 'Enter the LeetCode problem title slug',
//         });
//         if (!titleSlug) {
//             vscode.window.showErrorMessage('Title slug is required!');
//             return;
//         }
//         const scriptPath = "C:\\Users\\Arya\\OneDrive\\Desktop\\clone\\leetcode\\src\\scripts\\fetch.py";
//         const testCaseDir = "C:\\Users\\Arya\\OneDrive\\Desktop\\clone\\leetcode\\src\\testcases";
//         exec(`python3 ${scriptPath} --titleSlug ${titleSlug}`, (error, stdout, stderr) => {
//             if (error) {
//                 vscode.window.showErrorMessage(`Error: ${error.message}`);
//                 return;
//             }
//             if (stderr) {
//                 vscode.window.showWarningMessage(`Warning: ${stderr}`);
//                 return;
//             }
//             let inputOutputHtml = `
//                 <html>
//                 <head>
//                     <style>
//                         body {
//                             font-family: 'Inter', sans-serif;
//                             background-color: #121212;
//                             color: #e0e0e0;
//                             padding: 20px;
//                             margin: 0;
//                         }
//                         h2 {
//                             text-align: center;
//                             color: #ff9800;
//                             font-weight: 600;
//                             margin-bottom: 20px;
//                         }
//                         .test-case-card {
//                             background: #1e1e1e;
//                             border-radius: 12px;
//                             box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
//                             margin: 20px 0;
//                             padding: 20px;
//                             transition: transform 0.3s ease, box-shadow 0.3s ease;
//                         }
//                         .test-case-card:hover {
//                             transform: translateY(-8px);
//                             box-shadow: 0 12px 28px rgba(0, 0, 0, 0.4);
//                         }
//                         .test-case-header {
//                             font-size: 20px;
//                             font-weight: bold;
//                             margin-bottom: 15px;
//                             color: #29b6f6;
//                             border-bottom: 2px solid #ff9800;
//                             padding-bottom: 5px;
//                         }
//                         .section-title {
//                             margin: 15px 0 5px;
//                             font-weight: bold;
//                             color: #fbc02d;
//                             text-transform: uppercase;
//                         }
//                         .test-case-content {
//                             background: #212121;
//                             border-radius: 8px;
//                             padding: 15px;
//                             white-space: pre-wrap;
//                             font-family: 'Fira Code', monospace;
//                             overflow-x: auto;
//                             color: #e0e0e0;
//                         }
//                         .footer {
//                             text-align: center;
//                             margin-top: 30px;
//                             font-size: 14px;
//                             color: #757575;
//                         }
//                         .footer a {
//                             color: #29b6f6;
//                             text-decoration: none;
//                         }
//                         .footer a:hover {
//                             text-decoration: underline;
//                         }
//                         .button {
//                             background-color: #ff9800;
//                             border: none;
//                             border-radius: 8px;
//                             color: #121212;
//                             padding: 10px 50px;
//                             font-weight: bold;
//                             cursor: pointer;
//                             margin-top: 15px;
//                             display: inline-block;
//                         }
//                         .button:hover {
//                             background-color: #e68900;
//                         }
//                     </style>
//                 </head>
//                 <body>
//                     <h2>Fetched Test Cases</h2>
//             `;
//             // Read all input and output files in the directory
//             try {
//                 const files = fs.readdirSync(testCaseDir);
//                 const inputFiles = files.filter(file => file.startsWith('input_'));
//                 const outputFiles = files.filter(file => file.startsWith('output_'));
//                 inputFiles.sort(); // Ensure files are in the correct order
//                 outputFiles.sort();
//                 inputFiles.forEach((inputFile, index) => {
//                     const inputContent = fs.readFileSync(path.join(testCaseDir, inputFile), 'utf-8');
//                     const outputContent = fs.readFileSync(path.join(testCaseDir, outputFiles[index]), 'utf-8');
//                     inputOutputHtml += `
//                         <div class="test-case-card">
//                             <div class="test-case-header">Test Case ${index + 1}</div>
//                             <div class="section-title">Input</div>
//                             <div class="test-case-content">${inputContent}</div>
//                             <div class="section-title">Output</div>
//                             <div class="test-case-content">${outputContent}</div>
//                         </div>
//                     `;
//                 });
//             } catch (err) {
//                 vscode.window.showErrorMessage(`Error reading test cases: {err.message}`);
//                 return;
//             }
//             inputOutputHtml += `
//                     <button class="button" onclick="openCppFile()">Open C++ File</button>
//                     <button class="button" onclick="openPythonFile()">Open Python File</button>
//                     <button class="button" onclick="run_cpp_file()">Run C++ File</button>
//                     <button class="button" onclick="run_python_file()">Run Python File</button>
//                     <div class="footer">
//                         Built with ❤ by Rohit Bokare
//                     </div>
//                     <script>
//                         const vscode = acquireVsCodeApi();
//                         function openCppFile() {
//                             vscode.postMessage({ command: 'openCppFile' });
//                         }
//                         function openPythonFile() {
//                             vscode.postMessage({ command: 'openPythonFile' });
//                         }
//                         function run_cpp_file() {
//                             vscode.postMessage({ command: 'run_cpp_file' });
//                         }
//                         function run_python_file() {
//                             vscode.postMessage({ command: 'run_python_file' });
//                         }
//                         window.addEventListener('message', (event) => {
//                             const message = event.data;
//                             if (message.command === 'display_output') {
//                                 const outputContainer = document.createElement('div');
//                                 outputContainer.classList.add('test-case-card');
//                                 outputContainer.innerHTML = '<div class="test-case-header">Execution Output</div><div class="test-case-content">' + message.output + '</div>';
//                                 document.body.appendChild(outputContainer);
//                             }
//                         });
//                     </script>
//                 </body>
//                 </html>
//             `;
//             // Display the test cases in a webview
//             const panel = vscode.window.createWebviewPanel(
//                 'testCaseOutput',
//                 'Test Case Output',
//                 vscode.ViewColumn.One,
//                 {
//                     enableScripts: true, // Enable scripts in the webview
//                 }
//             );
//             panel.webview.html = inputOutputHtml;
//             // Handle messages from the webview
//             panel.webview.onDidReceiveMessage(
//                 (message) => {
//                     if (message.command === 'openCppFile') {
//                         openCppTab(context);
//                     } else if (message.command === 'openPythonFile') {
//                         openPythonTab(context);
//                     } else if (message.command === 'run_cpp_file') {
//                         run_cpp_file(context, panel);
//                     } else if (message.command === 'run_python_file') {
//                         run_python_file(context, panel);
//                     }
//                 },
//                 undefined,
//                 context.subscriptions
//             );
//         });
//     });
//     context.subscriptions.push(disposable);
// }
// function run_cpp_file(context: vscode.ExtensionContext, panel: vscode.WebviewPanel) {
//     const workspaceFolders = vscode.workspace.workspaceFolders;
//     if (!workspaceFolders || workspaceFolders.length === 0) {
//         vscode.window.showErrorMessage('No workspace folder is open. Cannot run test cases.');
//         return;
//     }
//     const workspaceFolder = workspaceFolders[0].uri.fsPath;
//     const cppFilePath = path.join(workspaceFolder, '1.cpp');
//     const executablePath = path.join(workspaceFolder, '1');
//     const pythonScriptPath ="C:/Users/Arya/OneDrive/Desktop/clone/leetcode/src/scripts/run_cpp.py"; // Path to the Python script
//     const testCaseDir =  "C:/Users/Arya/OneDrive/Desktop/clone/leetcode/src/testcases";  // Test case directory
//     if (!fs.existsSync(cppFilePath)) {
//         vscode.window.showErrorMessage('C++ file (1.cpp) not found in the workspace folder.');
//         return;
//     }
//     if (!fs.existsSync(pythonScriptPath)) {
//         vscode.window.showErrorMessage('Python script (run_cpp.py) not found in the specified path.');
//         return;
//     }
//     exec(`g++ -o "${executablePath}" "${cppFilePath}"`, (compileError, stdout, stderr) => {
//         if (compileError) {
//             vscode.window.showErrorMessage(`Compilation error: ${stderr || compileError.message}`);
//             return;
//         }
//         // const pythonProcess = spawn('python3', [pythonScriptPath, executablePath, testCaseDir], { shell: true });
//         const pythonProcess = spawn(
//             '"C:/Program Files/Python313/python.exe"',
//             [
//                 pythonScriptPath,
//                 `"${executablePath}"`, // Quote the file path
//                 `"${testCaseDir}"`     // Quote the test case directory
//             ],
//             { shell: true }
//         );
//         let output = '';
//         let errorOutput = '';
//         pythonProcess.stdout.on('data', (data) => {
//             output += data.toString();
//         });
//         pythonProcess.stderr.on('data', (data) => {
//             errorOutput += data.toString();
//         });
//         pythonProcess.on('close', (code) => {
//             if (code === 0) {
//                 vscode.window.showInformationMessage('Test cases executed successfully.');
//                 panel.webview.postMessage({ command: 'display_output', output }); // Send output to the Webview
//             } else {
//                 vscode.window.showErrorMessage(`Error executing test cases: ${errorOutput}`);
//             }
//         });
//     });
// }
// function run_python_file(context: vscode.ExtensionContext, panel: vscode.WebviewPanel) {
//     const workspaceFolders = vscode.workspace.workspaceFolders;
//     if (!workspaceFolders || workspaceFolders.length === 0) {
//         vscode.window.showErrorMessage('No workspace folder is open. Cannot run test cases.');
//         console.log('workspaceFolders:', workspaceFolders); // Add this for debugging
//         return;
//     }
//     const workspaceFolder = workspaceFolders[0].uri.fsPath;
//     const pythonFilePath = path.join(workspaceFolder, 'solution.py');
//     const pythonScriptPath = "C:/Users/Arya/OneDrive/Desktop/clone/leetcode/src/scripts/run_python.py";
//     const testCaseDir = "C:\\Users\\Arya\\OneDrive\\Desktop\\clone\\leetcode\\src\\testcases";
//     console.log("hey");
//     if (!fs.existsSync(pythonFilePath)) {
//         vscode.window.showErrorMessage('Python solution file (solution.py) not found in the workspace folder.');
//         return;
//     }
//     if (!fs.existsSync(pythonScriptPath)) {
//         vscode.window.showErrorMessage('Python script (run_python.py) not found in the specified path.');
//         return;
//     }
//     // const pythonProcess = spawn("C:/Program Files/Python313/python.exe", [pythonScriptPath, pythonFilePath, testCaseDir], { shell: true });
//     // const pythonProcess = spawn('py/thon', [pythonScriptPath, pythonFilePath, testCaseDir], { shell: true });
//     // const pythonProcess = spawn('"C:/Program Files/Python313/python.exe"', [pythonScriptPath, pythonFilePath, testCaseDir], { shell: true });
//     const pythonProcess = spawn(
//         '"C:/Program Files/Python313/python.exe"',
//         [
//             pythonScriptPath,
//             `"${pythonFilePath}"`, // Quote the file path
//             `"${testCaseDir}"`     // Quote the test case directory
//         ],
//         { shell: true }
//     );
//     let output = '';
//     let errorOutput = '';
//     pythonProcess.stdout.on('data', (data) => {
//         output += data.toString();
//     });
//     pythonProcess.stderr.on('data', (data) => {
//         errorOutput += data.toString();
//         console.error("Error Output:", data.toString());
//     });
//     pythonProcess.on('close', (code) => {
//         if (code === 0) {
//             vscode.window.showInformationMessage('Test cases executed successfully.');
//             panel.webview.postMessage({ command: 'display_output', output }); // Send output to the Webview
//         } else {
//             vscode.window.showErrorMessage(`Error executing test cases: ${errorOutput}`);
//             vscode.window.showErrorMessage(`Error executing test cases: ${output}`);
//         }
//     });
// }
// function openCppTab(context: vscode.ExtensionContext) {
//     const cppContent = `// This is a sample C++ file for the entered TitleSlug
// #include <iostream>
// using namespace std;
// int main() {
//     cout << "Hello, World!" << endl;
//     return 0;
// }
// `;
//     const workspaceFolders = vscode.workspace.workspaceFolders;
//     if (workspaceFolders && workspaceFolders.length > 0) {
//         const filePath = path.join(workspaceFolders[0].uri.fsPath, '1.cpp');
//         fs.writeFileSync(filePath, cppContent);
//         vscode.workspace.openTextDocument(filePath)
//             .then((document) => {
//                 vscode.window.showTextDocument(document, vscode.ViewColumn.Two);
//             });
//     } else {
//         vscode.window.showOpenDialog({
//             canSelectFolders: true,
//             openLabel: 'Select a folder to save 1.cpp',
//         }).then((folderUris) => {
//             if (folderUris && folderUris.length > 0) {
//                 const folderPath = folderUris[0].fsPath;
//                 const filePath = path.join(folderPath, '1.cpp');
//                 fs.writeFileSync(filePath, cppContent);
//                 vscode.workspace.openTextDocument(filePath)
//                     .then((document) => {
//                         vscode.window.showTextDocument(document, vscode.ViewColumn.Two);
//                     });
//             } else {
//                 vscode.window.showErrorMessage('No folder selected. Cannot create 1.cpp.');
//             }
//         });
//     }
// }
// function openPythonTab(context: vscode.ExtensionContext) {
//     const pythonContent = `# This is a sample Python file for the entered TitleSlug
// def solve():
//     pass
// if __name__ == "__main__":
//     t = 1  # Number of test cases
//     for _ in range(t):
//         solve()
// `;
//     const workspaceFolders = vscode.workspace.workspaceFolders;
//     if (workspaceFolders && workspaceFolders.length > 0) {
//         const filePath = path.join(workspaceFolders[0].uri.fsPath, 'solution.py');
//         fs.writeFileSync(filePath, pythonContent);
//         vscode.workspace.openTextDocument(filePath)
//             .then((document) => {
//                 vscode.window.showTextDocument(document, vscode.ViewColumn.Two);
//             });
//     } else {
//         vscode.window.showOpenDialog({
//             canSelectFolders: true,
//             openLabel: 'Select a folder to save solution.py',
//         }).then((folderUris) => {
//             if (folderUris && folderUris.length > 0) {
//                 const folderPath = folderUris[0].fsPath;
//                 const filePath = path.join(folderPath, 'solution.py');
//                 fs.writeFileSync(filePath, pythonContent);
//                 vscode.workspace.openTextDocument(filePath)
//                     .then((document) => {
//                         vscode.window.showTextDocument(document, vscode.ViewColumn.Two);
//                     });
//             } else {
//                 vscode.window.showErrorMessage('No folder selected. Cannot create solution.py.');
//             }
//         });
//     }
// }
// export function deactivate() {}
//.......................................................................................
//.......................................................................................
const vscode = __importStar(require("vscode"));
const child_process_1 = require("child_process");
const fs = __importStar(require("fs"));
const path = __importStar(require("path"));
function activate(context) {
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
        (0, child_process_1.exec)(`python3 ${scriptPath} --titleSlug ${titleSlug}`, (error, stdout, stderr) => {
            if (error) {
                vscode.window.showErrorMessage(`Error: ${error.message}`);
                return;
            }
            if (stderr) {
                vscode.window.showWarningMessage(`Warning: ${stderr}`);
                return;
            }
            function formatTestCaseMessage(inputContent, outputContent, testCaseNumber) {
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
            }
            catch (err) {
                if (err instanceof Error) {
                    vscode.window.showErrorMessage(`Error reading test cases: ${err.message}`);
                }
                else {
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
            const choice = await vscode.window.showQuickPick(['C++', 'Python'], { placeHolder: 'Both C++ and Python files exist. Which one would you like to run?' });
            if (!choice) {
                vscode.window.showErrorMessage('No language selected to run.');
                return;
            }
            if (choice === 'C++') {
                // Compile and run the C++ file
                const executablePath = path.join(workspaceFolder, '1');
                (0, child_process_1.exec)(`g++ -o "${executablePath}" "${cppFilePath}"`, (compileError, stdout, stderr) => {
                    if (compileError) {
                        vscode.window.showErrorMessage(`Compilation error: ${stderr || compileError.message}`);
                        return;
                    }
                    runCppTests(executablePath, testCaseDir);
                });
            }
            else if (choice === 'Python') {
                // Run the Python solution file
                runPythonTests(pythonFilePath, testCaseDir);
            }
        }
        else if (isCppFilePresent) {
            // Only C++ file exists, run it
            const executablePath = path.join(workspaceFolder, '1');
            (0, child_process_1.exec)(`g++ -o "${executablePath}" "${cppFilePath}"`, (compileError, stdout, stderr) => {
                if (compileError) {
                    vscode.window.showErrorMessage(`Compilation error: ${stderr || compileError.message}`);
                    return;
                }
                runCppTests(executablePath, testCaseDir);
            });
        }
        else if (isPythonFilePresent) {
            // Only Python file exists, run it
            runPythonTests(pythonFilePath, testCaseDir);
        }
    });
    function runCppTests(executablePath, testCaseDir) {
        const pythonScriptPath = "C:/Users/Arya/OneDrive/Desktop/clone/leetcode/src/scripts/run_cpp.py"; // Path to the Python script
        console.log("Reached before Python process spawn");
        const pythonProcess = (0, child_process_1.spawn)('"C:/Program Files/Python313/python.exe"', [
            pythonScriptPath,
            `"${executablePath}"`, // Quote the file path
            `"${testCaseDir}"` // Quote the test case directory
        ], { shell: true });
        let output = '';
        let errorOutput = '';
        pythonProcess.stdout.on('data', (data) => {
            output += data.toString();
            console.log("Stdout Data:", data.toString()); // Log stdout
        });
        pythonProcess.stderr.on('data', (data) => {
            errorOutput += data.toString();
        });
        pythonProcess.on('close', (code) => {
            if (code === 0) {
                vscode.window.showInformationMessage('Test cases executed successfully.');
                vscode.window.showInformationMessage(`Execution Output:\n${output}`);
            }
            else {
                vscode.window.showErrorMessage(`Error executing test cases: ${errorOutput}`);
            }
        });
    }
    function runPythonTests(pythonFilePath, testCaseDir) {
        const pythonScriptPath = "C:/Users/Arya/OneDrive/Desktop/clone/leetcode/src/scripts/run_python.py"; // Path to the Python script
        const pythonProcess = (0, child_process_1.spawn)('"C:/Program Files/Python313/python.exe"', [
            pythonScriptPath,
            `"${pythonFilePath}"`, // Quote the file path
            `"${testCaseDir}"` // Quote the test case directory
        ], { shell: true });
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
            }
            else {
                vscode.window.showErrorMessage(`Error executing test cases: ${errorOutput}`);
            }
        });
    }
}
function deactivate() { }
//# sourceMappingURL=extension.js.map