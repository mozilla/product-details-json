FROM quay.io/mozmar/base:latest

# Set Python-related environment variables to reduce annoying-ness
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV LANG C.UTF-8

WORKDIR /app
CMD ["./update-product-details.py"]

RUN update-alternatives --install /bin/sh sh /bin/bash 10

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
                    gettext build-essential python3-{dev,setuptools,pip} && \
    rm -rf /var/lib/apt/lists/*

RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 10
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 10

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY update-product-details.py ./
