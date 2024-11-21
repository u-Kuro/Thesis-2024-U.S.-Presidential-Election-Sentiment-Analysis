@echo off
echo Starting Installation...
:: Ensure pip is installed
python -m ensurepip

:: Upgrade pip and install core build dependencies
pip install pip==24.0
pip install jupyterlab==3.6.8
pip install setuptools==68.0.0
pip install wheel==0.42.0
pip install cython==3.0.11

:: Install Data Preprocessing dependencies with specific versions
pip install nltk==3.8.1
pip install spacy==2.1.0
pip install neuralcoref==4.0
pip install pandas==1.1.5
pip install tqdm==4.67.0

:: Install Data Gathering dependencies with specific versions
pip install torch==1.13.1
pip install ffmpeg-python==0.2.0
pip install openai-whisper==20230124
pip install pytubefix==8.3.2

:: Install URL Collection dependencies with specific versions
pip install youtube-search-python==1.6.6

:: Download spacy model
pip install "en_core_web_lg @ https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-2.1.0/en_core_web_lg-2.1.0.tar.gz"

echo Installation Completed.
pause