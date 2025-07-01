from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

app = Flask(__name__)

# Initialize model and tokenizer as None
model = None
tokenizer = None

# Replace with your Hugging Face model name
MODEL_NAME = "u-kuro/sentiment-model"  # Change this!

with app.app_context():
    """Load model and tokenizer once"""
    if model is None or tokenizer is None:
        print("Loading model...")
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
        model.eval()
        print("Model loaded successfully!")

def get_sentiment_score(text):
    """Get sentiment score from text"""    
    with torch.no_grad():
        encoding = tokenizer(
            text,
            truncation=True,
            padding=True,
            max_length=128,
            return_tensors='pt'
        )
        
        outputs = model(**encoding)
        _, predicted = torch.max(outputs.logits, 1)
        sentiment_score = int((predicted - 1).cpu().numpy()[0])
        
        return sentiment_score

def get_sentiment_label(score):
    """Convert sentiment score to label"""
    sentiment_map = {
        -1: "Negative",
        0: "Neutral", 
        1: "Positive"
    }
    return sentiment_map.get(score, "Unknown")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({'error': 'Please provide text to analyze'}), 400
        
        # Get prediction
        sentiment_score = get_sentiment_score(text)
        sentiment_label = get_sentiment_label(sentiment_score)
        
        return jsonify({
            'sentiment_score': sentiment_score,
            'sentiment_label': sentiment_label,
            'text': text
        })
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'An error occurred during prediction'}), 500
    
@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()