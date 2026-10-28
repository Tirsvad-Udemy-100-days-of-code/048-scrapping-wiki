# Scraping Wiki

🌐 [English](Home) · **Dansk** · [Bahasa Malaysia](Home-ms)

Et lille Python-projekt fra Udemys *100 Days of Code: The Complete Python Pro Bootcamp*. Det styrer Chrome med Selenium, åbner Wikipedias forside og udskriver antallet af artikler. Denne wiki forklarer, hvad hvert trin i lektionen lærte os, med et skærmbillede af hvert trin.

| Side | Læs den, når du vil |
| --- | --- |
| [Lektionens trin](Lecture-Steps-da) | Se de syv trin i lektionen, hvert med skærmbillede, kode og det, vi lærte |
| [Opsætning og kørsel](Setup-and-Run-da) | Oprette et lokalt `.venv`, opgradere pip, installere, køre scriptet og køre testene |
| [Test i Docker](Docker-Testing-da) | Forstå, hvorfor browseren kun kører i Docker, og hvordan skærmbillederne laves |

## Kort fortalt

- Python 3.13 eller nyere; `selenium` er den eneste afhængighed ved kørsel.
- Scriptet er `interaction.py`; konstanterne ligger i `constants.py`.
- Enhedstestene starter ingen browser; end to end-kørslen og skærmbillederne kører i en Docker-container.
- Repositoriet: [kildekode og README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-scrapping-wiki).

```bash
python -m scraping_wiki.interaction
```

Udskriften er én linje, for eksempel `7,256,081`.
