FROM python:3.10-slim-bookworm

# Copy and install requirements
COPY requirements.txt requirements.txt

RUN pip install -U pip cython wheel
RUN pip install -r requirements.txt

# Copy the main folder for the API
COPY api api

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
