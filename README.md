# U.S. Political Sentiment Analysis System

A production-ready sentiment analysis system trained on 2024 U.S. political discourse from YouTube videos. Built with BERT and deployed as a Flask web application on Hugging Face Spaces.

---

### 🖥️ Web Application Demo
<a href="https://u-kuro-sentiment-predictor.hf.space" target="_blank"><img src="./screenshots/web-interface.png" alt="Web Interface"></a>

**Live Demo:** [https://u-kuro-sentiment-predictor.hf.space](https://u-kuro-sentiment-predictor.hf.space/)  
**Model:** [https://huggingface.co/u-kuro/sentiment-model](https://huggingface.co/u-kuro/sentiment-model)  
**Source Code:** [https://huggingface.co/spaces/u-kuro/sentiment-predictor/tree/main](https://huggingface.co/spaces/u-kuro/sentiment-predictor/tree/main)

---

## 📄 Thesis Document

<a href="./Thesis-Document.pdf#page=1" target="_blank"><img src="./screenshots/thesis-page-01.png" alt="Thesis Page 1"></a>
<br/>
<details>
    <summary><b>📖 Show More</b></summary>
    <br/>
    <a href="./Thesis-Document.pdf#page=2" target="_blank"><img src="./screenshots/thesis-page-02.png" alt="Thesis Page 2"></a>
    <a href="./Thesis-Document.pdf#page=3" target="_blank"><img src="./screenshots/thesis-page-03.png" alt="Thesis Page 3"></a>
    <a href="./Thesis-Document.pdf#page=4" target="_blank"><img src="./screenshots/thesis-page-04.png" alt="Thesis Page 4"></a>
    <a href="./Thesis-Document.pdf#page=5" target="_blank"><img src="./screenshots/thesis-page-05.png" alt="Thesis Page 5"></a>
    <a href="./Thesis-Document.pdf#page=6" target="_blank"><img src="./screenshots/thesis-page-06.png" alt="Thesis Page 6"></a>
    <a href="./Thesis-Document.pdf#page=7" target="_blank"><img src="./screenshots/thesis-page-07.png" alt="Thesis Page 7"></a>
    <br/>
    <br/>
    <details>
        <summary><b>📖 Show Other References</b></summary>
        <br/>
        <a href="./Thesis-Document.pdf#page=8" target="_blank"><img src="./screenshots/thesis-page-08.png" alt="Thesis Page 8"></a>
        <a href="./Thesis-Document.pdf#page=9" target="_blank"><img src="./screenshots/thesis-page-09.png" alt="Thesis Page 9"></a>
    </details>
</details>

---

## 🛠️ Technical Stack

**Data Processing:**
- Youtube-Search-Python and PyTubeFix
- FFmpeg and OpenAI Whisper
- NLTK and spaCy (neuralcoref)

**Model Building:**
- Hugging Face Transformers (BERT, DistilBERT)
- Scikit-learn
- PyTorch

**Data Visualization:**
- Matplotlib and Seaborn
- WordCloud
- Pandas and NumPy

**Deployment:**
- Flask
- Docker
- Hugging Face Spaces

---

## 📂 Project Structure

```
├── 1) Data Collection/          # YouTube URL collection
├── 2) Video to Text Pipeline/   # Data transformation
├── 3) Text Preprocessing/       # Data cleaning and filtering
├── 4) Sentiment Annotation/     # Manual labeling and dataset creation
├── 5) BERT Models/              # Model training and evaluation
│   ├── BERT variants (4)
│   └── DistilBERT variants (4)
├── 6) Visualizations/           # Results visualization and analysis
└── Model-Prototype/web/         # Flask Web App
    ├── app.py
    ├── templates/
    └── static/
```
---

## 🔗 Quick Links

- **Try the Live App:** [u-kuro-sentiment-predictor.hf.space](https://u-kuro-sentiment-predictor.hf.space/)
- **View the Model:** [huggingface.co/u-kuro/sentiment-model](https://huggingface.co/u-kuro/sentiment-model)
- **Browse Source Code:** [huggingface.co/spaces/u-kuro/sentiment-predictor](https://huggingface.co/spaces/u-kuro/sentiment-predictor/tree/main)