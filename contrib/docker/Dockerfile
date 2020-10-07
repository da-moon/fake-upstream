[200~# multistage build for bifrost
# eg. build command
# docker build \
#        --build-arg GITHUB_REPOSITORY=$GITHUB_REPOSITORY \
#        --build-arg GITHUB_REPOSITORY_OWNER=$GITHUB_REPOSITORY_OWNER \
#        --build-arg GITHUB_ACTOR=$GITHUB_ACTOR \
#        --build-arg GITHUB_TOKEN=$GITHUB_TOKEN \
#        -t da-moon/upstream-gen:latest .

FROM python:alpine as base

ARG GITHUB_REPOSITORY_OWNER
ENV GITHUB_REPOSITORY_OWNER $GITHUB_REPOSITORY_OWNER

ARG GITHUB_REPOSITORY
ENV GITHUB_REPOSITORY $GITHUB_REPOSITORY

ARG GITHUB_ACTOR
ENV GITHUB_ACTOR $GITHUB_ACTOR

ARG GITHUB_TOKEN
ENV GITHUB_TOKEN $GITHUB_TOKEN
ENV TERM=xterm
ENV PIP_USER=false
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" > /etc/apk/repositories && \
    echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && \
    echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
	  apk upgrade -U -a && \
	  apk add build-base make git bash ncurses curl
		RUN mkdir -p "/workspace" && \
        mkdir -p "~/.local/bin" && \
        mkdir -p "~/.poetry/bin"
    RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
		RUN git clone "https://$GITHUB_ACTOR:$GITHUB_TOKEN@github.com/da-moon/upstream-gen.git" "/workspace/upstream-gen"
    WORKDIR /workspace/upstream-gen
    RUN mkdir -p dist && \
        make init && \
        make requirements.txt 
    RUN pex \
          --requirement=requirements.txt \
          --script=upstream-gen \
          --sources-directory=./upstream_gen \
          --output-file=./dist/upstream-gen.pex
		RUN echo "nobody:x:65534:65534:Nobody:/:" > /etc_passwd
		FROM python:alpine
		COPY --from=base /etc_passwd /etc/passwd
		COPY --from=base --chown=65534:0 /workspace/upstream-gen.pex /upstream-gen.pex
		USER nobody
		ENTRYPOINT ["/upstream-gen.pex","main:main"]
