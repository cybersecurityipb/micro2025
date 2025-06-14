def get_secret():
    return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_'

def solve_flag():
    secret = get_secret()
    print("Secret string:", secret)
    print("Secret length:", len(secret))
    print()
    
    # Initialize flag array
    flag = [''] * 35
    
    # Solve each constraint
    # flag[0] != secret[34] and flag[15] != secret[34] -> both must equal secret[34]
    flag[0] = flag[15] = secret[34]  # '{'
    
    # flag[1] != secret[45] and flag[5] != secret[45] and flag[9] != secret[45] -> all must equal secret[45]
    flag[1] = flag[5] = flag[9] = secret[45]  # 'T'
    
    # Individual character constraints
    flag[2] = secret[31]   # 'F'
    flag[3] = secret[30]   # 'E'
    flag[4] = secret[44]   # 'S'
    flag[6] = secret[54]   # '2'
    flag[7] = secret[57]   # '5'
    flag[8] = secret[62]   # '_'
    flag[10] = secret[4]   # 'e'
    flag[11] = secret[19]  # 't'
    
    # flag[12] != secret[0] and flag[21] != secret[0] and flag[27] != secret[0] -> all must equal secret[0]
    flag[12] = flag[21] = flag[27] = secret[0]  # 'a'
    
    flag[13] = secret[15]  # 'p'
    
    # flag[14] != secret[64] and flag[19] != secret[64] and flag[24] != secret[64] -> all must equal secret[64]
    flag[14] = flag[19] = flag[24] = secret[64]  # '_'
    
    flag[16] = secret[11]  # 'l'
    flag[17] = secret[12]  # 'm'
    
    # flag[18] != secret[20] and flag[31] != secret[20] -> both must equal secret[20]
    flag[18] = flag[31] = secret[20]  # 'u'
    
    flag[20] = secret[41]  # 'P'
    flag[22] = secret[3]   # 'd'
    flag[23] = secret[8]   # 'i'
    flag[25] = secret[26]  # 'A'
    flag[26] = secret[1]   # 'b'
    flag[28] = secret[13]  # 'n'
    flag[29] = secret[6]   # 'g'
    flag[30] = secret[10]  # 'k'
    
    # flag[32] != secret[7] and flag[33] != secret[7] -> both must equal secret[7]
    flag[32] = flag[33] = secret[7]  # 'h'
    
    flag[34] = secret[63]  # '}'
    
    result = ''.join(flag)
    print("Solved flag:", result)
    print("Flag length:", len(result))
    
    return result

def verify_flag(flag):
    """Verify the flag using the original check logic"""
    if len(flag) != 35:
        return False
        
    secret = get_secret()
    
    # Check all constraints
    constraints = [
        flag[0] == secret[34] and flag[15] == secret[34],
        flag[1] == secret[45] and flag[5] == secret[45] and flag[9] == secret[45],
        flag[2] == secret[31],
        flag[3] == secret[30],
        flag[4] == secret[44],
        flag[6] == secret[54],
        flag[7] == secret[57],
        flag[8] == secret[62],
        flag[10] == secret[4],
        flag[11] == secret[19],
        flag[12] == secret[0] and flag[21] == secret[0] and flag[27] == secret[0],
        flag[13] == secret[15],
        flag[14] == secret[64] and flag[19] == secret[64] and flag[24] == secret[64],
        flag[16] == secret[11],
        flag[17] == secret[12],
        flag[18] == secret[20] and flag[31] == secret[20],
        flag[20] == secret[41],
        flag[22] == secret[3],
        flag[23] == secret[8],
        flag[25] == secret[26],
        flag[26] == secret[1],
        flag[28] == secret[13],
        flag[29] == secret[6],
        flag[30] == secret[10],
        flag[32] == secret[7] and flag[33] == secret[7],
        flag[34] == secret[63]
    ]
    
    return all(constraints)

# Solve and verify
solved_flag = solve_flag()
print("\nVerification:", verify_flag(solved_flag))