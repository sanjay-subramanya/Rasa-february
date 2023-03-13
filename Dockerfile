FROM python:3.8 AS BASE

RUN apt-get update \
    && apt-get --assume-yes --no-install-recommends install \
        build-essential \
        curl \
        git \
        jq \
        libgomp1 \
        vim

WORKDIR /app

COPY gpt-grammar.py ./

EXPOSE 5000

RUN pip install openai
RUN pip install flask

CMD ["python", "./gpt-grammar.py"]