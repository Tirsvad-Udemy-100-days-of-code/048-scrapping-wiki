# End to end run of the Wikipedia scraper in headless Chromium, and the screenshots of the
# lecture steps. Build and run: see "Tests" in README.md.
FROM python:3.13-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    CHROME_BINARY=/usr/bin/chromium \
    CHROMEDRIVER_PATH=/usr/bin/chromedriver

RUN apt-get update \
    && apt-get install -y --no-install-recommends chromium chromium-driver fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

RUN useradd --create-home --shell /bin/bash runner
WORKDIR /app
COPY --chown=runner:runner . /app
RUN python -m pip install --upgrade pip \
    && python -m pip install ".[dev]"

RUN mkdir /results && chown runner:runner /results
USER runner
VOLUME ["/results"]

CMD ["bash", "tests/e2e/run_e2e.sh", "/results"]
