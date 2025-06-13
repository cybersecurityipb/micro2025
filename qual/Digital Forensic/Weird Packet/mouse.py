import re
from PIL import Image

# Step 1: Baca data dari out.txt
def read_out_txt(file_path):
    with open(file_path, "r") as f:
        return f.read().strip().splitlines()

# Step 2: Format menjadi (0xAA, 0xBB, 0xCC)
def process_mouse_data(lines):
    pattern = re.compile(r"^(..)(..)(..)..$")
    events = []
    for line in lines:
        match = pattern.match(line.strip())
        if match:
            a, b, c = match.groups()
            events.append((int(a, 16), int(b, 16), int(c, 16)))
    return events

# Step 3: Gambar berdasarkan mouse events
def draw_mouse_path(mouse_events):
    img = Image.new('RGB', (10000, 10000), color='white')
    canvas = img.load()
    mouse_x = 5000
    mouse_y = 5000
    for data in mouse_events:
        left_button_pressed = data[0] & 0x01
        x_offset = int.from_bytes(bytes([data[1]]), "big", signed=True)
        y_offset = int.from_bytes(bytes([data[2]]), "big", signed=True)
        mouse_x += x_offset
        mouse_y += y_offset
        if left_button_pressed:
            for i in range(5):
                for j in range(5):
                    if 0 <= mouse_x + i < 10000 and 0 <= mouse_y + j < 10000:
                        canvas[mouse_x + i, mouse_y + j] = (0, 0, 0)
    img.save("result.png")
    print("[✔] result.png saved!")

# Main
if __name__ == "__main__":
    lines = read_out_txt("hid.txt")
    mouse_events = process_mouse_data(lines)
    draw_mouse_path(mouse_events)