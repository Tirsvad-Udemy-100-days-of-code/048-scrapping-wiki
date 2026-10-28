# Test i Docker

🌐 [English](Docker-Testing) · **Dansk** · [Bahasa Malaysia](Docker-Testing-ms)

## Hvorfor Docker

Et script, der styrer en browser, åbner vinduer og bruger musens og tastaturets fokus på den maskine, det kører på. For at holde udviklerens skrivebord frit kører end to end-kørslen og skærmbillederne i en Docker-container med headless Chromium. Enhedstest kræver ingen browser og kører på værten.

## Byg og kør

```bash
docker build -t scraping-wiki-e2e .
docker run --rm -v "$(pwd)/results:/results" scraping-wiki-e2e
```

Containeren rapporterer gennem filer i `results/`:

| Fil | Indhold |
| --- | --- |
| `e2e.log` | Det samlede output fra testen og skærmbilledoptagelsen |
| `exit-code.txt` | `0`, når alt bestod |
| `screenshots/` | Én PNG for hvert af lektionens syv trin |

## Hvad der kører

1. `tests/e2e/test_interaction_e2e.py` kører `python -m scraping_wiki.interaction --headless` og kontrollerer, at ét tal udskrives, og at det er mindst en million (artikeltallet, ikke de aktive redaktører).
2. `tests/e2e/capture_screenshots.py` viser koden fra trin 1 til 3 som en editorside, tager rigtige skærmbilleder af Wikipedias forside til trin 4, 5 og 7 og viser det rigtige output i trin 6.

## Hold hemmeligheder ude

Filen `.dockerignore` holder `.env`, `.venv` og `.git` ude af imaget. Projektet læser eller importerer aldrig `.env`-filen.
