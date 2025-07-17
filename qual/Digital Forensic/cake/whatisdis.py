from PIL import Image

def converter(flag):
    return ''.join(format(ord(c), '08b') for c in flag)

def file(str, w, h, s=10, o='output.png'):
    padded = str.ljust(w * h, '0')
    pixels = [255 if bit == '1' else 0 for bit in padded]
    img = Image.new('L', (w * s, h * s))
    for y in range(h):
        for x in range(w):
            val = pixels[y * w + x]
            for dy in range(s):
                for dx in range(s):
                    img.putpixel((x * s + dx, y * s + dy), val)
    img.save(o)

flag = "[REDACTED]"
cipher = converter(flag)
file(cipher, 27, 24, s=10)
