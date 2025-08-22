# maelstrom

## Author

k1nomi

## Categories

Digital Forensic

## Description

John has captured a stream of confidential information and mailed it to his colleague... But that's as far as we know.

## Attachment(s)

- `maelstrom.pcapng`

## Solver

### 1. Analisis `maelstrom.pcapng` & Dekripsi Packet

Amati bahwa pada file capture, terdapat komunikasi SMTP antara John dan Mark. Sebagian packet berupa plaintext dan sebagian lainnya terenkripsi. Dari komunikasi yang tidak terenkripsi, kita mendapatkan sebuah public key RSA dan cara untuk mengenkripsi packet-packet lainnya. Dapat diketahui dari nilai `n` dan `e` nya bahwa public key pemberian John vulnerable terhadap Wiener attack. Maka dari itu, kita bisa memanfaatkan solver yang sudah dibuat pada soal qual `loser` untuk mendapatkan key AES yang digunakan.

```py
from Crypto.PublicKey import RSA
from Crypto.Util.number import *
from sage.all import *

# Load PEM file
with open("public_key.pem", "rb") as f:
    key = RSA.import_key(f.read())

n = key.n
e = key.e
c = 11572827139702219033043035156209321984649043642687945489684374639144134855239045455401365840335200319431397265510247847879366431001310282534181991867887006730414349464855348037462461686586131560893810921430475809676596608373928296023798346933224140510024488550824927633381142868145643454788744736355735531314162711739291327892715385882031310818076132068084018139626670727270122198151099370618059178823978999684348061857252978029799538241107391344123608586172254132992845845965216660982833551027542326829425336789327127330646599960659747127432752591231847665640700385594193573057036900001180936013113371595072363969803

# Solver dari soal qual 'loser' [https://github.com/cybersecurityipb/micro2025/blob/main/qual/Cryptography/loser/solver.sage]
def wiener(n, e):
    n = Integer(n)
    e = Integer(e)
    for f in (e / n).continued_fraction().convergents()[1:]:
        k, d = f.numerator(), f.denominator()
        if d == 0 or (e * d - 1) % k != 0:
            continue
        phi = (e * d - 1) // k
        b = -(n - phi + 1)
        discr = b * b - 4 * n
        if discr >= 0:
            sqrt_discr = sqrt(discr)
            if sqrt_discr.is_integer():
                p = (-b + sqrt_discr) // 2
                q = (-b - sqrt_discr) // 2
                if p * q == n:
                    return (p, q, d)
    return (None, None, None)

p, q, d = wiener(n, e)

if d:
    m = pow(c,d,n)
    print(long_to_bytes(m)) 

'''
Key in hex: 7f969cb91bf7b1a103dc544982dff07e
'''
```

Berikutnya, key tersebut digunakan untuk mendekripsi pesan pada packet-packet lainnya.

