#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

KEY_CODES = {
    0x04: ['a', 'A'], 0x05: ['b', 'B'], 0x06: ['c', 'C'], 0x07: ['d', 'D'],
    0x08: ['e', 'E'], 0x09: ['f', 'F'], 0x0A: ['g', 'G'], 0x0B: ['h', 'H'],
    0x0C: ['i', 'I'], 0x0D: ['j', 'J'], 0x0E: ['k', 'K'], 0x0F: ['l', 'L'],
    0x10: ['m', 'M'], 0x11: ['n', 'N'], 0x12: ['o', 'O'], 0x13: ['p', 'P'],
    0x14: ['q', 'Q'], 0x15: ['r', 'R'], 0x16: ['s', 'S'], 0x17: ['t', 'T'],
    0x18: ['u', 'U'], 0x19: ['v', 'V'], 0x1A: ['w', 'W'], 0x1B: ['x', 'X'],
    0x1C: ['y', 'Y'], 0x1D: ['z', 'Z'], 0x1E: ['1', '!'], 0x1F: ['2', '@'],
    0x20: ['3', '#'], 0x21: ['4', '$'], 0x22: ['5', '%'], 0x23: ['6', '^'],
    0x24: ['7', '&'], 0x25: ['8', '*'], 0x26: ['9', '('], 0x27: ['0', ')'],
    0x28: ['\n','\n'], 0x29: ['[ESC]', '[ESC]'], 0x2A: ['[BACKSPACE]', '[BACKSPACE]'],
    0x2B: ['\t','\t'], 0x2C: [' ', ' '], 0x2D: ['-', '_'], 0x2E: ['=', '+'],
    0x2F: ['[', '{'], 0x30: [']', '}'], 0x32: ['#','~'], 0x33: [';', ':'],
    0x34: ["'", '"'], 0x36: [',', '<'], 0x37: ['.', '>'], 0x38: ['/', '?'],
    0x39: ['[CAPSLOCK]','[CAPSLOCK]'], 0x4f: [u'→', u'→'], 0x50: [u'←', u'←'],
    0x51: [u'↓', u'↓'], 0x52: [u'↑', u'↑']
}

def read_use(file):
    with open(file, 'r') as f:
        datas = [line.strip() for line in f if line.strip()]

    cursor_x = 0
    cursor_y = 0
    offset_current_line = 0
    lines = [""]
    output = ''
    skip_next = False

    for data in datas:
        parts = data.split(':')
        if len(parts) < 3:
            continue  # skip if line malformed

        try:
            shift = int(parts[0], 16)
            key = int(parts[2], 16)
            third_byte = int(parts[3], 16)
        except ValueError:
            continue

        if skip_next:
            skip_next = False
            continue

        if key == 0 or third_byte > 0:
            continue

        if shift != 0:
            shift = 1
            skip_next = True

        # Tangani key yang tidak dikenal
        if key not in KEY_CODES:
            print(f'[!] Unknown key code: {key}, skipping...')
            continue

        char = KEY_CODES[key][shift]

        if char == u'↑':
            lines[cursor_y] += output
            output = ''
            cursor_y = max(cursor_y - 1, 0)
        elif char == u'↓':
            lines[cursor_y] += output
            output = ''
            cursor_y += 1
            if cursor_y >= len(lines):
                lines.append("")
        elif char == u'→':
            cursor_x += 1
        elif char == u'←':
            cursor_x = max(cursor_x - 1, 0)
        elif char == '\n':
            lines.append("")
            lines[cursor_y] += output
            cursor_x = 0
            cursor_y += 1
            output = ''
        elif char == '[BACKSPACE]':
            output = output[:-1]
            cursor_x = max(cursor_x - 1, 0)
        else:
            output += char
            cursor_x += 1

    if lines == [""]:
        lines[0] = output
    if output != '' and output not in lines:
        if cursor_y < len(lines):
            lines[cursor_y] += output
        else:
            lines.append(output)

    return '\n'.join(lines)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python sol.py <filename>')
        sys.exit(1)

    output = read_use(sys.argv[1])
    sys.stdout.write(output)
