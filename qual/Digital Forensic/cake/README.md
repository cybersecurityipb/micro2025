# cake

## Author

asburg

## Categories

Digital Forensic

## Description

man just do your basic forensic stuff, i don't really care

## Attachment(s)

- `chall.png`

## Solver

**Part 1**
- Ketika file dibuka di Apperisolve atau gunakan binwalk akan terdapat sebuah file zip
- Unzip filenya maka akan mendapatkan dua buah file yaitu `README.txt` dan `whatisdis.py`
- Membaca `README.txt` akan memberikan hint untuk langkah selanjutnya

**Part 2**
- Hintnya adalah `Just match all of the bodies with the head` artinya headnya adalah chunk-chunk sebelum IDAT dan bodynya adalah chunk IDAT
- Masing-masing IDAT pada `chall.png` dipasangkan dengan head pada file itu sendiri, sehingga akan terdapat 4 file PNG
- Gabungkan semua file PNG secara berurutan dan visual, maka akan mendapatkan gambar hitam putih yang mana itu adalah biner
- Memahami whatisdis.py akan memberikan hint untuk langkah selanjutnya

**Part 3**
- Dari file `whatisdis.py` akan ditemukan bahwa 1 kotak/bit berwarna hitam/putih mewakili 10x10 pixel
- buat kode untuk mengembalikan supaya 10x10 pixel itu diconvert jadi 0 jika berwarna hitam dan 1 jika berwarna putih
- Jika dilakukan dengan benar maka flagnya pun muncul

## Flag
```
ITFEST25{a1nt_p13c3_0f_c4k3_m4tch1n9_up_4ll_0f_th3_b0dy5_w1th_4_h34d_d4mn1t_15t9}
```
