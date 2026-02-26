FROM mcr.microsoft.com/devcontainers/python:3.10

RUN apt-get update && apt-get install -y --no-install-recommends \
    texlive-xetex texlive-latex-extra texlive-lang-spanish texlive-science \
    latexmk graphviz build-essential \
  && rm -rf /var/lib/apt/lists/*
