# Langkah Kuliah

🌐 [English](Lecture-Steps) · [Dansk](Lecture-Steps-da) · **Bahasa Malaysia**

Kuliah membina `interaction.py` dalam tujuh langkah. Setiap langkah di bawah mempunyai tangkapan skrinnya, kod selepas langkah itu dan apa yang kita dapat.

## Langkah 1: Cipta `interaction.py`

![Langkah 1: cipta fail](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-scrapping-wiki/raw/branch/main/docs/screenshots/step-1-create-the-file.png)

```python
# interaction.py
```

**Apa yang kita dapat:** tempat untuk skrip. Satu fail kecil dengan satu tujuan lebih mudah dibaca dan dibandingkan dengan penyelesaian orang lain berbanding kod yang bertaburan dalam banyak fail.

## Langkah 2: Import Selenium

![Langkah 2: import Selenium](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-scrapping-wiki/raw/branch/main/docs/screenshots/step-2-import-selenium.png)

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
```

**Apa yang kita dapat:** Selenium ialah pakej yang mengawal pelayar sebenar daripada Python. `webdriver` memulakan dan mengawal pelayar; `By` menyatakan cara mencari elemen (dengan pemilih CSS, id, nama dan sebagainya). Ia pakej pihak ketiga, jadi ia mesti dipasang dahulu dalam `.venv`.

## Langkah 3: Mulakan pemandu Chrome

![Langkah 3: mulakan pemandu Chrome](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-scrapping-wiki/raw/branch/main/docs/screenshots/step-3-initialise-chrome-driver.png)

```python
driver = webdriver.Chrome()
```

**Apa yang kita dapat:** pemandu (driver) ialah objek yang digunakan skrip untuk mengawal Chrome: membuka halaman, mencari elemen dan menutup pelayar. Apabila dicipta, tetingkap pelayar sebenar dibuka. Dalam projek kita ini ialah `create_driver()`, yang juga boleh memulakan Chrome tanpa tetingkap (`--headless`) untuk Docker.

## Langkah 4: Pergi ke Wikipedia dengan `get()`

![Langkah 4: pergi ke halaman dengan get](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-scrapping-wiki/raw/branch/main/docs/screenshots/step-4-navigate-with-get.png)

```python
driver.get("https://en.wikipedia.org/wiki/Main_Page")
```

**Apa yang kita dapat:** `get()` memuatkan URL dan menunggu sehingga halaman siap dimuatkan. URL ialah pemalar (`WIKIPEDIA_MAIN_PAGE_URL` dalam `constants.py`), jadi ia ditulis di satu tempat sahaja. Dalam projek kita ini ialah `open_main_page()`.

## Langkah 5: Kenal pasti elemen HTML

![Langkah 5: kenal pasti elemen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-scrapping-wiki/raw/branch/main/docs/screenshots/step-5-identify-the-element.png)

```python
# The article count is the anchor (a) inside the div whose id is "articlecount":
#     #articlecount a
```

**Apa yang kita dapat:** sebelum mengikis (scraping) data, lihat HTML halaman (alat pembangun pelayar menunjukkannya) dan cari elemen yang boleh dibezakan dengan pasti. Sesuatu `id` adalah unik pada satu halaman, jadi `#articlecount` ialah titik tolak yang baik untuk pemilih CSS, dan `a` memilih pautan di dalamnya.

**Satu pengajaran dari 2026:** Wikipedia kemudian menambah pautan kedua dalam `div` itu. Padanan pertama (merah pada tangkapan skrin) kini ialah bilangan penyunting aktif, dan bilangan artikel (hijau) ialah pautan pertama dalam item senarai kedua: `#articlecount li:nth-of-type(2) a`. Program menggunakan pemilih itu (`ARTICLE_COUNT_SELECTOR`) dan mengekalkan pemilih kuliah sebagai `LECTURE_SELECTOR`. Halaman berubah; pemilih mesti disemak terhadap halaman, dan ujian end to end menyemak bahawa nombor yang dicetak sekurang-kurangnya satu juta.

## Langkah 6: Cari elemen dan cetak teksnya

![Langkah 6: cari elemen dan cetak](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-scrapping-wiki/raw/branch/main/docs/screenshots/step-6-find-element-and-print.png)

```python
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)

driver.quit()
```

**Apa yang kita dapat:** `find_element` mengembalikan elemen pertama yang sepadan dan `.text` memberi teks yang dilihat pelawat. `driver.quit()` menutup pelayar; `main()` kita melakukannya dalam blok `finally` supaya pelayar ditutup walaupun sesuatu gagal. Panel terminal pada tangkapan skrin menunjukkan apa yang dikembalikan oleh pemilih kuliah hari ini dan, di bawahnya, bilangan artikel yang sebenar.

## Langkah 7: Apa yang menyusul

![Langkah 7: interaksi akan datang](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/048-scrapping-wiki/raw/branch/main/docs/screenshots/step-7-future-interactions.png)

```python
# article_count.click()                              # click a link
# search = driver.find_element(By.NAME, "search")    # type into a search field
```

**Apa yang kita dapat:** membaca hanyalah separuh daripadanya. Kuliah seterusnya mengklik pautan dan menaip dalam medan seperti kotak carian (ditandakan pada tangkapan skrin). Dua idea yang sama digunakan: cari elemen dengan pemilih, kemudian bertindak ke atasnya.
