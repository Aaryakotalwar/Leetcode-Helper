const fs = require('fs');
const path = "C:/Users/Arya/OneDrive/Desktop/clone/leetcode/src/scripts/run_python.py";

if (fs.existsSync(path)) {
    console.log('File exists:', path);
} else {
    console.log('File not found:', path);
}
console.log('Workspace folder:', workspaceFolder);
console.log('Python script path:', pythonScriptPath);
console.log('Test case directory:', testCaseDir);
