# Scraping Wiki

🌐 **English** · [Dansk](Home-da) · [Bahasa Malaysia](Home-ms)

A small Python project from Udemy's *100 Days of Code: The Complete Python Pro Bootcamp*. It drives Chrome with Selenium, opens the Wikipedia main page and prints the article count. This wiki explains what each lecture step taught, with a screenshot of each step.

| Page | Read it when you want to |
| --- | --- |
| [Lecture Steps](Lecture-Steps) | See the seven lecture steps, each with its screenshot, its code and what we gained |
| [Setup and Run](Setup-and-Run) | Create a local `.venv`, upgrade pip, install, run the script and run the tests |
| [Docker Testing](Docker-Testing) | Understand why the browser runs only in Docker, and how the screenshots are made |

## At a glance

- Python 3.13 or newer; `selenium` is the only runtime dependency.
- The script is `interaction.py`; the constants are in `constants.py`.
- Unit tests start no browser; the end to end run and the screenshots run in a Docker container.
- The repository: [source and README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-scrapping-wiki).

```bash
python -m scraping_wiki.interaction
```

The output is one line, for example `7,256,081`.
