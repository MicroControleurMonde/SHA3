import array
import ubinascii

# Fonction de rotation à gauche de 64 bits
def ROL64(a, n):
    return ((a >> (64 - (n % 64))) | (a << (n % 64))) & (2**64 - 1)

# Fonction principale de transformation Keccak (KeccakF1600onLanes)
def KeccakF1600onLanes(lanes):
    R = 1
    for round in range(24):
        # θ
        C = [lanes[x][0] ^ lanes[x][1] ^ lanes[x][2] ^ lanes[x][3] ^ lanes[x][4] for x in range(5)]
        D = [C[(x + 4) % 5] ^ ROL64(C[(x + 1) % 5], 1) for x in range(5)]
        lanes = [[lanes[x][y] ^ D[x] for y in range(5)] for x in range(5)]
        
        # ρ et π
        (x, y) = (1, 0)
        current = lanes[x][y]
        for t in range(24):
            (x, y) = (y, (2 * x + 3 * y) % 5)
            (current, lanes[x][y]) = (lanes[x][y], ROL64(current, (t + 1) * (t + 2) // 2))
        
        # χ
        for y in range(5):
            T = [lanes[x][y] for x in range(5)]
            for x in range(5):
                lanes[x][y] = T[x] ^ ((~T[(x + 1) % 5]) & T[(x + 2) % 5])
        
        # ι
        for j in range(7):
            R = ((R << 1) ^ ((R >> 7) * 0x71)) % 256
            if (R & 2):
                lanes[0][0] = lanes[0][0] ^ (1 << ((1 << j) - 1))
    
    return lanes

# Fonction de chargement de 64 bits (8 octets)
def load64(b):
    return sum((b[i] << (8 * i)) for i in range(8))

# Fonction de stockage de 64 bits (8 octets)
def store64(a):
    return array.array('B', [(a >> (8 * i)) & 0xFF for i in range(8)])

# Fonction KeccakF1600 qui applique la transformation à l'état
def KeccakF1600(state):
    lanes = [[load64(state[8 * (x + 5 * y): 8 * (x + 5 * y) + 8]) for y in range(5)] for x in range(5)]
    lanes = KeccakF1600onLanes(lanes)
    state = bytearray(200)
    for x in range(5):
        for y in range(5):
            state[8 * (x + 5 * y): 8 * (x + 5 * y) + 8] = store64(lanes[x][y])
    return state

# Fonction principale Keccak
def Keccak(rate, capacity, inputBytes, delimitedSuffix, outputByteLen):
    outputBytes = bytearray()
    state = bytearray(200)
    rateInBytes = rate // 8
    blockSize = 0
    if (((rate + capacity) != 1600) or ((rate % 8) != 0)):
        return
    inputOffset = 0
    # === Absorber tous les blocs d'entrée ===
    while inputOffset < len(inputBytes):
        blockSize = min(len(inputBytes) - inputOffset, rateInBytes)
        for i in range(blockSize):
            state[i] ^= inputBytes[i + inputOffset]
        inputOffset += blockSize
        if blockSize == rateInBytes:
            state = KeccakF1600(state)
            blockSize = 0
    # === Faire le padding et passer à la phase de squeeze ===
    state[blockSize] ^= delimitedSuffix
    if ((delimitedSuffix & 0x80) != 0) and (blockSize == (rateInBytes - 1)):
        state = KeccakF1600(state)
    state[rateInBytes - 1] ^= 0x80
    state = KeccakF1600(state)
    # === Extraire tous les blocs de sortie ===
    while outputByteLen > 0:
        blockSize = min(outputByteLen, rateInBytes)
        outputBytes.extend(state[:blockSize])
        outputByteLen -= blockSize
        if outputByteLen > 0:
            state = KeccakF1600(state)
    return outputBytes

def SHAKE128(inputBytes, outputByteLen):
    # Appeler la fonction Keccak avec un taux de 1344 bits et une capacité de 256 bits (SHAKE128)
    return Keccak(1344, 256, inputBytes, 0x1F, outputByteLen)

def SHAKE256(inputBytes, outputByteLen):
    # Appeler la fonction Keccak avec un taux de 1088 bits et une capacité de 512 bits (SHAKE256)
    return Keccak(1088, 512, inputBytes, 0x1F, outputByteLen)


def SHA3_224(inputBytes):
    return Keccak(1152, 448, inputBytes, 0x06, 224//8)

def SHA3_256(inputBytes):
    return Keccak(1088, 512, inputBytes, 0x06, 256 // 8)

def SHA3_384(inputBytes):
    return Keccak(832, 768, inputBytes, 0x06, 384//8)

def SHA3_512(inputBytes):
    return Keccak(576, 1024, inputBytes, 0x06, 512//8)

# Fonction pour convertir un tableau d'octets en une chaîne hexadécimale
def bytes_to_hex(byte_array):
    return ubinascii.hexlify(byte_array).decode('utf-8')

# Exporter les fonctions nécessaires dans le module
__all__ = [
    "SHA3_224", "SHA3_256", "SHA3_384", "SHA3_512",
    "SHAKE128", "SHAKE256", "bytes_to_hex"
]

