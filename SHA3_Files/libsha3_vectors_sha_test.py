# libsha3_vectors_sha_test.py
import libsha3

# Test function for SHA3
def test_sha3_function(sha3_function, test_vectors):
    for test in test_vectors:
        input_bytes = bytearray(test["input"], 'utf-8')
        expected_output = test["expected"]
        
        # Calculer le hachage
        hashed_output = sha3_function(input_bytes)
        hashed_hex = libsha3.bytes_to_hex(hashed_output).replace(" ", "").lower()
        
        # Afficher le résultat du test
        if hashed_hex == expected_output:
            print(f"Passed test for entry '{test['input']}': {hashed_hex}")
        else:
            print(f"Failure for entry '{test['input']}': {hashed_hex} (expected {expected_output})")

# Test vectors for SHA3-224
sha3_224_test_vectors = [
    {"input": "", "expected": "6b4e03423667dbb73b6e15454f0eb1abd4597f9a1b078e3f5b5a6bc7"},
    {"input": "abc", "expected": "e642824c3f8cf24ad09234ee7d3c766fc9a3a5168d0c94ad73b46fdf"},
    {"input": "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq", "expected": "8a24108b154ada21c9fd5574494479ba5c7e7ab76ef264ead0fcce33"}
]

# Test vectors for SHA3-256
sha3_256_test_vectors = [
    {"input": "", "expected": "a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a"},
    {"input": "abc", "expected": "3a985da74fe225b2045c172d6bd390bd855f086e3e9d525b46bfe24511431532"},
    {"input": "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq", "expected": "41c0dba2a9d6240849100376a8235e2c82e1b9998a999e21db32dd97496d3376"}
]

# Vecteurs de test pour SHA3-384
sha3_384_test_vectors = [
    {"input": "", "expected": "0c63a75b845e4f7d01107d852e4c2485c51a50aaaa94fc61995e71bbee983a2ac3713831264adb47fb6bd1e058d5f004"},
    {"input": "abc", "expected": "ec01498288516fc926459f58e2c6ad8df9b473cb0fc08c2596da7cf0e49be4b298d88cea927ac7f539f1edf228376d25"},
    {"input": "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq", "expected": "991c665755eb3a4b6bbdfb75c78a492e8c56a22c5c4d7e429bfdbc32b9d4ad5aa04a1f076e62fea19eef51acd0657c22"}
]

# Test vectors for SHA3-512
sha3_512_test_vectors = [
    {"input": "", "expected": "a69f73cca23a9ac5c8b567dc185a756e97c982164fe25859e0d1dcc1475c80a615b2123af1f5f94c11e3e9402c3ac558f500199d95b6d3e301758586281dcd26"},
    {"input": "abc", "expected": "b751850b1a57168a5693cd924b6b096e08f621827444f70d884f5d0240d2712e10e116e9192af3c91a7ec57647e3934057340b4cf408d5a56592f8274eec53f0"},
    {"input": "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq", "expected": "04a371e84ecfb5b8b77cb48610fca8182dd457ce6f326a0fd3d7ec2f1e91636dee691fbe0c985302ba1b0d8dc78c086346b533b49c030d99a27daf1139d6e75e"}
]

# Test SHA3-224
print("Tests SHA3-224:")
test_sha3_function(libsha3.SHA3_224, sha3_224_test_vectors)

# Test SHA3-256
print("\nTests SHA3-256:")
test_sha3_function(libsha3.SHA3_256, sha3_256_test_vectors)

# Test SHA3-384
print("\nTests SHA3-384:")
test_sha3_function(libsha3.SHA3_384, sha3_384_test_vectors)

# Test SHA3-512
print("\nTests SHA3-512:")
test_sha3_function(libsha3.SHA3_512, sha3_512_test_vectors)
