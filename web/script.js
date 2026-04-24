// Initialize Lucide Icons
lucide.createIcons();

document.addEventListener('DOMContentLoaded', () => {
    const scanBtn = document.getElementById('scanBtn');
    const dropZone = document.getElementById('dropZone');
    const dropZoneContent = document.getElementById('dropZoneContent');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const analysisResult = document.getElementById('analysisResult');
    const resultText = document.getElementById('resultText');

    function simulateAnalysis() {
        // Reset state
        dropZoneContent.classList.add('hidden');
        loadingIndicator.classList.remove('hidden');
        analysisResult.classList.add('hidden');

        // Simulate network delay
        setTimeout(() => {
            loadingIndicator.classList.add('hidden');
            dropZoneContent.classList.remove('hidden');
            
            // Show result
            resultText.innerText = "Identified Chicken Breast (200g), Rice (150g). Estimated Macros: Protein 60g, Carbs 45g, Fat 5g.";
            analysisResult.classList.remove('hidden');
        }, 1500);
    }

    // Attach Event Listeners
    scanBtn.addEventListener('click', simulateAnalysis);
    dropZone.addEventListener('click', simulateAnalysis);
});
