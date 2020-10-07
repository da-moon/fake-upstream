FROM gitpod/workspace-full
USER gitpod
SHELL ["/bin/bash", "-c"]
# installing nuitka for static compilation of python apps + some extra tools
RUN export DEBIAN_FRONTEND=noninteractive; \
    wget -O - http://nuitka.net/deb/archive.key.gpg | sudo apt-key add - && \
    echo "deb http://nuitka.net/deb/stable/$(lsb_release -c -s) $(lsb_release -c -s) main" | sudo tee /etc/apt/sources.list.d/nuitka.list && \ 
    sudo apt-get update && \ 
    sudo apt-get -y install nuitka upx
# uninstalling cargo since it takes too much space
RUN yes | /home/gitpod/.cargo/bin/rustup self uninstall && \
    sudo rm /home/gitpod/.bashrc.d/80-rust
#setting up PATH and other env vars
RUN export DEBIAN_FRONTEND=noninteractive; \
    rm -rf "/home/gitpod/.poetry" && \
    rm -rf "/home/gitpod/.local" && \
    mkdir -p "/home/gitpod/.local/bin" && \
    echo 'export PATH="$PATH:/home/gitpod/.poetry/bin"' >> "/home/gitpod/.bashrc" && \
    echo 'export PIP_USER=false' >> "/home/gitpod/.bashrc" && \
    echo 'alias poetry="python3 /home/gitpod/.poetry/bin/poetry"' >> "/home/gitpod/.bash_aliases" 
ENV PATH="$PATH:/home/gitpod/.local/bin:/home/gitpod/.poetry/bin"
# installing poetry. poetry is a python dependancy management software
RUN export DEBIAN_FRONTEND=noninteractive; \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python && \
    python3 "/home/gitpod/.poetry/bin/poetry" --version
# installing updating pip and installing pip packages 
RUN export DEBIAN_FRONTEND=noninteractive; \
    pip3 install dephell[full] && \
    dephell --version
#clean up
RUN export DEBIAN_FRONTEND=noninteractive; \
    sudo apt-get autoclean -y && \ 
    sudo apt-get clean && \
    sudo rm -rf /var/lib/apt/lists/* && \
    sudo rm -rf /tmp/* && \
    sudo rm -rf /home/gitpod/.cache/* && \
    sudo rm -rf /etc/bash_completion.d/rustup*
USER gitpod