```py
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

enc_messages = ['77fe6c0e51dcd60409cae008df37618dece2acbd78a0f863fc83f4e5d9fea94d7478ad1b539edbd8f733332d73ad6de178d27f9dbe9c38238faa9a10d82ce8351fa96c6081821e5176373e5488305d0d3671dfa332958454f792f681cc732620639da36c06d653b8806eb1f38e6a8ec3', '06a36908fc4e09d1b6f9d393a3ca6249976f357ea3b46b37027e97b92720d8fd26bef463e8a35d07b6b79ea3b28e506ddc68100529a3efc056e342ad688ce49ddbe8d03a6bb2249343bceec636e1a0780e8f502894c4cc483f322eabbcb5f05b6377096d4d0b74c476a582e0dc135797', '0e0695f59aab63afb98b1804721ea369ed803a04faad911132b5feb43067273a5247105684a95d13437e320761f719fca8be4a3070c524ba4e6f06e1fb80e898', '1e0a86c6140d02402691e3f4d0169000ac2bba69600816ef8cfefc7a541653d7d69d59e53334f713a14635b51a0667beb69c29ecaa84066c6729f9af0d3119aeb9e7c18be1e682081ad53e00b76713bd3a183cd8594a47c943ea464602a53603']
enc_attachments = ['secret.png.enc', 'secret.zip.enc']

# AES decryption setup (AES-128, CBC, IV in first block)
KEY = bytes.fromhex('7f969cb91bf7b1a103dc544982dff07e')
def decrypt(msg, key):
    ct = bytes.fromhex(msg)
    iv = ct[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ct[16:]), 16)
    return plaintext

# Decrypting messages
for enc_msg in enc_messages:
    print(decrypt(enc_msg, KEY))

'''
b"Can you read my message? Please reply with a cat picture so that I know it's you."
b"Here's your desired cat picture. Now, can we go back to the stream you captured?"
b'Of course! Here is the file in zip.'
b"Thank you for the valuable lead. I'll see you tomorrow in office."
'''

# Decrypting Attachments
for enc_att in enc_attachments:
    hex_ct = open("attachments/" + enc_att, "r").read()
    plain_att = decrypt(hex_ct, KEY)
    out_file = open("attachments/" + enc_att[:-4], "wb")
    out_file.write(plain_att)
    print(f"Decrypted {enc_att} and saved as {"attachments/" + enc_att[:-4]}")

'''
Decrypted secret.png.enc and saved as attachments/secret.png
Decrypted secret.zip.enc and saved as attachments/secret.zip
'''
```

### 2. Analisis `secret.pcapng`

Setelah melakukan dekripsi pada sisa packet, kita mendapatkan dua attachment, yakni `secret.png` dan `secret.pcapng` (didapatkan dari `secret.zip`). Dari konteks komunikasinya, jelas bahwa `secret.png` tidak ada hubungannya dengan apa yang ingin kita cari, yakni "stream of confidential information". Maka dari itu, langsung saja lakukan analisis pada `secret.pcapng`.

Karena jelas bahwa file ini berisikan packet-packet dari sebuah streaming, maka protokol yang paling umum untuk digunakan adalah RTP/RTSP. Kita bisa konfigurasi Wireshark untuk mendeteksi protokol ini melalui opsi "Edit >> Preferences >> Protocol >> RTSP". Packet-packet awal RTSP menunjukkan bahwa data streaming di-encode menggunakan encoding video "H264". Maka dari itu, langkah paling logis yang bisa kita lakukan adalah mengekstraksi data H264 yang ada dan memainkan videonya.

### 3. Ekstrak data H264 dari pcapng

Setelah melakukan sediki riset, dapat ditemukan bahwa data H264 bisa diekstrak dari Wireshark dengan mudah menggunakan plugin https://github.com/volvet/h264extractor/tree/master. Setelah melakukan instalasi dan mengonfigurasi protokol H264 lewat "Edit >> Preferences >> Protocol >> H264", kita bisa ekstrak datanya dan akan didapatkan sebuah file dengan ekstensi `.264`.

Berikutnya, file tersebut dapat dikonversi menggunakan `ffmpeg` ataupun tool online seperti https://video-converter.com/.

```
$ ffmpeg -i video_2025mmdd-hhmmss.264 -c:v copy output.mp4
```

### 4. Ekstrak frame dari video

Pada video, flagnya berupa frame-frame yang diputar secara cepat, di mana 1 frame berarti satu huruf. Untuk tahap ini sederhana saja. Frame bisa diekstrak baik menggunakan script Python maupun `ffmpeg`.

```py
import cv2
import os

def extract_frames(video_path, output_dir="frames/"):
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break  # no more frames

        filename = os.path.join(output_dir, f"frame_{frame_count:05d}.png")
        cv2.imwrite(filename, frame)
        frame_count += 1

    cap.release()
    print(f"Extracted {frame_count} frames to '{output_dir}'")

# Extract frames
extract_frames("output.mp4")
```

Ketika dibaca, maka akan terbentuk kalimat berikut.

```
Thank you for tuning in. Here is your flag: ITFEST25{smtp_and_rtsp_network_analysis}. Congratzzz!
```

## Flag

```
ITFEST25{smtp_and_rtsp_network_analysis}
```
