# Exe

## Author

Nikoo

## Categories

Reverse Engineering

## Description

Let's learn and warm up basic reverse engineering first

## Solver

### Langkah 1: Extract PyInstaller Executable
Gunakan PyInstaller Extractor untuk mengekstrak source code dari file executable yang dikompilasi dengan PyInstaller:

**Tool:** [pyinstxtractor](https://github.com/extremecoders-re/pyinstxtractor)

```bash
python pyinstxtractor.py target.exe
```

### Langkah 2: Decompile PYC Files
Setelah ekstraksi berhasil, decompile file `.pyc` yang dihasilkan menjadi file Python readable menggunakan salah satu tools berikut:

**Option 1:** Online Decompiler - [PyLingual.io](https://pylingual.io/)

**Option 2:** Offline Decompiler - [pycdc.exe](https://github.com/extremecoders-re/decompyle-builds/releases/download/build-16-Oct-2024-5e1c403/pycdc.exe)

```bash
pycdc.exe target.pyc > decompiled.py
```

### Langkah 3: Analisis Source Code
Analisis kode Python yang telah di-decompile untuk memahami logika program dan algoritma yang digunakan.

### Langkah 4: Develop Solver Script
Buat script Python `solver.py` berdasarkan analisis kode untuk mendapatkan flag yang diinginkan.

## Tools References

- [PyInstaller Extractor](https://github.com/extremecoders-re/pyinstxtractor)
- [PyLingual Online Decompiler](https://pylingual.io/)
- [PyCDC Offline Decompiler](https://github.com/extremecoders-re/decompyle-builds/releases/download/build-16-Oct-2024-5e1c403/pycdc.exe)

## Flag

```
ITFEST25{Tetap_Ilmu_Padi_Abangkuhh}
```
