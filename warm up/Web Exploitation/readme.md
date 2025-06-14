# Inject Me!

## Author

Nikoo

## Categories

Web Exploitation

## Description

Can you help me test my website?

I think it's safe... but maybe you can inject some commands.

Just take it slow cause I'm a bit scared of injections 😅

## Solver

### Langkah 1: Identifikasi Input Field
Identifikasi field input pada website yang dapat menerima user input dan berpotensi vulnerable terhadap command injection.

### Langkah 2: Test Command Injection
Inputkan payload command injection untuk menguji apakah aplikasi vulnerable. Gunakan referensi payload dari berbagai sumber.

### Langkah 3: Directory Listing
Masukkan command berikut untuk melihat daftar file di root directory:

```bash
; ls /
```

### Langkah 4: Read Flag File
Setelah berhasil melihat struktur direktori, masukkan command untuk membaca file flag:

```bash
; cat /flag
```

### Langkah 5: Extract Flag
Flag akan ditampilkan sebagai output dari command injection yang berhasil dieksekusi.

## References

- [Command Injection Payload List](https://github.com/payloadbox/command-injection-payload-list)

## Flag

```
ITFEST25{Command_Injection_Is_Easy_Right??}
```
