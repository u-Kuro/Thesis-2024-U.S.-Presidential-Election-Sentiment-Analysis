@echo off
echo Starting Installation...

:: Ensure pip is installed
python -m ensurepip

:: Install main dependencies
python -m pip install nltk "ffmpeg-python" "openai-whisper" pandas pytubefix bertopic "scikit-learn"

:: Install other dependencies
python -m pip install torch tqdm

:: Install BERTopic dependencies
python -m pip install "numpy<2" "tf-keras"

echo Installation completed.
pause