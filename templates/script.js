// Function to show/hide elements
function toggleElementVisibility(elementId, isVisible) {
    const element = document.getElementById(elementId);
    element.style.display = isVisible ? "block" : "none";
}

// Function to upload an image and show analysis options
function uploadImage() {
    const imageInput = document.getElementById("imageInput");
    imageInput.click();

    imageInput.addEventListener("change", function () {
        toggleElementVisibility("options", true);
    });
}

// Function to perform garbage detection analysis
function analyzeGarbage() {
    // Replace this with your actual garbage detection code
    const result = "Garbage detected in the image.";
    displayResult(result);
}

// Function to perform crowd density detection analysis
function analyzeCrowdDensity() {
    // Replace this with your actual crowd density detection code
    const result = "Crowd density analysis result.";
    displayResult(result);
}

// Function to perform suspicious activity detection analysis
function analyzeSuspiciousActivity() {
    // Replace this with your actual suspicious activity detection code
    const result = "Suspicious activity detected.";
    displayResult(result);
}

// Function to display analysis result
function displayResult(result) {
    const analysisResult = document.getElementById("analysisResult");
    analysisResult.textContent = result;
    toggleElementVisibility("result", true);
}

