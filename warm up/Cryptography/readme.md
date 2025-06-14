# Unknown

## Author

Nikoo

## Categories

Cryptography

## Description

Can you help me understand the message from my lecturer?

## Solver

### Langkah 1: Analisis Format Data
Pertama, analisis pesan yang diberikan untuk mengidentifikasi jenis encoding yang digunakan.

### Langkah 2: Decode Base64 Berulang
Lakukan decode base64 secara berulang kali hingga menemukan format flag yang valid dengan prefix `ITFEST25`.

Proses decoding dapat dilakukan menggunakan tools seperti:
- Command line: `echo "encoded_string" | base64 -d`
- Online decoder: CyberChef, base64decode.org
- Script Python untuk automasi decoding berulang

### Langkah 3: Verifikasi Flag
Pastikan hasil decode terakhir menghasilkan flag dengan format yang benar.

## Flag

```
ITFEST25{base64_berulang_ulang_kali}
```
