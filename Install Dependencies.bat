@echo off
echo Starting Installation...

:: Ensure pip is installed
python -m ensurepip

:: Install main dependencies
pip install nltk "ffmpeg-python" "openai-whisper" pandas pytubefix bertopic "scikit-learn"

:: Install other dependencies
pip install torch tqdm ipywidgets

:: Install BERTopic dependencies
pip install "numpy<2" "tf-keras"

echo Installation completed.
pause