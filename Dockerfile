FROM python:3.11-slim

WORKDIR /app

RUN pip install pyyaml
RUN touch /app/results.txt

COPY calculator.py .
COPY numbers.txt . 
COPY config.yaml .


ENTRYPOINT [ "python3", "calculator.py"  ]

