# Import the Keccak-p[1600] cryptographic hash function 
# Ported from XKCP code
# github.com/XKCP/XKCP
import keccakp1600

# Request a string as input from the user
try:
    user_input = input("Enter a string to hash with Keccak-p1600 : ").encode('utf-8')
    if not user_input:
        raise ValueError("Input cannot be empty.")
# Calculate the Keccak result    
    result = keccakp1600.compute_keccak(user_input)
    # Display the result
    print(f"Keccak-p[1600] result: {result.hex()}")

except Exception as e:
    print(f"An error has occurred : {e}")
