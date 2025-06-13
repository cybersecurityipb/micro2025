def extract_message_from_crc(file_path):
    def from_binary(binary_data):
        byte_array = [int(binary_data[i:i + 8], 2) for i in range(0, len(binary_data), 8)]
        return bytes(byte_array)

    try:
        with open(file_path, 'rb') as file:
            signature = file.read(8)
            if signature != b'\x89PNG\r\n\x1a\n':
                raise ValueError("File is not a valid PNG file.")

            message_bits = []
            chunk_lengths = []
            chunk_types = []

            while True:
                length_bytes = file.read(4)
                if len(length_bytes) < 4:
                    break
                length = int.from_bytes(length_bytes, 'big')
                chunk_type = file.read(4).decode('ascii')
                file.seek(length, 1)  # Skip chunk data
                crc_bytes = file.read(4)
                crc_binary = ''.join(format(byte, '08b') for byte in crc_bytes)
                # Extract LSBs from CRC
                for bit in crc_binary:
                    message_bits.append(bit)
                chunk_lengths.append(length)
                chunk_types.append(chunk_type)
                if chunk_type == 'IEND':
                    break

            # Convert message bits to bytes
            xored_message = from_binary(''.join(message_bits))
            print(f"Extracted XORed message bytes: {list(xored_message)}")
            print(f"Chunk types: {chunk_types}")
            print(f"Chunk lengths used as XOR keys: {chunk_lengths}")

            # Reverse XOR using chunk lengths
            original_message = []
            for i, xored_byte in enumerate(xored_message):
                chunk_index = i // 4  # Each CRC (32 bits) holds 4 chars
                if chunk_index >= len(chunk_lengths):
                    break
                key = chunk_lengths[chunk_index] & 0xFF  # Use least significant 8 bits
                original_byte = xored_byte ^ key
                original_message.append(original_byte)

            # Convert bytes to string, stopping at first invalid character or null byte
            message = ''
            for byte in original_message:
                if 32 <= byte <= 126:  # Printable ASCII range
                    message += chr(byte)
                else:
                    break  # Stop at non-printable or null byte

            return message, chunk_lengths, chunk_types

    except Exception as e:
        print(f"Error: {e}")
        return None, [], []

def main():
    file_path = input("Enter the path to the modified PNG file (e.g., 'output.png'): ")
    message, chunk_lengths, chunk_types = extract_message_from_crc(file_path)
    if message:
        print(f"Recovered message: {message}")
    else:
        print("Failed to extract message. Ensure the file is a valid PNG with embedded data.")

if __name__ == "__main__":
    main()