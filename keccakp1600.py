# keccak_p1600.py
# Ported from XKCP code
# github.com/XKCP/XKCP
from machine import mem32

# Constantes
KECCAK_ROUNDS = 24
KECCAK_STATE_SIZE = 200

# Tables de rotation
RHO = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 2, 14, 27, 41, 56, 8, 25, 43, 62, 18, 39, 61, 20, 44]
PI = [10, 7, 11, 17, 18, 3, 5, 16, 8, 21, 24, 4, 15, 23, 19, 13, 12, 2, 20, 14, 22, 9, 6, 1]

# Constantes de ronde
RC = [
    0x0000000000000001, 0x0000000000008082, 0x800000000000808A, 0x8000000080008000,
    0x000000000000808B, 0x0000000080000001, 0x8000000080008081, 0x8000000000008009,
    0x000000000000008A, 0x0000000000000088, 0x0000000080008009, 0x000000008000000A,
    0x000000008000808B, 0x800000000000008B, 0x8000000000008089, 0x8000000000008003,
    0x8000000000008002, 0x8000000000000080, 0x000000000000800A, 0x800000008000000A,
    0x8000000080008081, 0x8000000000008080, 0x0000000080000001, 0x8000000080008008
]

def rol64(a, n):
    """Effectue une rotation à gauche de 64 bits"""
    return ((a << n) | (a >> (64 - n))) & 0xFFFFFFFFFFFFFFFF

def keccak_f1600(state):
    """Effectue la fonction de permutation Keccak-p[1600]"""
    def theta():
        """Phase theta du Keccak"""
        C = [state[x] ^ state[x + 5] ^ state[x + 10] ^ state[x + 15] ^ state[x + 20] for x in range(5)]
        D = [C[(x - 1) % 5] ^ rol64(C[(x + 1) % 5], 1) for x in range(5)]
        for x in range(25):
            state[x] ^= D[x % 5]

    def rho_pi():
        """Phase rho et pi du Keccak"""
        current = state[1]
        for x in range(24):
            index = PI[x]
            temp = state[index]
            state[index] = rol64(current, RHO[x])
            current = temp

    def chi():
        """Phase chi du Keccak"""
        for y in range(0, 25, 5):
            T = [state[y + x] for x in range(5)]
            for x in range(5):
                state[y + x] ^= (~T[(x + 1) % 5]) & T[(x + 2) % 5]

    def iota(round):
        """Phase iota du Keccak"""
        state[0] ^= RC[round]

    for round in range(KECCAK_ROUNDS):
        theta()
        rho_pi()
        chi()
        iota(round)

    return state

def keccak_p1600(state):
    """Alias pour la fonction de permutation Keccak-p[1600]"""
    return keccak_f1600(state)

def bytes_to_state(data):
    """Convertit une séquence d'octets en un état Keccak"""
    state = [0] * 25
    for i in range(min(len(data) // 8, 25)):
        state[i] = int.from_bytes(data[i*8:(i+1)*8], 'little')
    return state

def state_to_bytes(state):
    """Convertit un état Keccak en une séquence d'octets"""
    return b''.join([x.to_bytes(8, 'little') for x in state])

def compute_keccak(input_data):
    """Calcul Keccak-p[1600] pour les données d'entrée"""
    padded_data = input_data + b'\x00' * (200 - len(input_data))
    
    # Convertir les données en état
    state = bytes_to_state(padded_data)
    
    # Effectuer la permutation Keccak-p[1600]
    state = keccak_p1600(state)
    
    # Convertir l'état en résultat
    result = state_to_bytes(state)
    
    return result
