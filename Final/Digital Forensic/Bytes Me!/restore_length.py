import struct
import zlib
import sys

def restore_idat_length(file_path, output_path):
    """
    Restore IDAT chunks from length 0 back to length 8192,
    but only change the length field - don't try to recalculate CRC
    since the actual data structure has changed.
    """
    with open(file_path, 'rb') as f:
        data = bytearray(f.read())
    
    png_header = b'\x89PNG\r\n\x1a\n'
    if not data.startswith(png_header):
        print("Not a PNG file.")
        return False
    
    offset = len(png_header)
    target_length = 0x00000000  # Looking for length 0
    restored_length = 0x00002000  # Restore to 8192
    modifications_made = 0
    
    print(f"Scanning file: {file_path}")
    print(f"Looking for IDAT chunks with length 0x{target_length:08X}")
    print("-" * 60)
    
    while offset + 12 <= len(data):
        try:
            # Read chunk length and type
            chunk_length = struct.unpack(">I", data[offset:offset+4])[0]
            chunk_type = data[offset+4:offset+8]
            
            if chunk_type == b'IDAT' and chunk_length == target_length:
                print(f"Found IDAT with length 0x{chunk_length:08X} at offset 0x{offset:08X}")
                
                # Show current bytes
                current_bytes = data[offset:offset+4]
                print(f"Current bytes: {' '.join(f'{b:02X}' for b in current_bytes)}")
                
                # Replace length field only
                data[offset:offset+4] = struct.pack(">I", restored_length)
                modifications_made += 1
                
                # Show new bytes
                new_bytes = data[offset:offset+4]
                print(f"New bytes:     {' '.join(f'{b:02X}' for b in new_bytes)}")
                print(f"✓ Length restored to 0x{restored_length:08X}")
                print()
                
            # Move to next chunk
            offset += 8 + chunk_length + 4
            
        except struct.error as e:
            print(f"Error reading chunk at offset 0x{offset:08X}: {e}")
            break
        except Exception as e:
            print(f"Unexpected error at offset 0x{offset:08X}: {e}")
            break
    
    if modifications_made > 0:
        # Write the modified file
        with open(output_path, 'wb') as f:
            f.write(data)
        print(f"✓ File successfully restored: {output_path}")
        print(f"✓ Modified {modifications_made} IDAT chunk(s)")
        return True
    else:
        print("No IDAT chunks with length 0x00000000 found.")
        return False

def verify_restoration(file_path):
    """Verify the restoration by showing IDAT chunks"""
    print(f"\nVerifying file: {file_path}")
    print("-" * 40)
    
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return
    
    png_header = b'\x89PNG\r\n\x1a\n'
    if not data.startswith(png_header):
        print("Not a PNG file.")
        return
    
    offset = len(png_header)
    idat_count = 0
    
    while offset + 12 <= len(data):
        try:
            chunk_length = struct.unpack(">I", data[offset:offset+4])[0]
            chunk_type = data[offset+4:offset+8]
            
            if chunk_type == b'IDAT':
                idat_count += 1
                length_bytes = data[offset:offset+4]
                length_hex = ' '.join(f'{b:02X}' for b in length_bytes)
                print(f"IDAT {idat_count}: offset=0x{offset:08X}, length={chunk_length}, hex=[{length_hex}]")
            
            offset += 8 + chunk_length + 4
            
        except struct.error:
            break
        except Exception:
            break
    
    if idat_count == 0:
        print("No IDAT chunks found.")

def main():
    if len(sys.argv) != 3:
        print("Usage: python restore_idat.py <input_file> <output_file>")
        print("Example: python restore_idat.py patched.png restored.png")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    print("IDAT Length Restorer")
    print("=" * 60)
    print(f"Input file:  {input_file}")
    print(f"Output file: {output_file}")
    print()
    
    # Verify input file before restoration
    verify_restoration(input_file)
    
    # Perform restoration
    success = restore_idat_length(input_file, output_file)
    
    if success:
        # Verify output file after restoration
        verify_restoration(output_file)
    
    print("\nOperation completed.")

if __name__ == "__main__":
    main()