# Login

## Author

Nikoo

## Categories

Reverse Engineering

## Description

I could've sworn I just logged in yesterday… but now I've forgotten again 😅

Can you help me get my credentials back?

## Solver

### Langkah 1: Decompile ELF File
Lakukan decompile terhadap file ELF yang diberikan menggunakan tools reverse engineering seperti Ghidra, IDA Pro, atau radare2.

### Langkah 2: Analisis Function
Analisis setiap fungsi yang ada dalam binary untuk memahami algoritma autentikasi dan mekanisme validasi username/password.

### Langkah 3: Reverse Engineering
Lakukan reverse engineering terhadap algoritma yang ditemukan. Proses ini dapat dipermudah dengan menggunakan script Python `solver.py` untuk mengotomatisasi proses reversing.

### Langkah 4: Extract Credentials
Setelah berhasil melakukan reverse engineering, ditemukan kredensial sebagai berikut:

**Username:** `ITFEST25`  
**Password:** `Try_n0t_tO_forg3t_y0ur_Usern4me_pa55word`

## Flag

```
ITFEST25{Try_n0t_tO_forg3t_y0ur_Usern4me_pa55word}
```
