import bitarray

# Initial permutation choice table (PC1)
PC1 = [
    57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43,
    35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54,
    46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
]

# Permuted choice 2 table (PC2)
PC2 = [
    14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7,
    27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39,
    56, 34, 53, 46, 42, 50, 36, 29, 32
]

# Initial permutation (IP)
IP = [
    58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46,
    38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17,
    9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55,
    47, 39, 31, 23, 15, 7
]
# Final permutation (FP)
FP = [
    40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46,
    14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20,
    60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33,
    1, 41, 9, 49, 17, 57, 25
]

# Expansion permutation table (E)
E = [
    32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15,
    16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28,
    29, 28, 29, 30, 31, 32, 1
]

# P-box permutation table (P)
P = [
    16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14,
    32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25
]

# S-boxes (S1 to S8)
S_BOX = [
    # S1
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

    # S2
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

    # S3
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

    # S4
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

    # S5
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

    # S6
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

    # S7
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

    # S8
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]


def add_spaces(binary_string):
  return ' '.join(binary_string[i:i + 8]
                  for i in range(0, len(binary_string), 8))


def permute(key, table):
  """Performs permutation on the key according to the given table."""
  return bitarray.bitarray([key[i - 1] for i in table])
def sbox_substitution(data,j):
  sboxed_data = bitarray.bitarray()
  for i in range(8):
      block = data[i * 6:(i + 1) * 6]

    # Pad the block with zeros to make it a multiple of 8 bits long
      while len(block) < 8:
          block.append(0)

    # Convert the block to an integer
      row = int(block[0]) * 2 + int(block[5])
      col = int(block[1]) * 8 + int(block[2]) * 4 + int(block[3]) * 2 + int(block[4])

      sbox_value = S_BOX[i][row][col]
      sboxed_data.extend(format(sbox_value, '04b'))
  print("\nAfter Appling S-Boxes on Each Block")
  if j==1:
    print(f"S(K1 XOR E(R0)): {sboxed_data.to01()}")
  else:
    print(f"S(K2 XOR E(R1)): {sboxed_data.to01()}")

  return sboxed_data





def perform_des_round(data, key,i):
  if i==1:
    print("F(R0, K1) :")
  else:
    print("F(R1, K2) :")
  # Expand and permute the data
  expanded_data = permute(data, E)  # 48 bits
  if i==1:
    print(f"E(R0) in 48 bits: {add_spaces(expanded_data.to01())}")
  else:
    print(f"E(R1) in 48 bits: {add_spaces(expanded_data.to01())}")
  # XOR with the round key
  expanded_data ^= key
  if i==1:
    print(f"K1 XOR E(R0): {add_spaces(expanded_data.to01())}")
  else:
    print(f"K2 XOR E(R1): {add_spaces(expanded_data.to01())}")
  # Apply the S-boxes
  sboxed_data = sbox_substitution(expanded_data,i)

  print("\nNow Applying P-BOX")
  # Permute using P-box
  permuted_data = permute(sboxed_data, P)
  if i==1:
    print(f"F(R0,K1): {permuted_data.to01()}")
  else:
    print(f"F(R1,K2): {permuted_data.to01()}")

  return permuted_data


