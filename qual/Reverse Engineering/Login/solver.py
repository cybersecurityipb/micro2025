#!/usr/bin/env python3

def solve_username():
    """
    Reverse the username transformation
    transform_user_char logic:
    - if index is odd: char + 10
    - if index is even: char ^ 5
    """
    secret_data = [0x4C, 0x5E, 0x43, 0x4F, 0x56, 0x5E, 0x37, 0x3F]
    username = ""
    
    for i in range(8):
        target = secret_data[i]
        if i % 2 == 1:  # odd index
            # target = char + 10, so char = target - 10
            char = target - 10
        else:  # even index
            # target = char ^ 5, so char = target ^ 5
            char = target ^ 5
        username += chr(char)
    
    return username

def solve_password():
    """
    Reverse the password transformation
    transform_pass_char logic based on (index % 4):
    - 0: char - 48 + 10 = char - 38
    - 1: 2 * (char - 48) = 2 * char - 96
    - 2: (char - 48) ^ 7
    - 3: (char - 48) + 20 = char - 28
    """
    pass_matrix = [
        0x2E, 0x84, 0x4E, 0x43, 0x48, 0x00, 0x43, 0x43, 0x4E, 0x3E, 
        0x28, 0x4A, 0x49, 0x84, 0x30, 0x17, 0x4E, 0x5E, 0x4E, 0x14, 
        0x4F, 0x84, 0x28, 0x39, 0x4D, 0x6A, 0x45, 0x52, 0x0E, 0x7A, 
        0x32, 0x43, 0x4A, 0x62, 0x02, 0x19, 0x51, 0x7E, 0x45, 0x48
    ]
    
    password = ""
    
    for i in range(40):
        target = pass_matrix[i]
        mod = i % 4
        
        if mod == 0:
            # target = (char - 48) + 10, so char - 48 = target - 10
            char = target - 10 + 48
        elif mod == 1:
            # target = 2 * (char - 48), so char - 48 = target / 2
            char = (target // 2) + 48
        elif mod == 2:
            # target = (char - 48) ^ 7, so char - 48 = target ^ 7
            char = (target ^ 7) + 48
        elif mod == 3:
            # target = (char - 48) + 20, so char - 48 = target - 20
            char = target - 20 + 48
            
        password += chr(char)
    
    return password

def verify_solution(username, password):
    """Verify our solution matches the original transformation logic"""
    
    # Verify username
    secret_data = [0x4C, 0x5E, 0x43, 0x4F, 0x56, 0x5E, 0x37, 0x3F]
    print("Username verification:")
    for i in range(len(username)):
        char_val = ord(username[i])
        if i % 2 == 1:  # odd
            transformed = char_val + 10
        else:  # even
            transformed = char_val ^ 5
        expected = secret_data[i]
        print(f"  [{i}] '{username[i]}' (0x{char_val:02X}) -> 0x{transformed:02X} == 0x{expected:02X} ? {transformed == expected}")
    
    print("\nPassword verification:")
    pass_matrix = [
        0x2E, 0x84, 0x4E, 0x43, 0x48, 0x00, 0x43, 0x43, 0x4E, 0x3E, 
        0x28, 0x4A, 0x49, 0x84, 0x30, 0x17, 0x4E, 0x5E, 0x4E, 0x14, 
        0x4F, 0x84, 0x28, 0x39, 0x4D, 0x6A, 0x45, 0x52, 0x0E, 0x7A, 
        0x32, 0x43, 0x4A, 0x62, 0x02, 0x19, 0x51, 0x7E, 0x45, 0x48
    ]
    
    for i in range(min(len(password), 40)):
        char_val = ord(password[i])
        v4 = char_val - 48  # This is the transform_pass_char logic
        mod = i % 4
        
        if mod == 0:
            transformed = v4 + 10
        elif mod == 1:
            transformed = 2 * v4
        elif mod == 2:
            transformed = v4 ^ 7
        elif mod == 3:
            transformed = v4 + 20
            
        expected = pass_matrix[i]
        print(f"  [{i}] '{password[i]}' (0x{char_val:02X}) -> 0x{transformed:02X} == 0x{expected:02X} ? {transformed == expected}")

if __name__ == "__main__":
    print("=== CTF Reverse Engineering Solution ===\n")
    
    # Solve for username and password
    username = solve_username()
    password = solve_password()
    
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Username length: {len(username)}")
    print(f"Password length: {len(password)}")
    
    print("\n=== Verification ===")
    verify_solution(username, password)
    
    print(f"\n=== Final Answer ===")
    print(f"Username: {username}")
    print(f"Password: {password}")