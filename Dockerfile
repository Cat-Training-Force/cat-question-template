FROM python:3.11-alpine
LABEL Author "Nemo Xiong <nemo@anzupop.com>"
# change to tuna
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories
RUN mkdir /chall
# add chall user
RUN addgroup -S chall && adduser -S chall -G chall -h /chall/ -s /bin/bash
# Alpine: make password hash section in shadow not '!'
RUN echo "chall:$(tr -dc A-Za-z0-9 < /dev/urandom | head -c 20)" | chpasswd
# ownership
RUN chown -R chall:chall /chall
# Entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
# switch to chall
USER chall
RUN python -m pip config set global.index-url https://mirror.sjtu.edu.cn/pypi/web/simple
RUN python -m pip install flask flask-cors
USER chall
COPY ./config/answer-hash /chall/answer-hash
COPY ./src/rest-server.py /chall/rest-server.py
COPY ./templates/main.html /chall/templates/main.html
COPY ./static /chall/static
ENTRYPOINT [ "/entrypoint.sh" ]