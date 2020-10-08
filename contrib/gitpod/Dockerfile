FROM gitpod/workspace-full
USER gitpod
SHELL ["/bin/bash", "-c"]
# installing nuitka/bazel for static compilation of python apps + some extra tools
RUN export DEBIAN_FRONTEND=noninteractive; \
    curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor > bazel.gpg && \
    sudo mv bazel.gpg /etc/apt/trusted.gpg.d/ && \
    wget -O - http://nuitka.net/deb/archive.key.gpg | sudo apt-key add - && \
    echo "deb http://nuitka.net/deb/stable/$(lsb_release -c -s) $(lsb_release -c -s) main" | sudo tee /etc/apt/sources.list.d/nuitka.list && \ 
    echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list && \
    sudo apt-get update && \ 
    sudo apt-get -y install nuitka upx python-dev python3-dev bazel

RUN export DEBIAN_FRONTEND=noninteractive; \
    echo 'export PATH="$PATH:/home/gitpod/.poetry/bin"' >> "/home/gitpod/.bashrc" && \
    echo 'alias poetry="python3 /home/gitpod/.poetry/bin/poetry"' >> "/home/gitpod/.bash_aliases" 
# pyenv setup
RUN export DEBIAN_FRONTEND=noninteractive; \
    pyenv uninstall 3.8.6 && \
    pyenv install 3.7.7 && \
    pyenv global 3.7.7 2.7.18 && \
    python2 -m pip install --upgrade pip && \
    python3 -m pip install --upgrade pip && \
    python3 -m pip install --upgrade \
        setuptools wheel virtualenv pipenv pylint rope flake8 \
        mypy autopep8 pep8 pylama pydocstyle bandit notebook \
        twine \
    && sudo rm -rf /tmp/*

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
# installing pyoxidizer
RUN /home/gitpod/.cargo/bin/cargo install pyoxidizer && \
    pyoxidizer --version
#clean up
RUN export DEBIAN_FRONTEND=noninteractive; \
    sudo apt-get autoclean -y && \ 
    sudo apt-get clean && \
    sudo rm -rf /var/lib/apt/lists/* 
USER gitpod
