function analyzeResume() {
    var resumeFile = document.getElementById('resumeInput').files[0];
    if (resumeFile) {
        // Implement analysis logic here
        alert('Resume/CV uploaded successfully. Starting analysis...');
    } else {
        alert('Please select a resume/CV file before analyzing.');
    }
}
// scriptresume.js

function analyzeResume() {
    // Get the role input value
    var role = document.getElementById("roleInput").value;

    // Perform analysis on the uploaded resume
    // Include the role variable in your analysis process
    // For example:
    console.log("Analyzing resume for role: " + role);
}
