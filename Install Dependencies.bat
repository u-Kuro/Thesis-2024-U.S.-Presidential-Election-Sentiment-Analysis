@echo off
echo Starting Installation...

:: Ensure pip is installed
python -m ensurepip

:: Install main dependencies
pip install torch "ffmpeg-python" "openai-whisper" pytubefix nltk pandas transformers bertopic "scikit-learn"

:: Install other dependencies
pip install tqdm jupyter ipywidgets

:: Install BERTopic dependencies
pip install "numpy<2" "tf-keras"

echo Installation Completed.
pause