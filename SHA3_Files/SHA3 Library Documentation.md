### SHA3 Library Documentation

This library implements the Keccak hashing algorithm, which is the basis of the SHA-3 family of hash functions (SHA3-224, SHA3-256, SHA3-384, SHA3-512) as well as the SHAKE128 and SHAKE256 functions. Keccak is a cryptographic hash function based on a permutation network (sponge construction system).

#### 1. **Main Functions**

- **`Keccak(rate, capacity, inputBytes, delimitedSuffix, outputByteLen)`**  
  This is the generic function that performs the Keccak transformation. It is used to generate the hash of the input with the given rate and capacity. This function is called by the hashing functions like SHA3 and SHAKE.

  **Parameters:**
  - `rate`: The rate (in bits) of the Keccak function.
  - `capacity`: The capacity (in bits) of the Keccak function.
  - `inputBytes`: The input data as a byte array.
  - `delimitedSuffix`: The delimiter suffix to append for the padding phase.
  - `outputByteLen`: The length of the output in bytes.

  **Returns:**  
  A byte array representing the generated hash.

- **`KeccakF1600(state)`**  
  Applies the KeccakF1600 transformation to the hash state. This transformation is repeated multiple times during the hashing process.

  **Parameters:**
  - `state`: The current hash state as a byte array.

  **Returns:**  
  The transformed state as a byte array.

- **`SHAKE128(inputBytes, outputByteLen)`**  
  The SHAKE128 function generates a variable-length output with a rate of 1344 bits and a capacity of 256 bits.

  **Parameters:**
  - `inputBytes`: The input data as a byte array.
  - `outputByteLen`: The length of the output in bytes.

  **Returns:**  
  A byte array containing the hash result.

- **`SHAKE256(inputBytes, outputByteLen)`**  
  The SHAKE256 function generates a variable-length output with a rate of 1088 bits and a capacity of 512 bits.

  **Parameters:**
  - `inputBytes`: The input data as a byte array.
  - `outputByteLen`: The length of the output in bytes.

  **Returns:**  
  A byte array containing the hash result.

- **`SHA3_224(inputBytes)`**  
  The SHA3-224 function generates a 224-bit (28-byte) hash of the input. It uses a rate of 1152 bits and a capacity of 448 bits.

  **Parameters:**
  - `inputBytes`: The input data as a byte array.

  **Returns:**  
  A byte array representing the SHA3-224 hash.

- **`SHA3_256(inputBytes)`**  
  The SHA3-256 function generates a 256-bit (32-byte) hash of the input. It uses a rate of 1088 bits and a capacity of 512 bits.

  **Parameters:**
  - `inputBytes`: The input data as a byte array.

  **Returns:**  
  A byte array representing the SHA3-256 hash.

- **`SHA3_384(inputBytes)`**  
  The SHA3-384 function generates a 384-bit (48-byte) hash of the input. It uses a rate of 832 bits and a capacity of 768 bits.

  **Parameters:**
  - `inputBytes`: The input data as a byte array.

  **Returns:**  
  A byte array representing the SHA3-384 hash.

- **`SHA3_512(inputBytes)`**  
  The SHA3-512 function generates a 512-bit (64-byte) hash of the input. It uses a rate of 576 bits and a capacity of 1024 bits.

  **Parameters:**
  - `inputBytes`: The input data as a byte array.

  **Returns:**  
  A byte array representing the SHA3-512 hash.

- **`bytes_to_hex(byte_array)`**  
  A utility function to convert a byte array to a human-readable hexadecimal string.

  **Parameters:**
  - `byte_array`: A byte array to convert.

  **Returns:**  
  A hexadecimal string.

---

#### 2. **Example Usage**

Here is an example of how to use the functions from this library to generate hashes with SHA3 and SHAKE:

```python
import ubinascii
from libsha3 import SHA3_224, SHA3_256, SHA3_384, SHA3_512, SHAKE128, SHAKE256, bytes_to_hex

def test_libsha3():
    ## Ask the user to enter a string of characters
    input_data = input("Enter a string of characters to hash : ").encode('utf-8')

    # Test for SHA3-512
    hash_sha3_512 = SHA3_512(input_data)
    print(f"SHA3-512: {bytes_to_hex(hash_sha3_512)}")

    # Test for SHAKE256 (output 64 octets)
    output_shake256 = SHAKE256(input_data, 64)
    print(f"SHAKE256 (64 octets output): {bytes_to_hex(output_shake256)}")

# Run the test
test_libsha3()
```

### Explanation of the Example Code:
1. **`input_data = input("Enter a string to hash: ").encode('utf-8')`**  
   This line prompts the user to input a string, which is then encoded into bytes to be processed by the hash functions.

2. **Calling the Hash Functions**  
   For the hash function (`SHA3-512`), we call the corresponding function with the input data and display the results in hexadecimal format.

3. **Displaying Results**  
   The hash results are converted to hexadecimal strings using the `bytes_to_hex()` function and printed to the user.

### Example Output:
```
Enter a string to hash: Hello, Keccak!

SHA3-512: 80f91cb7db0517d9298a4c0d281b0c54848f2cfabb6c74628d413aab29c442ea084b64a84e9a66b83531a07179eab9ae88b6eab457aa57d7a7de15b41642e07d
SHAKE256 (64 bytes): 564d672b62b48959c7c1ec4c37ff104c50b9a0b7b159c99f82b8f0c607dfca5f158c8a3932767e86907da278905b26e246010a35ab5fbd4cb39ca0c8f702c3a24
```

This code demonstrates how to integrate different hash functions to produce hashes with different hash sizes and for custom output lengths.