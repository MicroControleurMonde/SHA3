import libsha3

# Function to test SHAKE128
def test_shake128():
    print("\nSHAKE 128")
    test_cases = [
        {"msg": "", "expected": "7f9c2ba4e88f827d616045507605853ed73b8093f6efbc88eb1a6eacfa66ef26", "length": 32},
        {"msg": "The quick brown fox jumps over the lazy dog", "expected": "f4202e3c5852f9182a0430fd8144f0a74b95e7417ecae17db0f8cfeed0e3e66e", "length": 32},
    ]

    for case in test_cases:
        input_bytes = bytearray(case["msg"], 'utf-8')
        output = libsha3.SHAKE128(input_bytes, case["length"])
        output_hex = libsha3.bytes_to_hex(output)
        print(f"Test for '{case['msg']}': {output_hex}")
        assert output_hex == case["expected"], f"Failure for {case['msg']}: {output_hex} (expected {case['expected']})"
        print(f"Successful test for: {case['msg']}")

# # Function to test SHAKE256
def test_shake256():
    print("\nSHAKE 256")
    test_cases = [
        {"msg": "", "expected": "46b9dd2b0ba88d13233b3feb743eeb243fcd52ea62b81b82b50c27646ed5762fd75dc4ddd8c0f200cb05019d67b592f6fc821c49479ab48640292eacb3b7c4be", "length": 64},
        {"msg": "The quick brown fox jumps over the lazy dog", "expected": "2f671343d9b2e1604dc9dcf0753e5fe15c7c64a0d283cbbf722d411a0e36f6ca1d01d1369a23539cd80f7c054b6e5daf9c962cad5b8ed5bd11998b40d5734442", "length": 64},
    ]

    for case in test_cases:
        input_bytes = bytearray(case["msg"], 'utf-8')
        output = libsha3.SHAKE256(input_bytes, case["length"])
        output_hex = libsha3.bytes_to_hex(output)
        print(f"Test for'{case['msg']}': {output_hex}")
        assert output_hex == case["expected"], f"Failure for {case['msg']}: {output_hex} (expected {case['expected']})"
        print(f"Successful test for: {case['msg']}")

# Exécution des tests
test_shake128()
test_shake256()
