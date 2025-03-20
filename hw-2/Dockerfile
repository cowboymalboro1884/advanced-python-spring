FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    texlive-latex-base \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-fonts-recommended \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry

WORKDIR /app

COPY external ./external

WORKDIR /app/external

RUN poetry install --no-root

CMD ["poetry", "run", "python", "generate.py"]
