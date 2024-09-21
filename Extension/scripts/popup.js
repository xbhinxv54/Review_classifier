document.getElementById('getPredictionButton').addEventListener('click', async () => {
    const text = document.getElementById('reviewText').value;
    const response = await fetch('http://localhost:5000/predict', {  // Adjust the URL if necessary
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: text })
    });

    const data = await response.json();
    const resultDiv = document.getElementById('result');

    if (response.ok) {
        resultDiv.innerHTML = `Prediction: ${data.prediction}`;
        resultDiv.classList.remove('error');
    } else {
        resultDiv.innerHTML = `Error: ${data.error}`;
        resultDiv.classList.add('error');
    }
});
