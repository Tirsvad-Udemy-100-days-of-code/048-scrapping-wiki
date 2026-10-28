# Docker Testing

🌐 **English** · [Dansk](Docker-Testing-da) · [Bahasa Malaysia](Docker-Testing-ms)

## Why Docker

A script that drives a browser opens windows and uses the mouse and keyboard focus of the machine it runs on. To keep the developer's desktop free, the end to end run and the screenshots run in a Docker container with headless Chromium. Unit tests need no browser and run on the host.

## Build and run

```bash
docker build -t scraping-wiki-e2e .
docker run --rm -v "$(pwd)/results:/results" scraping-wiki-e2e
```

The container reports through files in `results/`:

| File | Content |
| --- | --- |
| `e2e.log` | The combined output of the test and the screenshot capture |
| `exit-code.txt` | `0` when everything passed |
| `screenshots/` | One PNG for each of the seven lecture steps |

## What runs

1. `tests/e2e/test_interaction_e2e.py` runs `python -m scraping_wiki.interaction --headless` and checks that one number is printed and that it is at least one million (the article count, not the active editors).
2. `tests/e2e/capture_screenshots.py` renders the code of steps 1 to 3 as an editor page, takes real screenshots of the Wikipedia main page for steps 4, 5 and 7, and shows the real output in step 6.

## Keeping secrets out

The `.dockerignore` file keeps `.env`, `.venv` and `.git` out of the image. The project never reads or imports the `.env` file.
