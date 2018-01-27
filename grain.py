from collections import deque
from itertools import repeat
from bitstring import BitArray

class Grain:
    def __init__(self, key, iv):
        self.NFSR = []
        self.LFSR = []
        self.NFTable = [
            0,1,0,0,1,0,1,1,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,0,1,0,0,0,1,0,1,
            1,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,1,0,1,1,0,1,0,0,0,1,0,0,0,1,0,1,
            1,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,1,0,1,1,1,0,1,0,
            0,1,0,0,1,0,1,1,1,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,1,0,1,1,1,0,1,0,
            1,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,1,0,1,1,1,0,1,0,
            0,1,0,0,1,0,1,1,1,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,1,0,1,1,1,0,1,0,
            0,1,0,0,1,0,1,1,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,0,1,0,0,0,1,0,1,
            1,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,1,0,1,1,0,1,0,0,0,1,0,0,1,0,1,0,
            1,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,1,0,1,1,1,0,1,0,
            0,1,0,0,1,0,1,1,1,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,1,0,1,1,1,0,1,0,
            0,1,0,0,1,0,1,1,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,0,1,0,0,0,1,0,1,
            1,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,1,0,1,1,0,1,0,0,0,1,0,0,0,1,0,1,
            0,1,0,0,1,0,1,1,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,0,1,0,0,0,1,0,1,
            1,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,1,0,1,1,1,0,1,0,
            0,1,0,0,1,0,1,1,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,0,1,0,0,0,1,0,1,
            1,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,1,0,1,1,0,1,0,1,
            0,1,0,0,1,0,1,1,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,0,1,0,0,0,1,0,1,
            1,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,1,0,1,1,0,1,0,0,0,1,0,0,0,1,0,1,
            1,0,1,1,0,1,0,0,0,0,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,1,1,0,1,1,1,1,
            0,1,0,0,1,0,1,1,1,1,1,0,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,0,1,1,1,1,
            1,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,1,0,1,1,1,0,1,0,
            0,1,0,0,1,0,1,1,1,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,1,0,1,1,1,0,1,0,
            0,1,0,0,1,0,1,1,1,1,1,0,0,0,0,1,1,0,1,1,0,1,0,0,0,0,0,1,0,0,0,0,
            1,0,1,1,0,1,0,0,0,0,0,1,1,1,1,0,1,0,1,1,0,1,0,0,0,0,0,1,1,1,1,1,
            0,1,0,0,1,0,0,0,1,0,1,1,0,1,1,1,1,0,1,1,0,1,1,1,0,1,0,0,0,1,1,0,
            1,0,1,1,0,1,1,1,0,1,0,0,1,0,0,0,1,0,1,1,0,1,1,1,0,1,0,0,0,1,1,0,
            1,0,1,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,0,1,0,0,0,1,1,1,0,1,1,0,0,
            0,1,0,0,1,0,0,0,1,1,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,1,1,0,1,1,0,0,
            1,0,1,1,0,1,1,1,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,1,1,1,0,0,1,
            0,1,0,0,1,0,0,0,1,0,1,1,0,1,1,1,1,0,1,1,0,1,1,1,0,1,0,0,0,1,1,0,
            1,0,1,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,0,1,0,0,0,1,1,1,0,1,1,0,0,
            1,0,1,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,0,1,0,0,0,1,1,1,0,0,0,1,1
        ]
        self.boolTable = [0,0,1,1,0,0,1,0,0,1,1,0,1,1,0,1,1,1,0,0,1,0,1,1,0,1,1,0,0,1,0,0]

        # Load NFSR with the key bits, bi = ki, 0 <= i < 79
        for i in range(80):
            self.NFSR.append(key[i])

        # Load the first 64 bits of LFSR with the IV si = IVi 0 <= i <= 63
        for i in range(64):
            self.LFSR.append(iv[i])
        
        # The remaining bits of LFSR are filled with ones si = 1, 64 <= i <= 79
        self.LFSR += list(repeat(1,16))

        # Convert list to collection deque
        self.NFSR = deque(self.NFSR)
        self.LFSR = deque(self.LFSR)

        # Initial clocking
        for i in range(160):
            outbit = self.keystream()
            self.LFSR[79] ^= outbit
            self.NFSR[79] ^= outbit

    def N(self, i):
        return self.NFSR[80-i]

    def L(self, i):
        return self.LFSR[80-i]

    def keystream(self):
        X0 = self.LFSR[3]
        X1 = self.LFSR[25]
        X2 = self.LFSR[46]
        X3 = self.LFSR[64]
        X4 = self.NFSR[63]
        
        # Calculate feedback and output bits
        outbit = self.N(79)^self.N(78)^self.N(76)^self.N(70)^self.N(49)^self.N(37)^self.N(24)^self.boolTable[(X4<<4) | (X3<<3) | (X2<<2) | (X1<<1) | X0]
        NBit = self.L(80)^self.N(18)^self.N(66)^self.N(80)^self.NFTable[(self.N(17)<<9) | (self.N(20)<<8) | (self.N(28)<<7) | (self.N(35)<<6) | (self.N(43)<<5) | (self.N(47)<<4) | (self.N(52)<<3) | (self.N(59)<<2) | (self.N(65)<<1) | self.N(71)]
        LBit = self.L(18)^self.L(29)^self.L(42)^self.L(57)^self.L(67)^self.L(80)
        
        self.NFSR.rotate(-1)
        self.LFSR.rotate(-1)
        self.NFSR[79] = NBit
        self.LFSR[79] = LBit
        
        return outbit

    def keystream_bytes(self, msglen):
        keystream = [0] * msglen
        for i in range(msglen):
            for j in range(8):
                outbit = self.keystream()
                outbit <<= j
                keystream[i] = keystream[i] | outbit
        return keystream

    def encrypt(self, msg):
        keystream = self.keystream_bytes(len(msg))
        
        cipher = [x^y for x,y in zip(msg, keystream)]

        return cipher
    
    def decrypt(self, msg):
        keystream = self.keystream_bytes(len(msg))
        
        plain = [x^y for x,y in zip(msg, keystream)]

        return plain