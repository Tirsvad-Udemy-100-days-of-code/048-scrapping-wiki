# Opsætning og kørsel

🌐 [English](Setup-and-Run) · **Dansk** · [Bahasa Malaysia](Setup-and-Run-ms)

## Krav

- Python 3.13 eller nyere
- Google Chrome (Selenium henter den passende driver)
- Valgfrit: Docker til end to end-kørslen; Doxygen til API-dokumentationen

## Opret og brug et lokalt `.venv`

```bash
python -m venv .venv
```

Aktivér det:

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (Git Bash)
source .venv/Scripts/activate

# Linux / macOS
source .venv/bin/activate
```

Opgradér pip og installér projektet med testværktøjerne:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Forlad miljøet med `deactivate`.

## Kør

```bash
python -m scraping_wiki.interaction
```

Chrome åbner, Wikipedias forside indlæses, artikeltallet udskrives, og browseren lukkes. Tilføj `--headless` for at køre uden vindue:

```bash
scraping-wiki --headless
```

## Test

```bash
python -m pytest
python -m ruff check src tests
python -m mypy src tests
```

Enhedstestene bruger en falsk driver og starter ingen browser. End to end-kørslen står under [Test i Docker](Docker-Testing-da).

## API-dokumentation

```bash
doxygen Doxyfile
```

HTML skrives til `docs/doxygen/html`.
