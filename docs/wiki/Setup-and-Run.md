# Setup and Run

🌐 **English** · [Dansk](Setup-and-Run-da) · [Bahasa Malaysia](Setup-and-Run-ms)

## Requirements

- Python 3.13 or newer
- Google Chrome (Selenium downloads the matching driver)
- Optional: Docker, for the end to end run; Doxygen, for the API documentation

## Create and use a local `.venv`

```bash
python -m venv .venv
```

Activate it:

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (Git Bash)
source .venv/Scripts/activate

# Linux / macOS
source .venv/bin/activate
```

Upgrade pip and install the project with the test tools:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Leave the environment with `deactivate`.

## Run

```bash
python -m scraping_wiki.interaction
```

Chrome opens, loads the Wikipedia main page, the article count is printed and the browser closes. Add `--headless` to run without a window:

```bash
scraping-wiki --headless
```

## Tests

```bash
python -m pytest
python -m ruff check src tests
python -m mypy src tests
```

The unit tests use a fake driver and start no browser. For the end to end run see [Docker Testing](Docker-Testing).

## API documentation

```bash
doxygen Doxyfile
```

The HTML is written to `docs/doxygen/html`.
