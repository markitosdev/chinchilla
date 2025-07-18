FROM python.3.12-slim

RUN pip install --no-cache-dir \
    pandas>=2.3.1 \
    pandera>=0.25.0 \
    pydantic>=2.11.7 \
    pykafka>=2.8.0 \

CMD ["python3", "src/app.py"]