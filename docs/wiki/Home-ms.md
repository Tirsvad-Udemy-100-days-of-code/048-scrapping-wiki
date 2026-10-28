# Scraping Wiki

🌐 [English](Home) · [Dansk](Home-da) · **Bahasa Malaysia**

Projek Python kecil daripada kursus Udemy *100 Days of Code: The Complete Python Pro Bootcamp*. Ia mengawal Chrome dengan Selenium, membuka halaman utama Wikipedia dan mencetak bilangan artikel. Wiki ini menerangkan apa yang dipelajari pada setiap langkah kuliah, dengan tangkapan skrin bagi setiap langkah.

| Halaman | Baca apabila anda mahu |
| --- | --- |
| [Langkah Kuliah](Lecture-Steps-ms) | Melihat tujuh langkah kuliah, setiap satu dengan tangkapan skrin, kod dan apa yang kita dapat |
| [Persediaan dan Jalankan](Setup-and-Run-ms) | Mencipta `.venv` setempat, menaik taraf pip, memasang, menjalankan skrip dan menjalankan ujian |
| [Ujian dalam Docker](Docker-Testing-ms) | Memahami mengapa pelayar hanya dijalankan dalam Docker dan bagaimana tangkapan skrin dibuat |

## Sepintas lalu

- Python 3.13 atau lebih baharu; `selenium` ialah satu-satunya kebergantungan semasa larian.
- Skripnya ialah `interaction.py`; pemalar berada dalam `constants.py`.
- Ujian unit tidak memulakan pelayar; larian end to end dan tangkapan skrin dijalankan dalam bekas Docker.
- Repositori: [kod sumber dan README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-scrapping-wiki).

```bash
python -m scraping_wiki.interaction
```

Outputnya satu baris, contohnya `7,256,081`.
