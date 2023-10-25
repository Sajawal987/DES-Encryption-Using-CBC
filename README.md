# DES-Encryption-Using-CBC

This repository contains a Python implementation of a single round of the Data Encryption Standard (DES) algorithm, focusing on the round function.

## Tables and Permutations

The provided tables are integral to the DES algorithm. These include:
- Initial Permutation Choice table (PC1)
- Permuted Choice 2 table (PC2)
- Initial permutation (IP)
- Final permutation (FP)
- Expansion permutation table (E)
- P-box permutation table (P)
- S-boxes (S1 to S8)

## Functions

1. *add_spaces(binary_string)*
   - Adds spaces between every 8 bits for better readability.
   
2. *permute(key, table)*
   - Performs permutation on the key according to the provided table.

3. *sbox_substitution(data)*
   - Performs substitution of data using S-boxes.

4. *perform_des_round(data, key)*
   - Executes a single round of the DES algorithm on the provided data using the given key.

## How to Use

1. Ensure you have Python installed.
2. Clone the repository to your local machine.
3. Use the functions provided in the code as per your requirement.

```python
# Example:
data = bitarray.bitarray('11001100110011001100110011001100')
key = bitarray.bitarray('10101010101010101010101010101010')
perform_des_round(data, key)
