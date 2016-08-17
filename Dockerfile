FROM quay.io/mozmar/base:latest

WORKDIR /app
CMD ["./update-product-details.py"]

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
                    gettext build-essential python3-dev python3-setuptools python3-pip

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY update-product-details.py ./
