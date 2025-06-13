# Keylogger

## Author

Nikoo

## Categories

Digital Forensic

## Description

Hmm, this looks weird! This PCAP file contains data from a strange device. Each packet is hiding something. Take a look, troubleshoot, and find out.

## Solver

### Langkah 1: Ekstrak Data HID Mouse
Ambil data HID mouse dengan command tshark dan simpan dalam file hid.txt sebagai berikut:
```bash
tshark -r done_hid_usb.pcap -Y 'frame.len == 68 && usb.transfer_type == 0x01 && usb.endpoint_address.direction == "IN"' -T fields -e usb.capdata > hid.txt
```

Setelah itu visualisasikan dengan mouse.py maka muncul flag part bagian 2: `mouse_ngasih_click_keputusan}`

**Reference mouse.py:** [https://res260.medium.com/usb-pcap-forensics-graphics-tablet-nsec-ctf-2021-writeup-part-2-3-9c6265ca4c40](https://res260.medium.com/usb-pcap-forensics-graphics-tablet-nsec-ctf-2021-writeup-part-2-3-9c6265ca4c40)

### Langkah 2: Ekstrak Data HID Keyboard
Ambil data HID keyboard dengan command tshark dan simpan dalam file out.txt sebagai berikut:
```bash
tshark -r done_hid_usb.pcap -Y 'frame.len == 72 && usb.transfer_type == 0x01 && usb.endpoint_address.direction == "IN"' -T fields -e usb.capdata | sed 's/../:&/g2' > out.txt
```

Setelah itu visualisasikan dengan keyboard.py maka muncul flag part bagian 1: `ITFEST25{keyboard_ngasih_clue_kehidupan_`

**Reference keyboard.py:** [https://github.com/TeamRocketIst/ctf-usb-keyboard-parser](https://github.com/TeamRocketIst/ctf-usb-keyboard-parser)

## Flag

```
ITFEST25{keyboard_ngasih_clue_kehidupan_mouse_ngasih_click_keputusan}
```
