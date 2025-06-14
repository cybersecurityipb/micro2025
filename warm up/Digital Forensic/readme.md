# Stego

## Author

Nikoo

## Categories

Digital Forensic

## Description

I hid a secret message in this image file, can you find it?

## Solver

### Langkah 1: Analisis Hex File
Analisis hex file gambar menggunakan hex editor atau command `strings` untuk mencari signature file tersembunyi.

```bash
strings chall.jpg
```

### Langkah 2: Identifikasi File WAV
Temukan strings "WAV" yang merupakan signature dari file WAV yang tersembunyi dalam gambar.

### Langkah 3: Recovery File WAV
Lakukan recovery file WAV dengan mengubah strings "riff" menjadi "RIFF" agar file dapat dikenali dengan benar.

### Langkah 4: Ekstrak File WAV
Ekstrak file WAV menggunakan tools seperti `binwalk` atau `foremost`:

```bash
binwalk -e chall.jpg
# atau
foremost chall.jpg
```

### Langkah 5: Analisis Spectrogram
Analisis spectrogram dari file WAV yang telah diekstrak. Pada spectrogram akan terlihat tulisan "microIPB" yang merupakan password untuk steganografi.

### Langkah 6: Extract Hidden Flag
Gunakan password yang ditemukan untuk mengekstrak flag tersembunyi menggunakan steghide:

```bash
steghide extract -sf chall.jpg -p microIPB
```

### Langkah 7: Baca Flag
Buka file `flag.txt` yang telah diekstrak untuk mendapatkan flag.

## Flag

```
ITFEST25{hmm_apakah_stegano_hanya_ada_di_warmup??}
```
