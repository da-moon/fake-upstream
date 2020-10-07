FROM gitpod/workspace-full
USER gitpod
SHELL ["/bin/bash", "-c"]
# installing nuitka for static compilation of python apps + some extra tools
RUN export DEBIAN_FRONTEND=noninteractive; \
    wget -O - http://nuitka.net/deb/archive.key.gpg | sudo apt-key add - && \
    echo "deb http://nuitka.net/deb/stable/$(lsb_release -c -s) $(lsb_release -c -s) main" | sudo tee /etc/apt/sources.list.d/nuitka.list && \ 
    sudo apt-get update && \ 
    sudo apt-get -y install nuitka upx python-dev python3-dev
# uninstalling cargo since it takes too much space
RUN yes | /home/gitpod/.cargo/bin/rustup self uninstall && \
    sudo rm /home/gitpod/.bashrc.d/80-rust
RUN export DEBIAN_FRONTEND=noninteractive; \
    echo 'export PATH="$PATH:/home/gitpod/.poetry/bin"' >> "/home/gitpod/.bashrc" && \
    echo 'alias poetry="python3 /home/gitpod/.poetry/bin/poetry"' >> "/home/gitpod/.bash_aliases" 

ENV PATH="$PATH:/home/gitpod/.local/bin:/home/gitpod/.poetry/bin"
# installing poetry. poetry is a python dependancy management software
RUN export DEBIAN_FRONTEND=noninteractive; \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 && \
    python3 "/home/gitpod/.poetry/bin/poetry" --version
# installing updating pip and installing pip packages 
# => [NOTE] do not upgrade pip since dephell is not compatible with latest version
RUN export DEBIAN_FRONTEND=noninteractive; \
    pip3 install dephell[full] && \
    dephell --version
RUN export DEBIAN_FRONTEND=noninteractive; \
    pip3 install pyinstaller && \
    pyinstaller -v
RUN export DEBIAN_FRONTEND=noninteractive; \
    pip3 install cython && \
    cython --version
RUN export DEBIAN_FRONTEND=noninteractive; \
    pip3 install pex && \
    pex --version
#clean up
RUN export DEBIAN_FRONTEND=noninteractive; \
    sudo apt-get autoclean -y && \ 
    sudo apt-get clean && \
    sudo rm -rf /var/lib/apt/lists/* && \
    sudo rm -rf /etc/bash_completion.d/rustup*
USER gitpod
