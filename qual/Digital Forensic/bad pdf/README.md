# bad-pdf

## Author

k1nomi

## Categories

Digital Forensic

## Description

I just downloaded a paper for my AI research, but it looks suspicious. Can you check if it is malicious or not for me?

## Attachment(s)

- `paper.pdf`

## Solver

**Part 1**

- Jika dibuka di browser, atau cek lewat `exiftool`, tampak bahwa file PDF ini memiliki title berupa text base64 yang sangat panjang
- Jika text base64 tersebut di-decode, maka akan menjadi kode JavaScript yang di-obfuscate
- Deobfuscate menggunakan [obf-io.deobfuscate.io](https://obf-io.deobfuscate.io/) dan jalankan kodenya
- Didapatkan string `[Part 1: ITFEST25{b3_c4r3ful_wh3n] [Part 2 Hint: JS, huh? Why put a lot of trouble putting it on the document title when you can embed it directly on the PDF?]`

**Part 2**

- Gunakan `pdf-parser` untuk menganalisis PDF. Tool tersebut dapat diunduh [di sini](https://blog.didierstevens.com/programs/pdf-tools/). Menggunakan tool PDF lain juga bisa.
- Jalankan command `python3 pdf-parser.py paper.pdf` dan `python3 pdf-parser.py paper.pdf --stats` untuk melihat struktur PDF serta memeriksa adanya object "JavaScript" yang ter-embed di dalam PDF
- Ikuti alur objectnya. Didapatkan bahwa JavaScript ada di object No. 1, yang me-reference object No. 4. Pada object No. 4, terdapat object stream.
- Kita bisa mengekstrak isi stream dengan command `python3 pdf-parser.py paper.pdf --object 4 -f`
- Sebuah kode JS yang obfuscated pun lagi-lagi didapatkan.
- Dari kode ini, kita mendapatkan string `[Part 2: _d0wnl0ad1ng_PDFs_n3xt_t] [Part 3 Hint: Isn't it unusual for this document to have no images? Again, maybe it's embedded?]`

**Part 3**

- Hint pada Part 2 merujuk pada "EmbeddedFile" yang mungkin ada pada PDF. 
- Menjalankan command `python3 pdf-parser.py paper.pdf --stats`, dapat diketahui bahwa EmbeddedFile terdapat di dalam objek No. 3
- Maka dari itu, bisa kita ekstrak dengan command `python3 pdf-parser.py paper.pdf --object 3 -f`
- Dari sini, kita mendapatkan teks base64 yang sangat panjang. Jika di-decode, hasilnya adalah sebuah gambar. Dari gambar tersebut, kita mendapatkan string `[Part 3: im3_it_m1ght_b3_malwar3}] [You got it all, Congrats!!! :D]`

## Flag

```
ITFEST25{b3_c4r3ful_wh3n_d0wnl0ad1ng_PDFs_n3xt_tim3_it_m1ght_b3_malwar3}
```
