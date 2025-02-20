# Crypto Keccak / SHA3

![image](https://github.com/user-attachments/assets/d23da5d7-1ce4-4f79-a960-7c93ea75acd0)

## Implementation of crypto code with MicroPython

The SHA-3 (Secure Hash Algorithm 3) and SHAKE functions are cryptographic hashing algorithms that are part of the SHA-3 family, standardized by the National Institute of Standards and Technology (NIST).

The library implements the following fixed size hash fonctions: **SHA3-224**, **SHA3-256**, **SHA3-384**, **SHA3-512** and **SHAKE128**, **SHAKE256** the  for variable size hashes.

The code was developed and tested on RP2350.
It is compatible with RP2040 / ESP32

## Keccak-p1600

- **Keccak-p[1600] library** [`keccakp1600.py`](https://github.com/MicroControleurMonde/SHA3/blob/main/keccakp1600.py)
- **library testing** [`test_keccak_p1600.py`](https://github.com/MicroControleurMonde/SHA3/blob/main/test_keccak_p1600.py`)
- **Documentation**[`Keccak-p[1600]`](https://github.com/MicroControleurMonde/SHA3/blob/main/Keccak/keccak_p1600.md)

## SHA3

- **SHA3 library** [`libsha3.py`](https://github.com/MicroControleurMonde/SHA3/blob/main/SHA3_Files/libsha3.py)
- **SHA3 Test code** [`libsha3_simple_test.py`](https://github.com/MicroControleurMonde/SHA3/blob/main/SHA3_Files/libsha3_simple_test.py)
- **Documentation** [`SHA3 Library Documentation.md`](https://github.com/MicroControleurMonde/SHA3/blob/main/SHA3_Files/SHA3%20Library%20Documentation.md)


NIST test vectors (FIPS 202) (https://csrc.nist.gov/projects/cryptographic-algorithm-validation-program/secure-hashing#sha3vsha3vss)
  
- **Library vectors testing for SHA3 fonctions** [`libsha3_vectors_sha_test.py`](https://github.com/MicroControleurMonde/SHA3/blob/main/SHA3_Files/libsha3_vectors_sha_test.py)
- **Library vectors testing for SHAKE fonctions** [`libsha3_vectors_shake_tests.py`](https://github.com/MicroControleurMonde/SHA3/blob/main/SHA3_Files/libsha3_vectors_shake_tests.py)

[XKCP Original code](https://github.com/XKCP/XKCP/tree/master/Standalone/CompactFIPS202/Python)
- **Reference code** in pure Python given by Keccak Team [`CompactFIPS202_XKCP_Ref_Code.py`](https://github.com/MicroControleurMonde/SHA3/blob/main/SHA3_Files/CompactFIPS202_XKCP_Ref_Code.py) {without Numpy}
---
Useful link for hashing, encoding, decoding, encryption, decryption, formatting, generating and so on...
[Online Tools](https://emn178.github.io/online-tools/)
