from flask import Flask, request, jsonify, render_template
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer
import torch
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

model_path = r"C:\Users\Lenovo\review_app\Review_model"  
model = DistilBertForSequenceClassification.from_pretrained(model_path)
tokenizer = DistilBertTokenizer.from_pretrained(model_path)

model.eval()

# Function for prediction
def predict(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=-1)
    return predicted_class.item()

# Route to get predictions
@app.route('/predict', methods=['POST'])
def predict_route():
    data = request.json  # Get the JSON data from the POST request
    text = data.get('text', '')

    if text:
        prediction = predict(text)
        if prediction == 0:
            result = "Computer Generated review"
        else:
            result = "Actual Review"
        return jsonify({'prediction': result})
    else:
        return jsonify({'error': 'No text provided'}), 400

# Route to serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
