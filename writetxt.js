const fs = require("fs");
const path = require("path");

// Read the file "MyFile1.txt" in the same directory
const filePath = path.join(__dirname, 'MyFile1.txt');

// Read entire file content as a string
let fileContent = fs.readFileSync(filePath, 'utf8');

// Read lines of the file into an array
let fileLines = fileContent.split('\n');

// Log for verification
console.log("File Content as string:", fileContent);
console.log("File Lines as array:", fileLines);

// Overwrite the file with new content
let L = ["Hello\n", "World\n"];

// This will delete the old content and write new data
fs.writeFileSync(filePath, "Hello");            // Write "Hello" without newline
fs.appendFileSync(filePath, "Hello\n");         // Append "Hello" with newline
fs.appendFileSync(filePath, L.join(""));        // Append the list of lines (joined as a string)

fileContent = fs.readFileSync(filePath, 'utf8'); // re read the contents after write
fileLines = fileContent.split('\n'); // convert to list again

//print both versions of the content, as a list or as a plain string
console.log("File Content as string:", fileContent);
console.log("File Lines as array:", fileLines);