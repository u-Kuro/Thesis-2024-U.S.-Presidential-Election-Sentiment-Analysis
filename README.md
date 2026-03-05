# U.S. Political Sentiment Analysis System

A production-ready sentiment analysis system trained on 2024 U.S. political discourse from YouTube videos. Built with BERT and deployed as a Flask web application on Hugging Face Spaces.

---

### 🖥️ Web Application Demo
[![Web Interface](./screenshots/web-interface.png)](https://u-kuro-sentiment-predictor.hf.space)

**Live Demo:** [https://u-kuro-sentiment-predictor.hf.space](https://u-kuro-sentiment-predictor.hf.space/)  
**Model:** [https://huggingface.co/u-kuro/sentiment-model](https://huggingface.co/u-kuro/sentiment-model)  
**Source Code:** [https://huggingface.co/spaces/u-kuro/sentiment-predictor/tree/main](https://huggingface.co/spaces/u-kuro/sentiment-predictor/tree/main)

---

## 📄 Thesis Document

[![Thesis Page 1](./screenshots/thesis-page-01.png)](./screenshots/thesis-page-01.png)
<details>
<summary><b>📖 Show More</b></summary>
 
[![Thesis Page 2](./screenshots/thesis-page-02.png)](./screenshots/thesis-page-02.png)
[![Thesis Page 3](./screenshots/thesis-page-03.png)](./screenshots/thesis-page-03.png)
[![Thesis Page 4](./screenshots/thesis-page-04.png)](./screenshots/thesis-page-04.png)
[![Thesis Page 5](./screenshots/thesis-page-05.png)](./screenshots/thesis-page-05.png)
[![Thesis Page 6](./screenshots/thesis-page-06.png)](./screenshots/thesis-page-06.png)
[![Thesis Page 7](./screenshots/thesis-page-07.png)](./screenshots/thesis-page-07.png)
[![Thesis Page 8](./screenshots/thesis-page-08.png)](./screenshots/thesis-page-08.png)
[![Thesis Page 9](./screenshots/thesis-page-09.png)](./screenshots/thesis-page-09.png)
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
- Matplotlib
- Seaborn
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