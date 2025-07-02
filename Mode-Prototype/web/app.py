import os, torch
from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()
MODEL_NAME = os.environ['MODEL_NAME']
TOKEN = os.environ['HF_TOKEN']

ismain = __name__ == '__main__'
app = FastAPI()
model = None
tokenizer = None

if ismain and (model is None or tokenizer is None):
    with app.app_context():
        print("Loading model...")
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, token=TOKEN)
        model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, token=TOKEN)
        model.eval()
        print("Model loaded successfully!")

def get_sentiment_score(text):
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

if ismain:
    app.run(host="0.0.0.0", port=7860, debug=True)