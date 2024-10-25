# syntax=docker/dockerfile:1.9
FROM ubuntu:noble AS build

# The following does not work in Podman unless you build in Docker
# compatibility mode: <https://github.com/containers/podman/issues/8477>
# You can manually prepend every RUN script with `set -ex` too.
SHELL ["sh", "-exc"]

# Security-conscious organizations should package/review uv themselves.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv


COPY . /app
WORKDIR /app

# set up a virtual env to use for whatever app is destined for this container.
RUN uv venv --python 3.12.5 /venv

RUN uv pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]
