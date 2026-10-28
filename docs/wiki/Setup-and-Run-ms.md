# Persediaan dan Jalankan

🌐 [English](Setup-and-Run) · [Dansk](Setup-and-Run-da) · **Bahasa Malaysia**

## Keperluan

- Python 3.13 atau lebih baharu
- Google Chrome (Selenium memuat turun pemandu yang sepadan)
- Pilihan: Docker untuk larian end to end; Doxygen untuk dokumentasi API

## Cipta dan guna `.venv` setempat

```bash
python -m venv .venv
```

Aktifkannya:

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (Git Bash)
source .venv/Scripts/activate

# Linux / macOS
source .venv/bin/activate
```

Naik taraf pip dan pasang projek bersama alat ujian:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Keluar daripada persekitaran dengan `deactivate`.

## Jalankan

```bash
python -m scraping_wiki.interaction
```

Chrome dibuka, halaman utama Wikipedia dimuatkan, bilangan artikel dicetak dan pelayar ditutup. Tambah `--headless` untuk berjalan tanpa tetingkap:

```bash
scraping-wiki --headless
```

## Ujian

```bash
python -m pytest
python -m ruff check src tests
python -m mypy src tests
```

Ujian unit menggunakan pemandu palsu dan tidak memulakan pelayar. Untuk larian end to end lihat [Ujian dalam Docker](Docker-Testing-ms).

## Dokumentasi API

```bash
doxygen Doxyfile
```

HTML ditulis ke `docs/doxygen/html`.