def generate_round_keys(key_text):
  print("Key Scheduling:")
  # Convert the key from text to a binary string
  key_binary = ''.join(format(ord(char), '08b') for char in key_text)

  # Ensure the key is 64 bits (pad with zeros if needed)
  key_binary = key_binary[:64].ljust(64, '0')
  print(f"Key in 64 bit:{add_spaces(key_binary)} ")

  # Apply the initial permutation (PC1)
  key = bitarray.bitarray(key_binary)
  key = permute(key, PC1)
  print(f"Key after PC-1:{add_spaces(key.to01())} ")

  print("\nSpliting Into C0 and D0")
  # Split the key into two halves (C0 and D0)
  C0 = key[:28]
  D0 = key[28:]

  print(f"C0:{add_spaces(C0.to01())} ")
  print(f"D0:{add_spaces(D0.to01())} ")
  print("\nLeft Shift by 1 Bit")
  # Perform a left shift for both halves (C1 and D1)
  C1 = C0[1:] + C0[:1]
  D1 = D0[1:] + D0[:1]
  print(f"C1:{add_spaces(C1.to01())} ")
  print(f"D1:{add_spaces(D1.to01())} ")
 

  print("\nAgain Left Shift by 1 Bit")
  # Perform a left shift for both halves (C2 and D2)
  C2 = C1[1:] + C1[:1]
  D2 = D1[1:] + D1[:1]
  print(f"C2:{add_spaces(C2.to01())} ")
  print(f"D2:{add_spaces(D2.to01())} ")

  print("\nConcatenating C1 and D1")
  # Combine C1 and D1
  combined_half = C1 + D1

  print(f"C1D1:{add_spaces(combined_half.to01())} ")
  
  # Apply the permutation choice 2 (PC2) to get K1
  K1 = permute(combined_half, PC2)

  print("\nConcatenating C2 and D2")
  # Combine C2 and D2
  combined_half = C2 + D2
  
  print(f"C2D2:{add_spaces(combined_half.to01())} ")


  # Apply the permutation choice 2 (PC2) to get K2
  K2 = permute(combined_half, PC2)
  print("\nAfter Appling PC-2")
  print(f"K1: {K1.to01()}")
  print(f"K2: {K2.to01()}")
  return K1, K2


def encrypt_with_iv(plaintext, K1, K2, iv):
  print("\n\nEncryption:")
  # Convert IV from text to binary
  iv_binary = ''.join(format(ord(char), '08b') for char in iv)

  # Ensure IV is 64 bits (pad with zeros if needed)
  iv_binary = iv_binary[:64].ljust(64, '0')
  print(f"IV in 64 bit:{add_spaces(iv_binary)} ")

  # XOR the IV with the plaintext
  plaintext_binary = ''.join(format(ord(char), '08b') for char in plaintext)
  plaintext_binary = plaintext_binary[:64].ljust(64,
                                                 '0')  # Ensure it's 64 bits
  print(f"Plaintext in 64 bit:{add_spaces(plaintext_binary)} ")
  initial_data = bitarray.bitarray(plaintext_binary) ^ bitarray.bitarray(
      iv_binary)
  print(f"IV XOR PlainText: {initial_data.to01()}")


  # Initial permutation (IP)
  initial_data = permute(initial_data, IP)

  print(f"After Initial Permutation: {initial_data.to01()}")

  print("\nNow Split this into L0 and R0 each of 32 bits")
  # Split the data into two halves, L0 and R0
  L0 = initial_data[:32]
  R0 = initial_data[32:]
  print(f"L0:{add_spaces(L0.to01())} ")
  print(f"R0:{add_spaces(R0.to01())} ")


  print("\nRound 1\n")
  # Round 1
  L1 = R0
  print(f"L1:{add_spaces(L1.to01())} ")
  print("R1 = L0 XOR F(R0, K1)")
  R1 = L0 ^ perform_des_round(R0, K1,1)
  print(f"R1:{add_spaces(R1.to01())} ")  

  print("\nRound 2\n")
  # Round 2
  L2 = R1
  print(f"L2:{add_spaces(L2.to01())} ")
  print("R2 = L1 XOR F(R1, K2)")
  R2 = L1 ^ perform_des_round(R1, K2,2)
  print(f"R2:{add_spaces(R2.to01())} ")  

  # Concatenate L2 and R2
  result_data = L2 + R2
  print(f"\nConcatenating L2 and R2 :{add_spaces(result_data.to01())} ")
  # Final permutation (FP)
  ciphertext = permute(result_data, FP)
  print(f"\nAfter Final Permutation\n\nCipherText: {ciphertext.to01()}")
  return ciphertext


# Input the key in text form
key_text = input("Enter the 8-character key in text form: ")

# Input the IV in text form
iv_text = input("Enter the 8-character IV in text form: ")

# Input the plaintext in text form
plaintext = input("Enter the 8-character plaintext in text form: ")




print(f"PlainText: {plaintext}")
print(f"Key: {key_text}")
print(f"IV: {iv_text}")
# Generate K1 and K2
K1, K2 = generate_round_keys(key_text)

# Encrypt the plaintext with IV
ciphertext = encrypt_with_iv(plaintext, K1, K2, iv_text)


