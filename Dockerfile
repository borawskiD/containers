FROM ubuntu:22.04
RUN apt-get update && apt-get install -y curl
COPY script.sh /usr/local/bin/script.sh
RUN chmod +x /usr/local/bin/script.sh
CMD ["bash", "/usr/local/bin/script.sh"]

