# Ujian dalam Docker

🌐 [English](Docker-Testing) · [Dansk](Docker-Testing-da) · **Bahasa Malaysia**

## Mengapa Docker

Skrip yang mengawal pelayar membuka tetingkap dan menggunakan fokus tetikus dan papan kekunci mesin tempat ia berjalan. Untuk memastikan desktop pembangun bebas, larian end to end dan tangkapan skrin dijalankan dalam bekas Docker dengan Chromium tanpa kepala (headless). Ujian unit tidak memerlukan pelayar dan dijalankan pada hos.

## Bina dan jalankan

```bash
docker build -t scraping-wiki-e2e .
docker run --rm -v "$(pwd)/results:/results" scraping-wiki-e2e
```

Bekas melaporkan melalui fail dalam `results/`:

| Fail | Kandungan |
| --- | --- |
| `e2e.log` | Output gabungan ujian dan rakaman tangkapan skrin |
| `exit-code.txt` | `0` apabila semuanya lulus |
| `screenshots/` | Satu PNG bagi setiap tujuh langkah kuliah |

## Apa yang dijalankan

1. `tests/e2e/test_interaction_e2e.py` menjalankan `python -m scraping_wiki.interaction --headless` dan menyemak bahawa satu nombor dicetak dan ia sekurang-kurangnya satu juta (bilangan artikel, bukan penyunting aktif).
2. `tests/e2e/capture_screenshots.py` memaparkan kod langkah 1 hingga 3 sebagai halaman penyunting, mengambil tangkapan skrin sebenar halaman utama Wikipedia untuk langkah 4, 5 dan 7, dan menunjukkan output sebenar pada langkah 6.

## Menyimpan rahsia di luar

Fail `.dockerignore` mengekalkan `.env`, `.venv` dan `.git` di luar imej. Projek ini tidak pernah membaca atau mengimport fail `.env`.
