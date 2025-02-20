import ubinascii
from libsha3 import SHA3_224, SHA3_256, SHA3_384, SHA3_512, SHAKE128, SHAKE256, bytes_to_hex

def test_keccak():
    ## Ask the user to enter a string of characters
    input_data = input("Enter a string of characters to hash : ").encode('utf-8')

    # Test for SHA3-224
    hash_sha3_224 = SHA3_224(input_data)
    print(f"SHA3-224: {bytes_to_hex(hash_sha3_224)}")

    # Test for  SHA3-256
    hash_sha3_256 = SHA3_256(input_data)
    print(f"SHA3-256: {bytes_to_hex(hash_sha3_256)}")

    # Test for  SHA3-384
    hash_sha3_384 = SHA3_384(input_data)
    print(f"SHA3-384: {bytes_to_hex(hash_sha3_384)}")

    # Test for  SHA3-512
    hash_sha3_512 = SHA3_512(input_data)
    print(f"SHA3-512: {bytes_to_hex(hash_sha3_512)}")

    # Test for  SHAKE128 (output 64 octets)
    output_shake128 = SHAKE128(input_data, 64)
    print(f"\nSHAKE128 (64 octets output): {bytes_to_hex(output_shake128)}")

    # Test for  SHAKE256 (output 64 octets)
    output_shake256 = SHAKE256(input_data, 64)
    print(f"SHAKE256 (64 octets output): {bytes_to_hex(output_shake256)}")

# Run the test
test_keccak()
