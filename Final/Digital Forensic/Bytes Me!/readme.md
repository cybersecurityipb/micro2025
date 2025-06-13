# Bytes Me!

## Author

Nikoo

## Categories

Digital Forensic

## Description

I was experimenting with a new steganography technique using Python. To be safe, I saved my code as a screenshot. But strangely, the image file can no longer be opened.

As if something is hidden… or maybe too visible?

Figure out what happened — and uncover the technique I was learning.

## Solver

### Langkah 1: Recovery PNG Structure
Lakukan recovery untuk semua length dan CRC32 pada struktur PNG yang rusak terlebih dahulu.

**Note khusus:** Untuk chunk IDAT dengan panjang 8192 bytes, dapat menggunakan automasi script Python `restore_length.py` untuk mempermudah proses recovery.

### Langkah 2: Analisis Script Python
Setelah file PNG berhasil diperbaiki dan dapat dibuka, akan terlihat screenshot script Python yang menunjukkan teknik steganografi menggunakan metode LSB (Least Significant Bit).

### Langkah 3: Extract Hidden Message
Terakhir, extract pesan tersembunyi menggunakan script Python `extract_lsb.py` berdasarkan teknik LSB yang ditemukan pada screenshot.

## References

- [PNG Structure Specification](https://www.libpng.org/pub/png/spec/1.2/PNG-Structure.html)
- [PNG Structure for Beginner](https://medium.com/@0xwan/png-structure-for-beginner-8363ce2a9f73)
- [PNG - Wikipedia](https://en.wikipedia.org/wiki/PNG)

## Flag

```
ITFEST25{L5b_Pi3nji_W1th_X0r_Len9th_CRC32}
```
