FROM quay.io/mozmar/base
EXPOSE 80
CMD ["nginx"]

RUN apt-get update && \
    apt-get install -y --no-install-recommends nginx

COPY nginx.conf /etc/nginx/nginx.conf
RUN rm -f /usr/share/nginx/html/*
COPY product-details/ /usr/share/nginx/html
