FROM python:3.8.0

RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

COPY --chown=user ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --user -r requirements.txt

COPY --chown=user . /app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:7860", "app:app"]