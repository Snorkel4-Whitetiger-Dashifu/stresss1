FROM public.ecr.aws/docker/library/python:3.13-slim-bookworm@sha256:01f42367a0a94ad4bc17111776fd66e3500c1d87c15bbd6055b7371d39c124fb

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        tmux \
        asciinema \
    && rm -rf /var/lib/apt/lists/*

# Test-only dependencies are installed at image build time (pinned, no network at verifier runtime).
RUN python3 -m pip install --no-cache-dir \
    iniconfig==2.3.0 \
    packaging==26.2 \
    pluggy==1.6.0 \
    Pygments==2.20.0 \
    pytest==8.4.1 \
    pytest-json-ctrf==0.3.5

WORKDIR /app

COPY app/ /app/
RUN cp /app/workflow/export_report.py /app/workflow/.export_report.original \
    && chmod a-w /app/workflow/.export_report.original
